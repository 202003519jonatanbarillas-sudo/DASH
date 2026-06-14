from sqlalchemy import create_engine
import pandas as pd
import json

# =====================================
# CONEXIÓN
# =====================================
engine = create_engine("mysql+pymysql://root:Admin@localhost/global_supply")

with engine.connect() as conn:
    df = pd.read_sql("SELECT * FROM supply", conn)

# =====================================
# FECHAS Y RISK SCORE
# =====================================
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce", dayfirst=True)

df["risk_score"] = (
    df["Geopolitical_Risk_Index"].astype(float) * 0.6 +
    (df["Weather_Severity_Index"].astype(float) / 10) * 0.4
)

df["risk_level"] = pd.cut(
    df["risk_score"],
    bins=[0, 0.33, 0.66, 1],
    labels=["Low", "Medium", "High"]
)

df["Year"] = df["Order_Date"].dt.year
df["Month"] = df["Order_Date"].dt.month
df["Quarter"] = df["Order_Date"].dt.quarter


# =====================================
# CÁLCULO DE KPIs DINÁMICOS
# =====================================
total_shipments = len(df)
on_time_rate = df["Delivery_Status"].eq("On Time").mean() * 100 if total_shipments > 0 else 0
avg_delay = df["Delay_Days"].mean() if total_shipments > 0 else 0
total_cost_m = df["Shipping_Cost_USD"].sum() / 1_000_000 # Convertido a Millones
high_risk_count = (df["risk_level"] == "High").sum()

# =====================================
# PANEL IZQUIERDO (HTML GENERADO)
# =====================================
# Calculamos top 4 disrupciones y sus porcentajes
disruptions = df["Disruption_Event"].value_counts()
tot_dis = disruptions.sum()
disruptions_html = ""
for name, count in disruptions.head(4).items():
    pct = (count / tot_dis) * 100 if tot_dis > 0 else 0
    disruptions_html += f'<div class="rank-item"><span>{name}</span><span class="rank-value">{pct:.0f}%</span></div>\n'

# Calculamos top 4 medios de transporte y sus porcentajes
transport = df["Transportation_Mode"].value_counts()
tot_trans = transport.sum()
transport_html = ""
for name, count in transport.head(4).items():
    pct = (count / tot_trans) * 100 if tot_trans > 0 else 0
    transport_html += f'<div class="rank-item"><span>{name}</span><span class="rank-value">{pct:.0f}%</span></div>\n'

# =====================================
# PANEL DERECHO (MAYOR RIESGO)
# =====================================
highest = df.sort_values("risk_score", ascending=False).iloc[0] if not df.empty else None
if highest is not None:
    high_route = f"{highest.get('Origin_City', 'N/A')}<br>⬇<br>{highest.get('Destination_City', 'N/A')}"
    high_score = f"{highest.get('risk_score', 0):.1f}"
    high_delay = f"+{highest.get('Delay_Days', 0):.1f} Days"
else:
    high_route, high_score, high_delay = "N/A", "0.0", "0 Days"

# =====================================
# MAPA ECHARTS (PREPARACIÓN DE DATOS)
# =====================================
map_routes = (
    df.dropna(subset=["origin_lat", "origin_lon", "destination_lat", "destination_lon"])
    .groupby(["Origin_City", "Destination_City"])
    .agg(
        Shipments=("Order_ID", "count"),
        Avg_Risk=("risk_score", "mean"),
        origin_lat=("origin_lat", "first"),
        origin_lon=("origin_lon", "first"),
        destination_lat=("destination_lat", "first"),
        destination_lon=("destination_lon", "first")
    ).reset_index()
)

routes = []
max_shipments = map_routes["Shipments"].max() if not map_routes.empty else 1

for _, row in map_routes.iterrows():
    risk = float(row["Avg_Risk"])
    color = "#ef4444" if risk >= 0.66 else "#f59e0b" if risk >= 0.33 else "#00f0ff"
    width = 1.5

    routes.append({
        "fromName": row["Origin_City"],
        "toName": row["Destination_City"],
        "coords": [
            [float(row["origin_lon"]), float(row["origin_lat"])],
            [float(row["destination_lon"]), float(row["destination_lat"])]
        ],
        "lineStyle": {"color": color, "width": width},
        "risk": round(risk, 2),
        "shipments": int(row["Shipments"])
    })

# =====================================
# OPCIONES DE FILTROS
# =====================================

routes_filter = ["All"] + sorted(
    df["Route_Type"]
      .dropna()
      .unique()
      .tolist()
)

products_filter = ["All"] + sorted(
    df["Product_Category"]
      .dropna()
      .unique()
      .tolist()
)

transport_filter = ["All"] + sorted(
    df["Transportation_Mode"]
      .dropna()
      .unique()
      .tolist()
)

risk_filter = [
    "All",
    "Low",
    "Medium",
    "High"
]

years_filter = ["All"] + sorted(
    df["Year"]
      .dropna()
      .unique()
      .astype(int)
      .tolist()
)

# =====================================
# JSON PARA JAVASCRIPT
# =====================================

df["Year"] = df["Year"].fillna(0).astype(int)

routes_json = json.dumps(routes)

routes_filter_json = json.dumps(routes_filter)

products_filter_json = json.dumps(products_filter)

transport_filter_json = json.dumps(transport_filter)

risk_filter_json = json.dumps(risk_filter)

years_filter_json = json.dumps(years_filter)

records_json = json.dumps(
    df.to_dict("records"),
    default=str
)
# =====================================
# PLANTILLA HTML MAESTRA
# =====================================
# Usamos placeholders como __VARIABLE__ para evitar conflictos con el CSS
html_template = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Supply Chain Resilience Dashboard</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;500;600;700;800;900&display=swap" rel="stylesheet">
  
  <script src="https://cdn.jsdelivr.net/npm/echarts@5/dist/echarts.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/echarts@4.9.0/map/js/world.js"></script>

  <style>
/* RESET */
    * { margin:0; padding:0; box-sizing:border-box; }
    html, body { width:100%; height:100%; overflow:hidden; }

    body {
      font-family:'Inter',sans-serif;
      color:var(--text);
      background: linear-gradient(135deg, var(--background-start), var(--background-mid), var(--background-end));
    }

    /* Patrón de fondo */
    body::before {
      content:""; position:fixed; inset:0;
      background-image: linear-gradient(rgba(255,255,255,.03) 1px, transparent 1px),
                        linear-gradient(90deg, rgba(255,255,255,.03) 1px, transparent 1px);
      background-size:40px 40px;
      pointer-events:none;
    }

    :root {
      --background-start: #0a0a0a; --background-mid: #171717; --background-end: #262626;
      --panel: rgba(30, 30, 30, 0.85); --border: rgba(255, 255, 255, 0.06);
      --accent: #d97706; --accent-soft: #f59e0b; --highlight: #b45309;
      --success: #65a30d; --warning: #ca8a04; --danger: #e11d48; --info: #71717a;
      --text: #f3f4f6; --muted: #a3a3a3; --shadow: 0 20px 40px rgba(0,0,0,.7);
    }

    /* LAYOUT OPTIMIZADO */
    .dashboard {
      height:100vh; 
      padding: 10px; 
      display:grid; 
      gap: 10px; 
      grid-template-rows: auto auto auto minmax(0,1fr) auto;
      overflow:hidden;
    }

    .panel {
      background:var(--panel); border:1px solid var(--border);
      backdrop-filter:blur(18px); border-radius:20px;
      box-shadow:var(--shadow);
    }

    .header {
      display: grid;
      grid-template-columns: 1fr auto 1fr;
      align-items: center;
      padding: 12px 20px;
    }
    .title { font-size:1.5rem; font-weight:900; letter-spacing:.05em; background:linear-gradient(135deg,#ffffff,var(--accent)); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }
    .subtitle { font-size:.65rem; color:var(--muted); letter-spacing:.2em; text-transform:uppercase; }
    /* Mejora de los filtros */
    .filters select { 
        min-width: 140px; 
        background: #1f1f1f; /* Color oscuro sólido (evita transparencia) */
        border: 1px solid var(--border); 
        color: #ffffff; 
        padding: 8px 12px; 
        border-radius: 10px; 
        cursor: pointer;
        transition: all 0.3s ease;
        font-size: 0.85rem;
    }
    
    /* Efecto al pasar el mouse por encima */
    .filters select:hover { 
        border-color: var(--accent); 
        background: #2a2a2a; 
    }
    
    /* Mejora visual al estar seleccionado */
    .filters select:focus { 
        outline: none; 
        border-color: var(--accent); 
        box-shadow: 0 0 0 2px rgba(217, 119, 6, 0.2);
    }
    
    .ribbon { display:grid; grid-template-columns:repeat(4,1fr); gap:10px; }
    .status-chip { background:var(--panel); border:1px solid var(--border); border-radius:12px; height:40px; display:flex; justify-content:center; align-items:center; font-weight:700; font-size:.75rem; }
    
    .kpi-grid { display:grid; grid-template-columns:repeat(5,1fr); gap:10px; }
    .kpi-card { position:relative; padding:14px; border-radius:16px; background:var(--panel); border:1px solid var(--border); min-height:0; }
    .kpi-card::before { content:""; position:absolute; left:0; top:0; width:100%; height:2px; background:linear-gradient(90deg,#d97706,#b45309); }
    .kpi-label { color:var(--muted); font-size:.65rem; text-transform:uppercase; }
    .kpi-value { margin-top:6px; font-size:1.6rem; font-weight:900; color:var(--accent); }
    .kpi-change { margin-top:4px; font-size:.65rem; color:#cbd5e1; }

    .content { display:grid; gap:10px; grid-template-columns:260px minmax(0,1fr) 300px; min-height:0; }
    .card { background:var(--panel); border:1px solid var(--border); border-radius:20px; padding:16px; display:flex; flex-direction:column; gap:10px; overflow:hidden; }
    .card-title { font-size:.75rem; font-weight:700; text-transform:uppercase; color:#cbd5e1; z-index: 10; }
    
    .rank-item { display:flex; justify-content:space-between; align-items:center; padding:8px 10px; border-radius:10px; background:rgba(255,255,255,.03); font-size: 0.85rem;}
    .rank-value { color:var(--accent); font-weight:700; }

    /* Contenedor del mapa ajustado para ECharts */
    .map-container { flex:1; border-radius:16px; display:flex; justify-content:center; align-items:center; color:rgba(255,255,255,.25); width: 100%; height: 100%; min-height: 300px; }

    .ai-card { background:linear-gradient(145deg,rgba(40,20,10,.6),rgba(15,10,5,.92)); }
    .risk-score { margin:8px 0; font-size:2rem; font-weight:900; color:#f87171; }
    .recommendation { margin-top:10px; padding:10px; border-radius:10px; background:rgba(239,68,68,.08); border:1px solid rgba(239,68,68,.2); font-size: 0.85rem; }

    .footer { display:flex; justify-content:center; align-items:center; color:var(--muted); font-size:.7rem; padding-bottom: 5px;}
    .fullscreen-btn { position:fixed; top:15px; right:15px; width:36px; height:36px; border:none; border-radius:10px; background:rgba(0,0,0,.5); border:1px solid var(--border); color:var(--accent); cursor:pointer; z-index:999; }

  </style>
</head>
<body>

<div class="dashboard">

  <header class="panel header">
    <div class="title-group">
      <div class="title">GLOBAL SUPPLY CHAIN</div>
      <div class="subtitle">RESILIENCE MONITOR</div>
    </div>
    
<div class="filters">
    <select id="routeFilter" onchange="applyFilters()">
        <option value="All">All Routes</option>
    </select>
    <select id="productFilter" onchange="applyFilters()">
        <option value="All">All Products</option>
    </select>
    <select id="transportFilter" onchange="applyFilters()">
        <option value="All">All Modes</option>
    </select>
    <select id="yearFilter" onchange="applyFilters()">
        <option value="All">All Years</option>
    </select>
    <button class="fullscreen-btn" onclick="toggleFullscreen()">⛶</button>
</div>

  </header>

  <section class="ribbon">
    <div class="status-chip status-green">SUEZ • NORMAL</div>
    <div class="status-chip status-yellow">PACIFIC • WARNING</div>
    <div class="status-chip status-green">ATLANTIC • STABLE</div>
    <div class="status-chip status-red">GLOBAL RISK • MODERATE</div>
  </section>

    <section class="kpi-grid">
        <div class="kpi-card"><div class="kpi-label">Total Shipments</div><div class="kpi-value" id="kpi-shipments">__KPI_SHIPMENTS__</div><div class="kpi-change">Real time</div></div>
        <div class="kpi-card"><div class="kpi-label">On Time Rate</div><div class="kpi-value" id="kpi-ontime">__KPI_ONTIME__</div><div class="kpi-change">Real time</div></div>
        <div class="kpi-card"><div class="kpi-label">Avg Delay</div><div class="kpi-value" id="kpi-delay">__KPI_DELAY__</div><div class="kpi-change">Days</div></div>
        <div class="kpi-card"><div class="kpi-label">Logistics Cost</div><div class="kpi-value" id="kpi-cost">__KPI_COST__</div><div class="kpi-change">Real time</div></div>
        <div class="kpi-card"><div class="kpi-label">High Risk Routes</div><div class="kpi-value" id="kpi-risk">__KPI_RISK__</div><div class="kpi-change">Active Alerts</div></div>
    </section>

  <section class="content">

    <aside class="card">
      <div class="card-title">Disruption Events</div>
      __DISRUPTIONS_LIST__
      <br>
      <div class="card-title">Transport Mode</div>
      __TRANSPORT_LIST__
    </aside>

    <main class="card" style="padding: 0; position: relative;">
      <div class="card-title" style="position: absolute; top: 16px; left: 16px;">Global Logistics Network</div>
      <div class="map-container" id="map"></div>
    </main>

    <aside class="card ai-card">
      <div class="card-title">AI Risk Engine</div>
      <div class="alert-box">
        <strong style="font-size:0.8rem;">__HIGH_ROUTE_NAME__</strong><br><br>
        Risk Score
        <div class="risk-score">__HIGH_RISK_VAL__</div>
        Expected Delay <p style="color:var(--accent);">__HIGH_DELAY_VAL__</p><br>
        <div class="recommendation">
          <strong>Recommended Action</strong><br><br>
          EXPEDITED ROUTING
        </div>
      </div>

      <div class="card-title" style="margin-top:10px;">Active Alerts</div>
      <div class="rank-item"><span>Suez Canal</span><span class="rank-value">HIGH</span></div>
      <div class="rank-item"><span>Shanghai Route</span><span class="rank-value">MEDIUM</span></div>
      <div class="rank-item"><span>Atlantic Route</span><span class="rank-value">LOW</span></div>
    </aside>

  </section>

  <footer class="footer">
    Supply Chain Analytics Engine © 2026
  </footer>

</div>

<script>
// Carga los datos (esto se reemplaza por el JSON de Python)
const allData = __RECORDS_JSON__; 

// Carga las opciones de los filtros
const routesOptions = __ROUTES_FILTER_JSON__;
const productsOptions = __PRODUCTS_FILTER_JSON__;
const transportOptions = __TRANSPORT_FILTER_JSON__;
const yearsOptions = __YEARS_FILTER_JSON__;

// Asegúrate de que esto se ejecute al cargar la página
document.addEventListener("DOMContentLoaded", function() {
    populateFilters(routesOptions, "routeFilter");
    populateFilters(productsOptions, "productFilter");
    populateFilters(transportOptions, "transportFilter");
    populateFilters(yearsOptions, "yearFilter");
});

function populateFilters(options, elementId) {
    const select = document.getElementById(elementId);
    options.forEach(option => {
        if (option !== "All") { // "All" ya está en el HTML
            const el = document.createElement("option");
            el.value = option;
            el.textContent = option;
            select.appendChild(el);
        }
    });
}
  function toggleFullscreen() {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen();
    } else {
      if (document.exitFullscreen) {
        document.exitFullscreen();
      }
    }
  }

  // ==========================================
  // INICIALIZACIÓN DE ECHARTS
  // ==========================================
  const routesData = __ROUTES_JSON__;
  const chart = echarts.init(document.getElementById("map"));

  const option = {
      backgroundColor: "transparent", // Permite que el fondo de tu tarjeta CSS sea visible
      tooltip: { trigger: "item" },
      geo: {
          map: "world",
          roam: true,
          zoom: 1.2,
          label: {
              show: false, // Ponlo en 'true' si quieres ver todos los nombres siempre
              color: "#d97706" 
          },
          itemStyle: {
              areaColor: "rgba(255, 255, 255, 0.03)", 
              borderColor: "rgba(255, 255, 255, 0.1)",
              borderWidth: 1
          },
          emphasis: {
              itemStyle: { 
                  areaColor: "rgba(217, 119, 6, 0.2)" 
              },
              // 2. Controla el texto cuando PASAS EL MOUSE por encima (Hover)
              label: {
                  show: true,
                  color: "#f59e0b", // El anaranjado dorado brillante
                  fontWeight: "bold",
                  fontSize: 14
              }
          }
      },
      series: [{
          type: "lines",
          coordinateSystem: "geo",
          zlevel: 2,
          effect: {
              show: true,
              period: 4,
              trailLength: 0.4,
              symbol: "arrow",
              symbolSize: 6
          },
          lineStyle: {
              opacity: 0.6,
              curveness: 0.25,
              cap: "round",   // Redondea las puntas de las líneas
              join: "round"   // Suaviza las intersecciones si las hubiera
          },
          tooltip: {
              formatter: function(params) {
                  return `
                      <div style="padding: 4px; font-family: Inter, sans-serif;">
                          <b>${params.data.fromName}</b> → <b>${params.data.toName}</b><br>
                          <span style="color: #94a3b8;">Shipments:</span> <b>${params.data.shipments}</b><br>
                          <span style="color: #94a3b8;">Avg Risk:</span> <b>${params.data.risk}</b>
                      </div>
                  `;
              }
          },
          data: routesData
      }]
  };

  chart.setOption(option);
  window.addEventListener("resize", () => chart.resize());
function applyFilters() {
    // 1. Obtener valores seleccionados
    const route = document.getElementById("routeFilter").value;
    const product = document.getElementById("productFilter").value;
    const mode = document.getElementById("transportFilter").value;
    const year = document.getElementById("yearFilter").value;

    // 2. Filtrar el dataset global
    const filtered = allData.filter(row => {
        return (route === "All" || row.Route_Type === route) &&
               (product === "All" || row.Product_Category === product) &&
               (mode === "All" || row.Transportation_Mode === mode) &&
               (year === "All" || row.Year == year);
    });

    // 3. Ejecutar actualizaciones
    updateKPIs(filtered);
    updateMap(filtered);
    updateRankings(filtered);
    updateRiskEngine(filtered);
}

function updateKPIs(data) {
    const total = data.length;
    // Cálculos rápidos
    const onTimeRate = total > 0 ? (data.filter(r => r.Delivery_Status === "On Time").length / total) * 100 : 0;
    const avgDelay = total > 0 ? (data.reduce((acc, curr) => acc + (curr.Delay_Days || 0), 0) / total) : 0;
    const totalCost = data.reduce((acc, curr) => acc + (curr.Shipping_Cost_USD || 0), 0) / 1_000_000;
    const highRisk = data.filter(r => r.risk_level === "High").length;

    // Actualizar el DOM (Asegúrate de que tus elementos HTML tengan estos IDs)
    document.getElementById("kpi-shipments").innerText = total.toLocaleString();
    document.getElementById("kpi-ontime").innerText = onTimeRate.toFixed(1) + "%";
    document.getElementById("kpi-delay").innerText = avgDelay.toFixed(1);
    document.getElementById("kpi-cost").innerText = "$" + totalCost.toFixed(1) + "M";
    document.getElementById("kpi-risk").innerText = highRisk;
}

function updateMap(data) {
    // 1. Agrupamos los datos
    const routeGroups = {};

    data.forEach(row => {
        if (!row.origin_lat || !row.destination_lat) return;
        
        const key = `${row.Origin_City}-${row.Destination_City}`;
        
        if (!routeGroups[key]) {
            routeGroups[key] = {
                fromName: row.Origin_City,
                toName: row.Destination_City,
                coords: [[row.origin_lon, row.origin_lat], [row.destination_lon, row.destination_lat]],
                shipments: 0,
                riskSum: 0
            };
        }
        
        routeGroups[key].shipments += 1;
        routeGroups[key].riskSum += (parseFloat(row.risk_score) || 0);
    });

    // 2. Convertimos a array
    const optimizedRoutes = Object.values(routeGroups).map(r => {
        const avgRisk = r.riskSum / r.shipments;
        let color = "#00f0ff"; 
        if (avgRisk >= 0.66) color = "#ef4444";
        else if (avgRisk >= 0.33) color = "#f59e0b";

        return {
            fromName: r.fromName,
            toName: r.toName,
            coords: r.coords,
            lineStyle: { 
                color: color, 
                width: 1.5
            },
            risk: avgRisk.toFixed(2),
            shipments: r.shipments
        };
    });

    // 3. Actualizar solo la serie de datos
    // Ya NO usamos { notMerge: true }. 
    // ECharts actualizará solo la información de las rutas sin borrar el mapa.
    chart.setOption({
        series: [{
            data: optimizedRoutes
        }]
    });
}
function updateRankings(data) {
    console.log("Actualizando Rankings con:", data.length);
    // Aquí podrías agregar lógica futura para actualizar las listas del panel izquierdo
}

function updateRiskEngine(data) {
    console.log("Actualizando Risk Engine con:", data.length);
    // Aquí podrías agregar lógica futura para actualizar el panel derecho
}
</script>

</body>
</html>"""

html_final = html_template

# =========================
# DATOS JS
# =========================

html_final = html_final.replace(
    "__ROUTES_JSON__",
    routes_json
)

html_final = html_final.replace(
    "__RECORDS_JSON__",
    records_json
)

html_final = html_final.replace(
    "__ROUTES_FILTER_JSON__",
    routes_filter_json
)

html_final = html_final.replace(
    "__PRODUCTS_FILTER_JSON__",
    products_filter_json
)

html_final = html_final.replace(
    "__TRANSPORT_FILTER_JSON__",
    transport_filter_json
)

html_final = html_final.replace(
    "__RISK_FILTER_JSON__",
    risk_filter_json
)

html_final = html_final.replace(
    "__YEARS_FILTER_JSON__",
    years_filter_json
)

# =========================
# KPIs
# =========================

html_final = html_final.replace(
    "__KPI_SHIPMENTS__",
    f"{total_shipments:,}"
)

html_final = html_final.replace(
    "__KPI_ONTIME__",
    f"{on_time_rate:.1f}%"
)

html_final = html_final.replace(
    "__KPI_DELAY__",
    f"{avg_delay:.1f}"
)

html_final = html_final.replace(
    "__KPI_COST__",
    f"${total_cost_m:.1f}M"
)

html_final = html_final.replace(
    "__KPI_RISK__",
    str(high_risk_count)
)

# =========================
# PANEL IZQUIERDO
# =========================

html_final = html_final.replace(
    "__DISRUPTIONS_LIST__",
    disruptions_html
)

html_final = html_final.replace(
    "__TRANSPORT_LIST__",
    transport_html
)

# =========================
# PANEL DERECHO
# =========================

html_final = html_final.replace(
    "__HIGH_ROUTE_NAME__",
    high_route
)

html_final = html_final.replace(
    "__HIGH_RISK_VAL__",
    high_score
)

html_final = html_final.replace(
    "__HIGH_DELAY_VAL__",
    high_delay
)

# =========================
# GUARDAR HTML
# =========================

with open(
    "dashboard.html",
    "w",
    encoding="utf-8"
) as f:

    f.write(html_final)

print("✅ dashboard.html generado")
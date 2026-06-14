import json
from sqlalchemy import create_engine
import pandas as pd

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

# Asegurar enteros para el año antes de procesar filtros y JSON
df["Year"] = df["Year"].fillna(0).astype(int)

# =====================================
# CÁLCULO DE KPIs DINÁMICOS
# =====================================
total_shipments = len(df)
on_time_rate = df["Delivery_Status"].eq("On Time").mean() * 100 if total_shipments > 0 else 0
avg_delay = df["Delay_Days"].mean() if total_shipments > 0 else 0
total_cost_m = df["Shipping_Cost_USD"].sum() / 1_000_000 
high_risk_count = (df["risk_level"] == "High").sum()

# =====================================
# PANEL IZQUIERDO (GAUGES DATA)
# =====================================
mode_pcts = df["Transportation_Mode"].value_counts(normalize=True).head(2)
transport_data = mode_pcts.to_dict()
transport_gauges_json = json.dumps(transport_data)

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
for _, row in map_routes.iterrows():
    risk = float(row["Avg_Risk"])
    color = "#ef4444" if risk >= 0.66 else "#f59e0b" if risk >= 0.33 else "#00f0ff"
    
    routes.append({
        "fromName": row["Origin_City"],
        "toName": row["Destination_City"],
        "coords": [
            [float(row["origin_lon"]), float(row["origin_lat"])],
            [float(row["destination_lon"]), float(row["destination_lat"])]
        ],
        "lineStyle": {"color": color, "width": 1.5},
        "risk": round(risk, 2),
        "shipments": int(row["Shipments"])
    })

# =====================================
# OPCIONES DE FILTROS
# =====================================
routes_filter = ["All"] + sorted(df["Route_Type"].dropna().unique().tolist())
products_filter = ["All"] + sorted(df["Product_Category"].dropna().unique().tolist())
transport_filter = ["All"] + sorted(df["Transportation_Mode"].dropna().unique().tolist())
risk_filter = ["All", "Low", "Medium", "High"]
years_filter = ["All"] + sorted(df["Year"].dropna().unique().astype(int).tolist())

# =====================================
# SERIALIZACIÓN SEGURA DE JSON (Evita NaNs rotos)
# =====================================
df_clean = df.where(pd.notnull(df), None)

routes_json = json.dumps(routes)
routes_filter_json = json.dumps(routes_filter)
products_filter_json = json.dumps(products_filter)
transport_filter_json = json.dumps(transport_filter)
risk_filter_json = json.dumps(risk_filter)
years_filter_json = json.dumps(years_filter)
records_json = json.dumps(df_clean.to_dict("records"), default=str)

# =====================================
# PLANTILLA HTML MAESTRA
# =====================================
html_template = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Supply Chain Resilience Dashboard</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;500;600;700;800;900&display=swap" rel="stylesheet">
  
  <script src="https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/echarts.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/echarts-liquidfill@3.1.0/dist/echarts-liquidfill.min.js"></script>
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
    
    .filters select { 
        min-width: 140px; 
        background: #1f1f1f; 
        border: 1px solid var(--border); 
        color: #ffffff; 
        padding: 8px 12px; 
        border-radius: 10px; 
        cursor: pointer;
        transition: all 0.3s ease;
        font-size: 0.85rem;
    }
    
    .filters select:hover { border-color: var(--accent); background: #2a2a2a; }
    .filters select:focus { outline: none; border-color: var(--accent); box-shadow: 0 0 0 2px rgba(217, 119, 6, 0.2); }
    
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
    
    .rank-item { display:flex; justify-content:space-between; align-items:center; padding:8px 10px; border-radius:10px; background:rgba(255,255,255,.03); font-size: 0.85rem; margin-bottom: 4px; }
    .rank-value { font-weight:700; }

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
    <div style="display: flex; flex-direction: column; gap: 10px;">
        <aside class="card">
            <div class="card-title">Disruption Events</div>
            <div id="disruptions_chart" style="width: 100%; height: 180px;"></div>
        </aside>

        <aside class="card">
            <div class="card-title">Top Transport Modes</div>
            <div style="display: flex; justify-content: space-around; align-items: center; padding: 10px 0;">
                <div id="gauge_t1" style="width: 125px; height: 125px;"></div>
                <div id="gauge_t2" style="width: 125px; height: 125px;"></div>
            </div>
        </aside>
    </div>

    <main class="card" style="padding: 0; position: relative;">
      <div class="card-title" style="position: absolute; top: 16px; left: 16px; z-index: 10;">Global Logistics Network</div>
      <div class="map-container" id="map"></div>
    </main>

    <aside class="card ai-card">
      <div class="card-title">AI Risk Engine</div>
      <div class="alert-box">
        <strong style="font-size:0.8rem;" id="high-route-name">__HIGH_ROUTE_NAME__</strong><br><br>
        Risk Score
        <div class="risk-score" id="high-risk-val">__HIGH_RISK_VAL__</div>
        Expected Delay <p style="color:var(--accent);" id="high-delay-val">__HIGH_DELAY_VAL__</p><br>
        <div class="recommendation">
          <strong>Recommended Action</strong><br><br>
          EXPEDITED ROUTING
        </div>
      </div>

      <div class="card-title" style="margin-top:10px;">Active Alerts</div>
      <div id="alerts-container">
         </div>
    </aside>
  </section>

  <footer class="footer">
    Supply Chain Analytics Engine © 2026
  </footer>
</div>

<script type="application/json" id="data-records">__RECORDS_JSON__</script>
<script type="application/json" id="data-routes">__ROUTES_JSON__</script>
<script type="application/json" id="data-transport">__TRANSPORT_GAUGES_JSON__</script>
<script type="application/json" id="filter-routes">__ROUTES_FILTER_JSON__</script>
<script type="application/json" id="filter-products">__PRODUCTS_FILTER_JSON__</script>
<script type="application/json" id="filter-transport">__TRANSPORT_FILTER_JSON__</script>
<script type="application/json" id="filter-years">__YEARS_FILTER_JSON__</script>

<script>
const allData = JSON.parse(document.getElementById('data-records').textContent); 
const routesData = JSON.parse(document.getElementById('data-routes').textContent);
const transportData = JSON.parse(document.getElementById('data-transport').textContent);
const routesOptions = JSON.parse(document.getElementById('filter-routes').textContent);
const productsOptions = JSON.parse(document.getElementById('filter-products').textContent);
const transportOptions = JSON.parse(document.getElementById('filter-transport').textContent);
const yearsOptions = JSON.parse(document.getElementById('filter-years').textContent);

let chart; 
let disruptionsChart; 

document.addEventListener("DOMContentLoaded", function() {
    populateFilters(routesOptions, "routeFilter");
    populateFilters(productsOptions, "productFilter");
    populateFilters(transportOptions, "transportFilter");
    populateFilters(yearsOptions, "yearFilter");

    const modes = Object.entries(transportData);
    if(modes[0]) renderGauge('gauge_t1', modes[0][0], modes[0][1]);
    if(modes[1]) renderGauge('gauge_t2', modes[1][0], modes[1][1]);

    initMap();
    initDisruptionsChart(); 
    applyFilters();         
});

function initMap() {
    const chartDom = document.getElementById("map");
    chart = echarts.init(chartDom);

    const option = {
        backgroundColor: "transparent",
        tooltip: { 
            trigger: "item",
            backgroundColor: 'transparent',
            borderWidth: 0,
            padding: 0,
            shadowBlur: 0,
            extraCssText: 'box-shadow: none; background: transparent; border: none;'
        },
        geo: {
            map: "world",
            roam: true,
            zoom: 1.2,

            // ➔ EL PARCHE ESTÁ AQUÍ: Desactiva por completo el texto negro/gris fijo del mapa
            label: {
                show: false
            },

            itemStyle: {
                areaColor: "rgba(255, 255, 255, 0.03)", 
                borderColor: "rgba(255, 255, 255, 0.1)",
                borderWidth: 1
            },
            emphasis: {
                itemStyle: { areaColor: "rgba(217, 119, 6, 0.2)" },
                // El texto SOLO se activará en Hover y con tu estilo premium ámbar
                label: { show: true, color: "#f59e0b", fontWeight: "bold", fontSize: 14 }
            }
        },
        series: [{
            type: "lines",
            coordinateSystem: "geo",
            zlevel: 2,
            effect: { show: true, period: 4, trailLength: 0.4, symbol: "arrow", symbolSize: 6 },
            lineStyle: { opacity: 0.6, curveness: 0.25, cap: "round", join: "round" },
            tooltip: {
                formatter: function(params) {
                    if (!params.data) return '';
                    
                    const rVal = parseFloat(params.data.risk);
                    const riskColor = rVal >= 0.66 ? '#ef4444' : rVal >= 0.33 ? '#f59e0b' : '#00f0ff';

                    return `
                        <div style="background: #141414; border: 1px solid #d97706; border-radius: 12px; padding: 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.8); font-family: 'Inter', sans-serif; min-width: 200px;">
                            <div style="color: #858585; font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 4px;">Logística de Ruta</div>
                            <div style="color: #ffffff; font-weight: 700; font-size: 13px; margin-bottom: 10px;">
                                ${params.data.fromName} <span style="color: #d97706;">➔</span> ${params.data.toName}
                            </div>
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px; font-size: 12px;">
                                <span style="color: #94a3b8;">Envíos Totales:</span>
                                <span style="color: #ffffff; font-weight: 700;">${Number(params.data.shipments).toLocaleString()}</span>
                            </div>
                            <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid rgba(255,255,255,0.06); padding-top: 8px; font-size: 12px;">
                                <span style="color: #94a3b8;">Riesgo Promedio:</span>
                                <span style="color: ${riskColor}; font-weight: 800; font-size: 13px;">${params.data.risk}</span>
                            </div>
                        </div>
                    `;
                }
            },
            data: routesData
        }]
    };
    chart.setOption(option);
    window.addEventListener("resize", () => chart.resize());
}

function initDisruptionsChart() {
    const chartDom = document.getElementById("disruptions_chart");
    if (!chartDom) return;

    disruptionsChart = echarts.init(chartDom);

    const option = {
        backgroundColor: "transparent",
        animationDuration: 700,
        animationEasing: 'cubicOut',
        tooltip: {
            trigger: 'axis',
            backgroundColor: 'transparent',
            borderWidth: 0,
            padding: 0,
            shadowBlur: 0,
            extraCssText: 'box-shadow: none; background: transparent; border: none; z-index: 9999;',
            axisPointer: { 
                type: 'shadow',
                shadowStyle: {
                    color: 'rgba(255, 255, 255, 0.02)' 
                }
            },
            // ➔ AQUÍ ESTÁ LA SOLUCIÓN DEFINITIVA PARA EL CORTE IZQUIERDO
            position: function (point, params, dom, rect, size) {
                // point[0] = X del mouse, point[1] = Y del mouse
                // size.contentSize = [ancho, alto] del tooltip flotante
                // size.viewSize = [ancho, alto] del contenedor de la gráfica
                
                // 1. Forzamos a que se dibuje 20px a la DERECHA del cursor
                let x = point[0] + 20; 
                let y = point[1] - (size.contentSize[1] / 2); // Centrado vertical sutil

                // 2. Si el usuario se va muy a la derecha y el tooltip se sale de la gráfica, 
                // lo pateamos temporalmente a la izquierda del cursor.
                if (x + size.contentSize[0] > size.viewSize[0]) {
                    x = point[0] - size.contentSize[0] - 20;
                }

                // 3. Línea de vida: Si por alguna razón X intenta ser menor a 15px (tu zona de peligro),
                // lo obligamos a quedarse estático en 15px para que nunca se mutile.
                if (x < 15) x = 15;
                if (y < 5) y = 5;

                return [x, y];
            },
            formatter: function(params) {
                const p = params[0];
                if (!p || p.value === undefined) return '';
                
                return `
                    <div style="background: #141414; border: 1px solid #d97706; border-radius: 25px; padding: 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.8); font-family: 'Inter', sans-serif; width: 180px; box-sizing: border-box;">
                        <div style="color: #858585; font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 2px;">Métrica de Evento</div>
                        <div style="color: #ffffff; font-weight: 700; font-size: 13px; margin-bottom: 5px; white-space: normal; word-break: break-word;">${p.name}</div>
                        <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid rgba(255,255,255,0.06); padding-top: 5px;">
                            <span style="color: #d97706; font-size: 11px; font-weight: 600;">Frecuencia:</span>
                            <span style="color: #f3f4f6; font-weight: 800; font-size: 12.5px;">${p.value}%</span>
                        </div>
                    </div>
                `;
            }
        },
        grid: { 
            left: 10,       
            right: 45,     
            bottom: 5, 
            top: 17.5,       
            containLabel: false 
        },
        xAxis: { type: 'value', show: false },
        yAxis: {
            type: 'category',
            data: [],
            axisLine: { show: false },
            axisTick: { show: false },
            axisLabel: { show: false } 
        },
        series: [
            {
                name: 'Barras Visibles',
                type: 'bar',
                data: [],
                barWidth: '45%',
                showBackground: true,
                backgroundStyle: { color: 'rgba(255, 255, 255, 0.02)', borderRadius: 5 },
                label: {
                    show: true,
                    position: 'right',
                    formatter: '{c}%',
                    color: '#d97706',
                    fontWeight: 'bold',
                    fontFamily: 'Inter'
                }
            },
            {
                name: 'Texto Flotante',
                type: 'bar',
                data: [],
                barWidth: '45%',
                barGap: '-100%', 
                itemStyle: { color: 'transparent' }, 
                label: {
                    show: true,
                    position: [0, -16], 
                    formatter: function(params) {
                        return params.name; 
                    },
                    color: '#f3f4f6',
                    fontSize: 12.5,
                    fontFamily: 'Inter'
                }
            }
        ]
    };
    disruptionsChart.setOption(option);
    window.addEventListener("resize", () => disruptionsChart.resize());
}

function renderGauge(elementId, mode, value) {
    const gaugeChart = echarts.init(document.getElementById(elementId));
    const option = {
        series: [{
            type: 'liquidFill',
            data: [value],
            radius: '95%',
            color: ['#d97706'], 
            backgroundStyle: { color: 'rgba(255, 255, 255, 0.03)' },
            label: { 
                formatter: mode + '\\n' + (value * 100).toFixed(0) + '%', 
                fontSize: 14,
                color: '#ffffff',       
                insideColor: '#1e1e1e'  
            },
            outline: { show: false }
        }]
    };
    gaugeChart.setOption(option);
}

function populateFilters(options, elementId) {
    const select = document.getElementById(elementId);
    options.forEach(option => {
        if (option !== "All") {
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
    } else if (document.exitFullscreen) {
        document.exitFullscreen();
    }
}

function applyFilters() {
    const route = document.getElementById("routeFilter").value;
    const product = document.getElementById("productFilter").value;
    const mode = document.getElementById("transportFilter").value;
    const year = document.getElementById("yearFilter").value;

    const filtered = allData.filter(row => {
        return (route === "All" || row.Route_Type === route) &&
               (product === "All" || row.Product_Category === product) &&
               (mode === "All" || row.Transportation_Mode === mode) &&
               (year === "All" || row.Year == year);
    });

    updateKPIs(filtered);
    updateMap(filtered);
    updateRankings(filtered);
    updateRiskEngine(filtered);
    updateGauges(filtered);
    updateDisruptionsChart(filtered); 
}

function updateKPIs(data) {
    const total = data.length;
    const onTimeRate = total > 0 ? (data.filter(r => r.Delivery_Status === "On Time").length / total) * 100 : 0;
    const avgDelay = total > 0 ? (data.reduce((acc, curr) => acc + (curr.Delay_Days || 0), 0) / total) : 0;
    const totalCost = data.reduce((acc, curr) => acc + (curr.Shipping_Cost_USD || 0), 0) / 1_000_000;
    const highRisk = data.filter(r => r.risk_level === "High").length;

    document.getElementById("kpi-shipments").innerText = total.toLocaleString();
    document.getElementById("kpi-ontime").innerText = onTimeRate.toFixed(1) + "%";
    document.getElementById("kpi-delay").innerText = avgDelay.toFixed(1);
    document.getElementById("kpi-cost").innerText = "$" + totalCost.toFixed(1) + "M";
    document.getElementById("kpi-risk").innerText = highRisk;
}

function updateMap(data) {
    const routeGroups = {};
    data.forEach(row => {
        if (!row.origin_lat || !row.destination_lat) return;
        const key = `${row.Origin_City}-${row.Destination_City}`;
        if (!routeGroups[key]) {
            routeGroups[key] = {
                fromName: row.Origin_City, toName: row.Destination_City,
                coords: [[row.origin_lon, row.origin_lat], [row.destination_lon, row.destination_lat]],
                shipments: 0, riskSum: 0
            };
        }
        routeGroups[key].shipments += 1;
        routeGroups[key].riskSum += (parseFloat(row.risk_score) || 0);
    });

    const optimizedRoutes = Object.values(routeGroups).map(r => {
        const avgRisk = r.riskSum / r.shipments;
        let color = "#00f0ff";
        if (avgRisk >= 0.66) color = "#ef4444";
        else if (avgRisk >= 0.33) color = "#f59e0b";
        return { fromName: r.fromName, toName: r.toName, coords: r.coords, lineStyle: { color: color, width: 1.5 }, risk: avgRisk.toFixed(2), shipments: r.shipments };
    });

    chart.setOption({
        series: [{ data: optimizedRoutes }]
    });
}

function updateDisruptionsChart(data) {
    if (!disruptionsChart) return;
    const total = data.length;
    if (total === 0) {
        disruptionsChart.setOption({ yAxis: { data: [] }, series: [{ data: [] }, { data: [] }] });
        return;
    }

    const counts = {};
    data.forEach(row => {
        const event = row.Disruption_Event || "None";
        counts[event] = (counts[event] || 0) + 1;
    });

    let sortedEvents = Object.entries(counts)
        .map(([name, count]) => ({
            name: name,
            value: Math.round((count / total) * 100)
        }))
        .sort((a, b) => b.value - a.value)
        .slice(0, 4);

    sortedEvents.reverse();

    const categories = sortedEvents.map(e => e.name);
    const values = sortedEvents.map(e => e.value);
    const goldPalette = ["#5c4a1f", "#8b6b25", "#ca8a04", "#d97706"];

    const seriesDataVisibles = values.map((val, idx) => ({
        value: val,
        itemStyle: { 
            color: goldPalette[idx % goldPalette.length],
            borderRadius: 5 
        }
    }));

    disruptionsChart.setOption({
        yAxis: { data: categories },
        series: [
            { data: seriesDataVisibles }, // Actualiza las barras de colores con sus %
            { data: values }              // Actualiza las barras invisibles que sostienen los nombres largos
        ]
    });
}

function updateGauges(data) {
    const total = data.length;
    const modesKeys = Object.keys(transportData);
    const mode1Name = modesKeys[0] || "Sea";
    const mode2Name = modesKeys[1] || "Air";

    const count1 = data.filter(r => r.Transportation_Mode === mode1Name).length;
    const count2 = data.filter(r => r.Transportation_Mode === mode2Name).length;

    const val1 = total > 0 ? (count1 / total) : 0;
    const val2 = total > 0 ? (count2 / total) : 0;

    renderGauge('gauge_t1', mode1Name, val1);
    renderGauge('gauge_t2', mode2Name, val2);
}

function updateRankings(data) {
    const container = document.getElementById("alerts-container");
    if (!container) return;

    if (data.length === 0) {
        container.innerHTML = '<div class="rank-item"><span style="color:var(--muted);">No active routes</span></div>';
        return;
    }

    const sorted = [...data].sort((a, b) => (b.risk_score || 0) - (a.risk_score || 0)).slice(0, 3);
    
    let html = "";
    sorted.forEach(item => {
        const routeStr = `${item.Origin_City || 'N/A'} ➔ ${item.Destination_City || 'N/A'}`;
        const level = item.risk_level || "Low";
        let color = "var(--success)";
        if (level === "High") color = "var(--danger)";
        else if (level === "Medium") color = "var(--warning)";

        html += `
            <div class="rank-item">
                <span style="max-width: 75%; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">${routeStr}</span>
                <span class="rank-value" style="color: ${color};">${level}</span>
            </div>
        `;
    });
    container.innerHTML = html;
}

function updateRiskEngine(data) {
    const nameEl = document.getElementById("high-route-name");
    const scoreEl = document.getElementById("high-risk-val");
    const delayEl = document.getElementById("high-delay-val");
    if (!nameEl || !scoreEl || !delayEl) return;

    if (data.length === 0) {
        nameEl.innerHTML = "N/A";
        scoreEl.innerText = "0.0";
        delayEl.innerText = "0 Days";
        return;
    }

    let highestItem = data[0];
    for (let i = 1; i < data.length; i++) {
        if ((data[i].risk_score || 0) > (highestItem.risk_score || 0)) {
            highestItem = data[i];
        }
    }

    const origin = highestItem.Origin_City || "N/A";
    const dest = highestItem.Destination_City || "N/A";
    
    nameEl.innerHTML = `${origin}<br>⬇<br>${dest}`;
    scoreEl.innerText = Number(highestItem.risk_score || 0).toFixed(1);
    delayEl.innerText = `+${Number(highestItem.Delay_Days || 0).toFixed(1)} Days`;
}
</script>

</body>
</html>"""

# ==================================================
# REEMPLAZOS GENERALES Y GUARDADO
# ==================================================
replacements = {
    "__ROUTES_JSON__": routes_json,
    "__RECORDS_JSON__": records_json,
    "__ROUTES_FILTER_JSON__": routes_filter_json,
    "__PRODUCTS_FILTER_JSON__": products_filter_json,
    "__TRANSPORT_FILTER_JSON__": transport_filter_json,
    "__RISK_FILTER_JSON__": risk_filter_json,
    "__YEARS_FILTER_JSON__": years_filter_json,
    "__TRANSPORT_GAUGES_JSON__": transport_gauges_json,
    "__KPI_SHIPMENTS__": f"{total_shipments:,}",
    "__KPI_ONTIME__": f"{on_time_rate:.1f}%",
    "__KPI_DELAY__": f"{avg_delay:.1f}",
    "__KPI_COST__": f"${total_cost_m:.1f}M",
    "__KPI_RISK__": str(high_risk_count),
    "__HIGH_ROUTE_NAME__": high_route,
    "__HIGH_RISK_VAL__": high_score,
    "__HIGH_DELAY_VAL__": high_delay
}

html_final = html_template
for placeholder, value in replacements.items():
    html_final = html_final.replace(placeholder, value)

with open("dashboard2.html", "w", encoding="utf-8") as f:
    f.write(html_final)

print("✅ Dashboard generado con éxito: 'dashboard2.html'")
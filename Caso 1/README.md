# Caso 1 - Análisis del Comportamiento de los Saldos Bancarios durante 2025

## Descripción

Este proyecto presenta un análisis exploratorio de datos (Exploratory Data Analysis - EDA) desarrollado para una institución bancaria ficticia con el objetivo de comprender el comportamiento de los saldos bancarios de sus clientes durante el año 2025.

El análisis fue realizado utilizando Python, MySQL y Bokeh, aplicando técnicas de limpieza, exploración y visualización de datos para obtener información que apoye la toma de decisiones comerciales.

---

# Contexto del negocio

Banco Capital GT desea comprender el comportamiento de los saldos de las cuentas de sus clientes durante el año 2025. La gerencia busca identificar patrones temporales, diferencias entre sucursales, segmentos de clientes y grupos de edad con el propósito de fortalecer la toma de decisiones comerciales y mejorar la gestión de su cartera de clientes.

---

# Objetivo general

Analizar el comportamiento de los saldos bancarios registrados durante el año 2025 mediante técnicas de análisis exploratorio de datos para identificar patrones, diferencias entre segmentos de clientes y oportunidades que contribuyan a la toma de decisiones.

---

# Preguntas de negocio

Durante el análisis se buscó responder las siguientes preguntas:

1. ¿Cómo evolucionó el saldo total administrado por el banco durante 2025?
2. ¿Qué sucursales concentran el mayor saldo de los clientes?
3. ¿Qué segmentos de clientes concentran los mayores saldos?
4. ¿Existe una relación entre el ingreso de los clientes y el saldo disponible en sus cuentas?
5. ¿Qué grupos de edad concentran el mayor saldo administrado por el banco durante 2025?

---

# Metodología

El proyecto fue desarrollado siguiendo un flujo de trabajo de análisis exploratorio de datos (EDA), compuesto por las siguientes etapas:

1. Comprensión del problema de negocio y definición de las preguntas de análisis.
2. Creación e importación de la base de datos en MySQL.
3. Limpieza, validación y preparación de los datos utilizando consultas SQL.
4. Exportación del conjunto de datos limpio a formato CSV.
5. Importación del archivo CSV en Python mediante Pandas.
6. Análisis exploratorio de los datos utilizando estadísticas descriptivas y agregaciones.
7. Construcción de visualizaciones interactivas con Bokeh para responder las preguntas de negocio.
8. Interpretación de los resultados obtenidos.
9. Elaboración de conclusiones y recomendaciones orientadas a la toma de decisiones.

---

# Tecnologías utilizadas

- Python
- Pandas
- NumPy
- MySQL
- Bokeh
- Jupyter Lab

---

# Archivos del proyecto

| Archivo | Descripción |
|----------|-------------|
| `caso1.ipynb` | Desarrollo completo del análisis. |
| `banco.csv` | Base de datos utilizada durante el análisis. |
| `banco.sql` | Script para crear e importar la base de datos en MySQL. |
| `requirements.txt` | Librerías necesarias para ejecutar el proyecto. |
| `img/` | Imágenes de las visualizaciones utilizadas en el proyecto. |

---

# Principales resultados

El análisis permitió identificar los siguientes hallazgos:

- El saldo total administrado presentó fluctuaciones durante 2025, sin evidenciar una tendencia sostenida de crecimiento o disminución.
- La distribución de los saldos entre las sucursales fue relativamente equilibrada, sin observarse una concentración significativa en una única agencia.
- Los segmentos de clientes mostraron una distribución homogénea del saldo administrado.
- No se identificó una relación lineal claramente definida entre el ingreso de los clientes y el saldo disponible en sus cuentas.
- La mayor concentración de saldos se registró en clientes con edades comprendidas entre 20 y 69 años.

---

# Recomendaciones

Como resultado del análisis se proponen las siguientes acciones:

- Incorporar variables adicionales que permitan explicar con mayor precisión el comportamiento de los saldos.
- Realizar análisis específicos por sucursal y segmento de clientes para identificar oportunidades comerciales.
- Diseñar estrategias diferenciadas según el perfil de los clientes y los grupos de edad.
- Complementar el análisis exploratorio mediante técnicas estadísticas y modelos predictivos.

---

# Cómo ejecutar el proyecto

1. Crear la base de datos utilizando el archivo `banco.sql`.
2. Importar la información desde el archivo `banco.csv`.
3. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

4. Abrir el archivo `caso1.ipynb` utilizando Jupyter Lab.

---

# Autor

**Javier Barillas**

Estudiante de Economía | Analista de Datos

Proyecto desarrollado con fines educativos y de construcción de portafolio profesional.
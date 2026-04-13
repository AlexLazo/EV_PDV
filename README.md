# 📊 Dashboard PDV Evaluados - Streamlit

Sistema profesional de análisis de PDVs evaluados con visualización de datos interactiva y comparativas de desempeño.

## 🎯 Características Principales

### 1. **🏆 Podio Digital**
- Ranking interactivo de usuarios por cantidad de PDVs registrados
- Medallas especiales para los tres primeros lugares (Oro, Plata, Bronce)
- Filtros para ver Top 5, Top 10, Top 15, etc.
- Estadísticas descriptivas (promedio, mediana, máximo)
- Tabla detallada con ranking

### 2. **📈 Dashboard General**
- Filtros multiselectivos por:
  - UEN (Unidad Estratégica de Negocio)
  - Mes
  - Calificación de riesgo
- Análisis de evaluaciones por:
  - UEN
  - Calificación (Sin Riesgo, Riesgo Moderado, Riesgo Alto)
  - Mes (Tendencia temporal)
  - Día de la semana

### 3. **⚠️ Análisis de Riesgos**
- Identificación de los riesgos más comunes
- Clasificación de riesgos por categoría
- Estadísticas de evaluaciones con y sin riesgo
- Tabla detallada de riesgos

### 4. **👤 Desempeño por Usuario**
- Selección individual de cada usuario
- Estadísticas personalizadas:
  - Total de evaluaciones
  - Evaluaciones con riesgo
  - Porcentaje de éxito sin riesgo
- Gráficos de distribución de calificaciones
- Análisis por UEN
- Tabla detallada de evaluaciones del usuario

### 5. **🗺️ Análisis Geográfico**
- Distribución por:
  - Departamento/Estado (Top 10)
  - País
  - Municipio (Top 15)
  - Zona/Barrio
- Visualización geográfica completa

## 📦 Requisitos

- Python 3.8+
- Las librerías necesarias están en `requirements.txt`

## 🚀 Instalación y Ejecución

### Opción 1: Usando Python (Recomendado)

```bash
# 1. Abre PowerShell o CMD en la carpeta del proyecto
cd c:\xampp\htdocs\EV_PDV

# 2. Ejecuta el script (PowerShell)
.\run_dashboard.ps1

# O si usas CMD
run_dashboard.bat
```

### Opción 2: Instalación Manual

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Ejecutar la aplicación
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador en: **http://localhost:8501**

## 📊 Estructura de Datos

El dashboard utiliza el archivo `PDV_Evaluados.xlsx` con las siguientes información:

- **Nombre usuario**: Identificación del evaluador
- **UEN**: Unidad Estratégica de Negocio
- **Calificación**: Nivel de riesgo identificado
- **Datos geográficos**: País, Departamento, Municipio, Zona
- **Temporales**: Mes, Día del mes, Día de la semana, Hora
- **Información del cliente**: Nombre, código, ubicación
- **Análisis de riesgos**: 20+ categorías de evaluación
- **ACIs creados**: Acciones Correctivas Inmediatas registradas

## 🎨 Características de Diseño

✅ Interfaz moderna y responsive
✅ Gráficos interactivos con Plotly
✅ Filtros en tiempo real
✅ Colores profesionales y accesibles
✅ Métricas destacadas
✅ Tablas ordenables
✅ Indicadores de desempeño

## 💡 Sugerencias de Uso

### Caso 1: Revisar Desempeño Individual
1. Ir a pestaña "👤 Desempeño por Usuario"
2. Seleccionar el usuario de interés
3. Analizar sus estadísticas y evaluaciones

### Caso 2: Identificar Riesgos Críticos
1. Ir a pestaña "⚠️ Análisis de Riesgos"
2. Revisar los top 10 riesgos
3. Tomar acciones correctivas

### Caso 3: Comparar Desempeño Regional
1. Ir a pestaña "📈 Dashboard General"
2. Filtrar por mes específico
3. Analizar comportamiento por UEN

### Caso 4: Análisis Geográfico
1. Ir a pestaña "🗺️ Análisis Geográfico"
2. Identificar municipios/departamentos con más evaluaciones
3. Priorizar recursos

## 🔄 Actualizar Datos

Para actualizar el dashboard con nuevos datos:

1. Actualiza el archivo `PDV_Evaluados.xlsx` con nuevos registros
2. Reinicia la aplicación Streamlit (Ctrl+C y ejecuta nuevamente)
3. La caché de datos se limpiará automáticamente

## 📝 Notas Importantes

- **Cache de datos**: Los datos se cargan en memoria para mejor rendimiento. Se actualizan al reiniciar.
- **Filtros inteligentes**: Los filtros se aplican en tiempo real sin necesidad de hacer clic en botones.
- **Responsive**: El dashboard se adapta a diferentes tamaños de pantalla.

## 🛠️ Solución de Problemas

### La aplicación no inicia

```bash
# 1. Verifica que Python esté instalado
python --version

# 2. Instala las dependencias manualmente
pip install -r requirements.txt

# 3. Ejecuta de nuevo
streamlit run app.py
```

### El archivo Excel no se encuentra

- Asegúrate de que `PDV_Evaluados.xlsx` esté en la misma carpeta que `app.py`
- Verifica que el archivo no esté abierto en Excel mientras se ejecuta el dashboard

### Gráficos no aparecen

- Actualiza Plotly: `pip install --upgrade plotly`
- Limpia el caché: Presiona Ctrl+C y reinicia

## 📧 Soporte

Para reportar problemas o sugerencias, contacta al equipo de desarrollo.

---

**Versión**: 1.0.0  
**Última actualización**: Abril 2026  
**Desarrollado con**: Streamlit, Pandas, Plotly

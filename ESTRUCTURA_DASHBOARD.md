# 📋 Estructura del Dashboard - Guía Visual

## 🏗️ Arquitectura de Datos

```
PDV_Evaluados.xlsx
    ├── 54 Evaluaciones
    ├── 14 Usuarios Únicos
    ├── 3 UENs
    ├── Múltiples Departamentos/Municipios
    └── 20+ Categorías de Riesgo
```

---

## 📊 PESTAÑA 1: 🏆 PODIO DIGITAL

### ¿Qué muestra?
Ranking de usuarios que evaluaron más PDVs

### Datos Principales
- **Gráfico de barras interactivo** con los Top N usuarios
- **Medallas especiales** para 🥇🥈🥉
- **Tabla con rankings** numerados
- **Estadísticas estadísticas**: Promedio, Mediana, Máximo

### Filtros
- Slider para seleccionar Top 5, 10, 15, etc.

### Insights Clave
```
🥇 #1: Carlos Marroquin Aguilar (14 evaluaciones)
   - Líder en cantidad de registros
   - Promedio: ~11 evaluaciones por usuario
```

---

## 📈 PESTAÑA 2: DASHBOARD GENERAL

### ¿Qué muestra?
Análisis integral con filtros multidimensionales

### Filtros en Tiempo Real
- **UEN** (Paracentral, Central, Oriental, etc.)
- **Mes** (Enero, Febrero, etc.)
- **Calificación** (Sin Riesgo, Riesgo Moderado, Riesgo Alto)

### Visualizaciones
1. **Gráfico de Barras**: PDVs por UEN
2. **Gráfico de Pastel**: Distribución de Calificaciones
3. **Gráfico de Líneas**: Tendencia por Mes
4. **Gráfico de Barras**: Evaluaciones por Día de la Semana

### Casos de Uso
- Ver cuál UEN tiene más evaluaciones
- Identificar tendencias mensuales
- Saber en qué día de la semana hay más actividad

---

## ⚠️ PESTAÑA 3: ANÁLISIS DE RIESGOS

### ¿Qué muestra?
Identificación sistemática de riesgos

### Tipos de Riesgos Analizados
```
1. Ubicación del PDV
2. Espacio de estacionamiento
3. Maniobras de reversa
4. Descarga del producto
5. Condiciones del suelo
6. Inclinación
7. Condiciones de escaleras
8. Iluminación
9. Desniveles
10. Limpieza y orden (5S)
... y más
```

### Estadísticas
- **Total de Riesgos Identificados**: Suma de todos los sí
- **Evaluaciones con Riesgo**: Cuántas NO son "Sin Riesgo"
- **% Evaluaciones con Riesgo**: Porcentaje del total

### Top 15 Riesgos
Gráfico horizontal mostrando los 15 riesgos más comunes

---

## 👤 PESTAÑA 4: DESEMPEÑO POR USUARIO

### ¿Qué muestra?
Análisis personalizado de cada evaluador

### Selector
Dropdown para elegir cualquier usuario

### Métricas Personales
- Total de Evaluaciones del Usuario
- Cuántas con Riesgo
- Cuántas Sin Riesgo
- % de Éxito (Sin Riesgo)

### Visualizaciones
1. **Gráfico de Pastel**: Calificaciones del usuario
2. **Gráfico de Barras**: Evaluaciones por UEN

### Tabla de Detalle
Listado completo de todas las evaluaciones del usuario:
- Día del mes
- Mes
- Cliente
- UEN
- Calificación
- ACIs creados

### Casos de Uso
- Evaluar desempeño individual
- Ver patrón de riesgos identificados
- Comparar con promedio de otros usuarios

---

## 🗺️ PESTAÑA 5: ANÁLISIS GEOGRÁFICO

### ¿Qué muestra?
Distribución espacial de evaluaciones

### Análisis Geográficos
1. **Top 10 Departamentos/Estados**
   - Gráfico horizontal con más evaluaciones

2. **Distribución por País**
   - Gráfico de pastel

3. **Top 15 Municipios**
   - Gráfico horizontal detallado

4. **Estadísticas Geográficas**
   - Cantidad de países
   - Cantidad de departamentos
   - Cantidad de municipios
   - Cantidad de zonas/barrios únicos

### Casos de Uso
- Identificar municipios con más riesgo
- Planificar recursos en áreas específicas
- Ver cobertura geográfica
- Priorizar zonas de intervención

---

## 🎨 ELEMENTOS COMUNES

### En Todas las Pestañas

✅ **Filtros inteligentes**: Se aplican en tiempo real
✅ **Gráficos interactivos**: Hover para ver detalles
✅ **Tablas ordenables**: Click en columnas para ordenar
✅ **Responsive design**: Funciona en desktop y tablet
✅ **Colores profesionales**: Paleta corporativa

### Interactividad

- **Zoom en gráficos**: Arrastra para zoom
- **Seleccionar serie**: Click en leyenda para mostrar/ocultar
- **Descargar**: Botón de cámara en cada gráfico
- **Hover**: Muestra detalles al pasar el mouse

---

## 📊 FLUJO DE ANÁLISIS RECOMENDADO

### Flujo 1: Evaluación de Desempeño
```
Dashboard General 
    ↓
Podio Digital (ver top performers)
    ↓
Desempeño por Usuario (profundizar)
    ↓
Tomar decisiones
```

### Flujo 2: Identificación de Riesgos
```
Análisis de Riesgos (ver top riesgos)
    ↓
Desempeño por Usuario (ver quién detecta qué)
    ↓
Análisis Geográfico (dónde está el riesgo)
    ↓
Crear plan de acción
```

### Flujo 3: Expansión Geográfica
```
Análisis Geográfico (identificar áreas)
    ↓
Dashboard General (filtrar por zona)
    ↓
Podio Digital (ver recursos disponibles)
    ↓
Asignar evaluadores
```

---

## 🎯 KPIs MONITOREADOS

| KPI | Pestaña | Fórmula |
|-----|---------|---------|
| Productividad | Podio Digital | Conteo por usuario |
| Calidad | Dashboard General | % Sin Riesgo |
| Cobertura UEN | Dashboard General | Evaluaciones / UEN |
| Riesgo Crítico | Análisis Riesgos | Suma de riesgos |
| Eficiencia Geográfica | Análisis Geográfico | Evaluaciones / Zona |
| Tendencia | Dashboard General | Mes a Mes |

---

## 💾 DATOS ACTUALIZADOS

El dashboard utiliza **caché inteligente**:
- Los datos se cargan una vez en memoria
- Muy rápido para interactuar
- Para actualizar: reinicia la aplicación

---

## 🔑 RESUMEN

**Este dashboard proporciona una vista 360° de:**
- ✅ Quién está haciendo el trabajo (Podio)
- ✅ Cómo está distribuido (Dashboard General)
- ✅ Qué riesgos se encuentran (Análisis Riesgos)
- ✅ Cómo rinde cada persona (Desempeño)
- ✅ Dónde se concentra el trabajo (Geografía)

**Resultado:** Toma de decisiones basada en datos reales y consistentes.

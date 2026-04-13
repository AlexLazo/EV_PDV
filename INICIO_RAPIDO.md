# 🚀 INICIO RÁPIDO - Dashboard PDV Evaluados

## En 1 minuto: Ejecuta tu Dashboard

### Opción 1: PowerShell (Recomendado) ⭐

```powershell
cd c:\xampp\htdocs\EV_PDV
.\run_dashboard.ps1
```

### Opción 2: CMD (Windows)

```cmd
cd c:\xampp\htdocs\EV_PDV
run_dashboard.bat
```

### Opción 3: Manual

```bash
cd c:\xampp\htdocs\EV_PDV
pip install -r requirements.txt
streamlit run app.py
```

---

## ✅ Lo que verás

Después de ejecutar, tu navegador abrirá **http://localhost:8501** con:

### 📊 5 Pestañas Principal

| Pestaña | Función |
|---------|---------|
| 🏆 **Podio Digital** | Ranking de usuarios - ¿Quién evaluó más PDVs? |
| 📈 **Dashboard General** | Análisis con filtros (UEN, Mes, Calificación) |
| ⚠️ **Análisis de Riesgos** | Top riesgos identificados en evaluaciones |
| 👤 **Desempeño por Usuario** | Estadísticas individual de cada usuario |
| 🗺️ **Análisis Geográfico** | Distribución por país, departamento, municipio |

---

## 🎯 Top 3 Usuarios (Podio)

```
🥇 1er lugar: Carlos Marroquin Aguilar       (14 evaluaciones)
🥈 2do lugar: FRANKLIN JAVIER RODRIGUEZ      (11 evaluaciones)
🥉 3er lugar: Jose Ernesto Garcia Rivas      (10 evaluaciones)
```

---

## ❓ Preguntas Frecuentes

### ¿Cómo actualizo con nuevos datos?

1. Actualiza el archivo `PDV_Evaluados.xlsx`
2. Reinicia la aplicación (Ctrl+C y ejecuta nuevamente)

### ¿Qué filtros tiene?

- **UEN** (Unidad de Negocio)
- **Mes** (Temporal)
- **Calificación** (Sin Riesgo, Riesgo Moderado, Riesgo Alto)

### ¿Puedo exportar datos?

Las tablas son interactivas, puedes:
- Ordenar columnas
- Copiar datos
- Ver en pantalla completa

### ¿Dónde veo errores?

Si hay problemas, revisa la terminal donde ejecutaste el script.

---

## 📝 Requisitos

✅ Python 3.8+ instalado  
✅ Conexión a internet (primera ejecución)  
✅ El archivo `PDV_Evaluados.xlsx` en la carpeta  

---

## 🆘 Solución Rápida

**Si no funciona:**

```bash
# Limpia e instala de nuevo
pip install --upgrade streamlit pandas plotly openpyxl
streamlit run app.py
```

---

**¡Listo! Ahora tienes un dashboard profesional con análisis completo de PDVs.**

Para más información, lee: `README.md`

@echo off
REM Script para instalar dependencias y ejecutar el dashboard
REM ======================================

echo.
echo ========================================
echo Dashboard PDV Evaluados - Streamlit
echo ========================================
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no está instalado o no está en PATH
    pause
    exit /b 1
)

echo [1/3] Instalando dependencias...
pip install -r requirements.txt

if errorlevel 1 (
    echo ERROR: Falló la instalación de dependencias
    pause
    exit /b 1
)

echo.
echo [2/3] Iniciando aplicación...
echo.
echo La aplicación se abrirá en tu navegador en http://localhost:8501
echo Presiona Ctrl+C para detener el servidor
echo.

timeout /t 2

REM Ejecutar la aplicación
streamlit run app.py

pause

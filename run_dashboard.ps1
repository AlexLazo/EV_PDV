# Script para instalar dependencias y ejecutar el dashboard
# ======================================

Write-Host ""
Write-Host "======================================" -ForegroundColor Cyan
Write-Host "Dashboard PDV Evaluados - Streamlit" -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan
Write-Host ""

# Verificar si Python está instalado
try {
    $pythonVersion = python --version 2>&1
    Write-Host "[✓] Python encontrado: $pythonVersion" -ForegroundColor Green
}
catch {
    Write-Host "[✗] ERROR: Python no está instalado o no está en PATH" -ForegroundColor Red
    Write-Host "Por favor, instala Python desde https://www.python.org" -ForegroundColor Yellow
    Read-Host "Presiona Enter para salir"
    exit 1
}

Write-Host ""
Write-Host "[1/3] Instalando dependencias..." -ForegroundColor Yellow
$requirementsPath = Split-Path -Parent $MyInvocation.MyCommand.Definition
pip install -r "$requirementsPath\requirements.txt"

if ($LASTEXITCODE -ne 0) {
    Write-Host "[✗] ERROR: Falló la instalación de dependencias" -ForegroundColor Red
    Read-Host "Presiona Enter para salir"
    exit 1
}

Write-Host ""
Write-Host "[2/3] Iniciando aplicación..." -ForegroundColor Yellow
Write-Host ""
Write-Host "La aplicación se abrirá en tu navegador en http://localhost:8501" -ForegroundColor Green
Write-Host "Presiona Ctrl+C para detener el servidor" -ForegroundColor Green
Write-Host ""

Start-Sleep -Seconds 2

# Ejecutar la aplicación
streamlit run "$requirementsPath\app.py"

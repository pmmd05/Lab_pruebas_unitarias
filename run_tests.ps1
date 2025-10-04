# Script para ejecutar todas las pruebas con salida visible
# Uso: .\run_tests.ps1

Write-Host "=== Ejecutando todas las pruebas con salida visible ===" -ForegroundColor Green
Write-Host ""

# Cambiar al directorio del proyecto
Set-Location $PSScriptRoot

# Ejecutar todas las pruebas con -s para mostrar prints y -v para más detalles
Write-Host "Ejecutando: pytest tests/ -s -v" -ForegroundColor Yellow
pytest tests/ -s -v

Write-Host ""
Write-Host "=== Pruebas completadas ===" -ForegroundColor Green
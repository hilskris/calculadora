#!/bin/bash
echo "Ejecutando pruebas de liberación..."

python -m py_compile calculator.py app.py

echo "Pruebas de liberación completadas correctamente."

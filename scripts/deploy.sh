#!/bin/bash
echo "Generando despliegue..."

mkdir -p release
cp calculator.py release/
cp app.py release/
cp requirements.txt release/

echo "Despliegue generado en la carpeta release/"
ls -la release
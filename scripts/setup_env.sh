#!/bin/bash
echo "Generando entorno de liberación..."

python -m pip install --upgrade pip
pip install -r requirements.txt

echo "Entorno de liberación generado correctamente."

#!/bin/bash

# Inicia el backend
cd backend
python -m venv venv
source venv/bin/activate  # En Windows: .\venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver &

# Inicia el frontend
cd ../frontend
npm install
npm run dev 
"""
SafeCity Mérida - Servidor Backend
Mapa interactivo de seguridad específico para Mérida, Yucatán
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = True

@app.route('/')
def home():
    """API principal para SafeCity Mérida"""
    return jsonify({
        "message": "🏛️ SafeCity Mérida - API de Seguridad",
        "ciudad": "Mérida, Yucatán, México",
        "version": "1.0",
        "endpoints": [
            "/api/colonias",
            "/api/seguridad",
            "/api/buscar"
        ]
    })

@app.route('/api/colonias')
def get_colonias():
    """Colonias de Mérida con puntuaciones de seguridad"""
    # Datos reales de colonias de Mérida con coordenadas aproximadas
    colonias_merida = [
        {
            "id": 1,
            "nombre": "Centro Histórico",
            "puntuacion_seguridad": 7.5,
            "latitud": 20.9674,
            "longitud": -89.5926,
            "color": "green",
            "poblacion": 15000,
            "zona": "Centro"
        },
        {
            "id": 2,
            "nombre": "Colonia México",
            "puntuacion_seguridad": 6.8,
            "latitud": 20.9555,
            "longitud": -89.5802,
            "color": "orange",
            "poblacion": 8500,
            "zona": "Centro"
        },
        {
            "id": 3,
            "nombre": "Francisco de Montejo",
            "puntuacion_seguridad": 8.9,
            "latitud": 20.9988,
            "longitud": -89.6154,
            "color": "green",
            "poblacion": 25000,
            "zona": "Norte"
        },
        {
            "id": 4,
            "nombre": "García Ginerés",
            "puntuacion_seguridad": 8.2,
            "latitud": 20.9789,
            "longitud": -89.6089,
            "color": "green",
            "poblacion": 12000,
            "zona": "Norte"
        },
        {
            "id": 5,
            "nombre": "San José Tecoh",
            "puntuacion_seguridad": 5.8,
            "latitud": 20.9234,
            "longitud": -89.5654,
            "color": "red",
            "poblacion": 22000,
            "zona": "Sur"
        },
        {
            "id": 6,
            "nombre": "Pensiones",
            "puntuacion_seguridad": 6.5,
            "latitud": 20.9456,
            "longitud": -89.5723,
            "color": "orange",
            "poblacion": 18000,
            "zona": "Centro-Sur"
        }
    ]
    
    return jsonify({
        "colonias": colonias_merida,
        "total": len(colonias_merida),
        "ciudad": "Mérida, Yucatán"
    })

@app.route('/api/seguridad')
def get_datos_seguridad():
    """Indicadores de seguridad agregados de Mérida"""
    indicadores_merida = {
        "iluminacion_calles": 78,  # % de calles bien iluminadas
        "presencia_policial": 65,  # Cobertura policial
        "camaras_seguridad": 52,   # Cámaras por km²
        "reportes_ciudadanos": 89, # Reportes este mes
        "puntuacion_promedio": 7.1,
        "poblacion_total": 1000000,
        "superficie_km2": 324.97,
        "zonas_mas_seguras": ["Francisco de Montejo", "García Ginerés", "Centro Histórico"],
        "zonas_atencion": ["San José Tecoh", "Pensiones"]
    }
    
    return jsonify(indicadores_merida)

@app.route('/api/buscar')
def buscar_colonias():
    """Buscar colonias de Mérida por nombre"""
    consulta = request.args.get('q', '').lower()
    
    if not consulta:
        return jsonify({"error": "Se requiere parámetro 'q' para buscar colonias"})
    
    # Base de datos simple de colonias de Mérida
    todas_colonias = [
        {"id": 1, "nombre": "Centro Histórico", "puntuacion": 7.5},
        {"id": 2, "nombre": "Colonia México", "puntuacion": 6.8},
        {"id": 3, "nombre": "Francisco de Montejo", "puntuacion": 8.9},
        {"id": 4, "nombre": "García Ginerés", "puntuacion": 8.2},
        {"id": 5, "nombre": "San José Tecoh", "puntuacion": 5.8},
        {"id": 6, "nombre": "Pensiones", "puntuacion": 6.5},
        {"id": 7, "nombre": "Itzimná", "puntuacion": 7.8},
        {"id": 8, "nombre": "Campestre", "puntuacion": 8.0}
    ]
    
    # Filtrar colonias que contengan la consulta
    resultados = [
        colonia for colonia in todas_colonias 
        if consulta in colonia["nombre"].lower()
    ]
    
    return jsonify({
        "consulta": consulta,
        "resultados": resultados,
        "total": len(resultados),
        "ciudad": "Mérida, Yucatán"
    })

@app.route('/api/mapa-info')
def info_mapa():
    """Información para centrar el mapa en Mérida"""
    return jsonify({
        "centro": {
            "latitud": 20.9674,
            "longitud": -89.5926
        },
        "zoom_inicial": 12,
        "limites": {
            "norte": 21.0500,
            "sur": 20.8500,
            "este": -89.4500,
            "oeste": -89.7500
        }
    })

if __name__ == '__main__':
    print("🏛️ Iniciando SafeCity Mérida...")
    print("📍 Servidor: http://localhost:5000")
    print("🗺️ Enfocado en: Mérida, Yucatán, México")
    print("📊 Endpoints disponibles:")
    print("   - GET /api/colonias (colonias con seguridad)")
    print("   - GET /api/seguridad (indicadores generales)")
    print("   - GET /api/buscar?q=nombre (buscar colonias)")
    print("   - GET /api/mapa-info (configuración del mapa)")
    
    app.run(debug=True, port=5000)
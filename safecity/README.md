# SafeCity - Mapa Interactivo de Seguridad para Mérida, Yucatán

Proyecto estudiantil para crear una aplicación web que muestre áreas seguras/inseguras de Mérida usando datos públicos.

## Estructura del Proyecto

```
safecity/
├── backend/                    # Servidor Python
│   ├── app/
│   │   ├── api/               # Rutas y endpoints de la API
│   │   ├── models/            # Modelos de datos
│   │   ├── services/          # Lógica de negocio
│   │   └── data_processing/   # Procesamiento de datos
│   ├── data/
│   │   ├── raw/              # Datos sin procesar
│   │   └── processed/        # Datos limpios
│   └── tests/                # Pruebas del backend
├── frontend/                  # Página web
│   ├── src/
│   │   ├── components/       # Componentes reutilizables
│   │   ├── pages/           # Páginas principales
│   │   └── services/        # Comunicación con API
│   └── public/              # Archivos estáticos
└── docs/                    # Documentación
```

## Tecnologías

**Backend:**
- Flask/FastAPI (servidor web Python)
- Pandas (análisis de datos)
- SQLite (base de datos simple)

**Frontend:**
- HTML, CSS, JavaScript
- Leaflet.js (mapas interactivos)
- Chart.js (gráficas)

**Datos:**
- INEGI (datos gubernamentales)
- datos.gob.mx (portal de datos abiertos)

## Funcionalidades Planeadas

1. 🗺️ Mapa interactivo con colores por seguridad
2. 📊 Dashboard con gráficas
3. 🔍 Búsqueda de colonias
4. 📱 Diseño responsive

## Para Comenzar

```bash
# Instalar dependencias de Python
pip install flask pandas requests

# Ejecutar el servidor
cd backend
python app.py
```

¡Vamos a construir esto paso a paso! 🚀
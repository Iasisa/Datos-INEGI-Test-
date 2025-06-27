# 🚀 Cómo usar SafeCity Mérida

## Pasos para probar la aplicación

### 1. Instalar dependencias del backend
```bash
cd safecity/backend
pip install -r requirements.txt
```

### 2. Ejecutar el servidor backend
```bash
python app.py
```

Deberías ver:
```
🏛️ Iniciando SafeCity Mérida...
📍 Servidor: http://localhost:5000
🗺️ Enfocado en: Mérida, Yucatán, México
```

### 3. Abrir el frontend
Abre el archivo `safecity/frontend/index.html` en tu navegador web.

### 4. ¡Prueba las funciones!

**Mapa:**
- Verás un mapa de Mérida con círculos de colores
- Verde = Seguro, Naranja = Medio, Rojo = Inseguro
- Haz clic en los círculos para ver información

**Búsqueda:**
- Busca colonias como "Centro", "Francisco", "García"
- Los resultados aparecerán en una ventana emergente

**Estadísticas:**
- Panel lateral con datos de seguridad de Mérida

## Lo que ya funciona ✅

- **Backend**: API REST con datos de colonias de Mérida
- **Frontend**: Mapa interactivo con Leaflet.js  
- **Conexión**: Frontend se comunica con backend via AJAX
- **Búsqueda**: Funcionalidad de búsqueda de colonias
- **Visualización**: Marcadores de colores por nivel de seguridad

## Endpoints de la API

Puedes probar la API directamente en el navegador:

- http://localhost:5000/ (información general)
- http://localhost:5000/api/colonias (todas las colonias)
- http://localhost:5000/api/seguridad (estadísticas)
- http://localhost:5000/api/buscar?q=centro (buscar)

## Próximos pasos posibles 🚧

1. **Más colonias**: Agregar más datos estáticos de colonias reales
2. **Mejor diseño**: Mejorar la UI/UX del frontend
3. **Gráficas**: Agregar Chart.js para visualizaciones
4. **Base de datos**: Migrar de datos estáticos a SQLite
5. **Datos reales**: Conectar con datasets INEGI reales

## Estructura de archivos creados

```
safecity/
├── backend/
│   ├── app.py              # Servidor Flask
│   └── requirements.txt    # Dependencias Python
├── frontend/
│   ├── index.html         # Página principal
│   └── src/
│       ├── app.js         # JavaScript principal
│       └── style.css      # Estilos CSS
└── COMO_USAR.md           # Este archivo
```

¡El proyecto base está listo para usar! 🎉
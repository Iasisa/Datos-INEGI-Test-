// SafeCity Mérida - JavaScript Principal
// Conecta el frontend con el backend Flask

// Configuración
const API_BASE = 'http://localhost:5000/api';

// Variables globales
let map;
let colonias = [];

// Inicializar la aplicación
document.addEventListener('DOMContentLoaded', function() {
    console.log('🏛️ Iniciando SafeCity Mérida...');
    initMap();
    loadColonias();
    loadStats();
    setupEventListeners();
});

// Inicializar el mapa
function initMap() {
    // Crear mapa centrado en Mérida
    map = L.map('map').setView([20.9674, -89.5926], 12);
    
    // Agregar capa de OpenStreetMap
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);
    
    console.log('🗺️ Mapa inicializado');
}

// Cargar colonias desde el backend
async function loadColonias() {
    try {
        const response = await fetch(`${API_BASE}/colonias`);
        const data = await response.json();
        
        colonias = data.colonias;
        console.log(`📍 Cargadas ${colonias.length} colonias`);
        
        // Agregar marcadores al mapa
        addMarkersToMap(colonias);
        
    } catch (error) {
        console.error('❌ Error cargando colonias:', error);
        showError('No se pudieron cargar las colonias');
    }
}

// Agregar marcadores al mapa
function addMarkersToMap(colonias) {
    colonias.forEach(colonia => {
        // Determinar color del marcador
        let color = 'gray';
        if (colonia.puntuacion_seguridad >= 8.0) color = 'green';
        else if (colonia.puntuacion_seguridad >= 6.0) color = 'orange';
        else color = 'red';
        
        // Crear marcador
        const marker = L.circleMarker([colonia.latitud, colonia.longitud], {
            color: color,
            fillColor: color,
            fillOpacity: 0.7,
            radius: 8
        });
        
        // Popup con información
        const popupContent = `
            <div>
                <h4>${colonia.nombre}</h4>
                <p><strong>Puntuación:</strong> ${colonia.puntuacion_seguridad}/10</p>
                <p><strong>Zona:</strong> ${colonia.zona}</p>
                <p><strong>Población:</strong> ${colonia.poblacion.toLocaleString()}</p>
            </div>
        `;
        
        marker.bindPopup(popupContent);
        marker.addTo(map);
    });
}

// Cargar estadísticas
async function loadStats() {
    try {
        const response = await fetch(`${API_BASE}/seguridad`);
        const data = await response.json();
        
        // Actualizar elementos del DOM
        document.getElementById('iluminacion').textContent = `${data.iluminacion_calles}%`;
        document.getElementById('policia').textContent = `${data.presencia_policial}%`;
        document.getElementById('camaras').textContent = `${data.camaras_seguridad}%`;
        document.getElementById('promedio').textContent = `${data.puntuacion_promedio}/10`;
        
        console.log('📊 Estadísticas cargadas');
        
    } catch (error) {
        console.error('❌ Error cargando estadísticas:', error);
    }
}

// Configurar eventos
function setupEventListeners() {
    // Búsqueda
    document.getElementById('search-btn').addEventListener('click', buscarColonias);
    document.getElementById('search-input').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            buscarColonias();
        }
    });
}

// Buscar colonias
async function buscarColonias() {
    const query = document.getElementById('search-input').value.trim();
    
    if (!query) {
        showError('Por favor ingresa el nombre de una colonia');
        return;
    }
    
    try {
        const response = await fetch(`${API_BASE}/buscar?q=${encodeURIComponent(query)}`);
        const data = await response.json();
        
        console.log(`🔍 Búsqueda: "${query}" - ${data.total} resultados`);
        
        if (data.total > 0) {
            showSearchResults(data.resultados);
        } else {
            showError(`No se encontraron colonias con "${query}"`);
        }
        
    } catch (error) {
        console.error('❌ Error en búsqueda:', error);
        showError('Error al buscar colonias');
    }
}

// Mostrar resultados de búsqueda
function showSearchResults(resultados) {
    const resultsDiv = document.getElementById('search-results');
    
    let html = `
        <button class="close-btn" onclick="hideSearchResults()">×</button>
        <h3>Resultados de búsqueda</h3>
    `;
    
    resultados.forEach(resultado => {
        html += `
            <div class="result-item" onclick="goToColonia(${resultado.id})">
                <strong>${resultado.nombre}</strong>
                <br>
                <small>Puntuación: ${resultado.puntuacion}/10</small>
            </div>
        `;
    });
    
    resultsDiv.innerHTML = html;
    resultsDiv.classList.add('show');
}

// Ir a una colonia específica
function goToColonia(id) {
    const colonia = colonias.find(c => c.id === id);
    
    if (colonia) {
        // Centrar mapa en la colonia
        map.flyTo([colonia.latitud, colonia.longitud], 15);
        
        // Cerrar resultados
        hideSearchResults();
        
        console.log(`📍 Navegando a: ${colonia.nombre}`);
    }
}

// Ocultar resultados de búsqueda
function hideSearchResults() {
    document.getElementById('search-results').classList.remove('show');
}

// Mostrar errores
function showError(message) {
    alert(message); // Por ahora usamos alert, después podemos hacer algo más elegante
}

// Función de utilidad para logging
console.log('🚀 SafeCity Mérida JS cargado');
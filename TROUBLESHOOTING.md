# Troubleshooting — Proyecto BREATH

## ⚠️ Warning: consumo excesivo de Firebase Realtime Database

### Problema
La pantalla de puntuación (`pantalla_normalizada.html`) descargaba **toda** la base de datos cada 3 segundos mediante un `setInterval` + `db.ref('/').once('value')`. Esto incluía el nodo `validCodes` (cientos de entradas) que no era necesario para mostrar los tanques.

Con la pantalla abierta en el proyector durante las clases, el consumo llegó a **~4 GB/día**, agotando la cuota gratuita de Firebase (10 GB/mes) en pocos días.

### Causa
```javascript
// ❌ MAL — descarga toda la base de datos cada 3 segundos
const snapshot = await db.ref('/').once('value');
setInterval(updateDisplay, 3000);
```

### Solución aplicada (abril 2026)
Se sustituyó por dos listeners en tiempo real sobre los únicos nodos necesarios:

```javascript
// ✅ BIEN — solo descarga 'courses' y 'usedCodes', y solo cuando cambian
db.ref('courses').on('value', snapshot => { ... });
db.ref('usedCodes').on('value', snapshot => { ... });
```

El consumo pasó de **~4 GB/día** a **~65 MB/día**.

### Regla general
> Nunca usar `db.ref('/')` para leer datos. Siempre apuntar al nodo más específico que se necesite. Usar `.on('value')` en lugar de `setInterval` + `.once('value')` para actualizaciones en tiempo real.

---

## ⚠️ Warning: versiones antiguas de la pantalla de puntuación

El repositorio puede contener versiones antiguas de `pantalla_normalizada.html` con el bug descrito arriba. **No usar ninguna versión anterior a abril 2026.** La versión correcta es `pantalla_normalizada-2.html` (o la que la sustituya).

Si se detecta un consumo anómalo en Firebase, revisar primero la pestaña **Uso** en la consola de Firebase → Realtime Database y comprobar si las descargas diarias superan los 100 MB.

# SOLUCIÓN: No Puedo Subir JSON a Firebase

## 🔥 Problema Común

Firebase Realtime Database no te deja importar el JSON manualmente desde la consola.

---

## ✅ SOLUCIÓN 1: Configurar Reglas de Seguridad (Más Rápido)

### Paso 1: Ir a Firebase Console
1. Abre https://console.firebase.google.com/
2. Selecciona tu proyecto: **breath-8f51d**
3. En el menú lateral: **Realtime Database**

### Paso 2: Cambiar las Reglas
1. Clic en la pestaña **"Reglas"** (Rules)
2. Verás algo como:

```json
{
  "rules": {
    ".read": false,
    ".write": false
  }
}
```

3. **Cámbialo a esto:**

```json
{
  "rules": {
    ".read": true,
    ".write": true
  }
}
```

4. Clic en **"Publicar"** (Publish)

### Paso 3: Importar el JSON Manualmente
1. Ve a la pestaña **"Datos"** (Data)
2. Clic en los **3 puntos** (⋮) en la raíz
3. **"Importar JSON"**
4. Selecciona tu archivo `codigos_firebase_XXXXXX.json`
5. **"Importar"**

✅ ¡Debería funcionar!

---

## ✅ SOLUCIÓN 2: Usar Script Python (Más Automático)

Si la solución 1 no funciona o prefieres automatizar:

### Paso 1: Obtener Credenciales de Firebase

1. **Firebase Console** → Tu proyecto
2. **⚙️ Configuración del proyecto** (icono engranaje arriba a la izquierda)
3. **Cuentas de servicio** (Service accounts)
4. Clic en **"Generar nueva clave privada"**
5. Descargar el archivo JSON
6. **Renombrarlo a:** `firebase-credentials.json`
7. **Guardarlo** en la misma carpeta que `subir_firebase.py`

### Paso 2: Instalar Librería

```bash
pip install firebase-admin
```

### Paso 3: Ejecutar Script

```bash
python subir_firebase.py
```

El script:
- ✅ Se conecta automáticamente a Firebase
- ✅ Sube todos los códigos
- ✅ Inicializa los puntos de las clases en 0
- ✅ Crea la lista de códigos usados vacía
- ✅ Verifica que todo se subió correctamente

---

## ✅ SOLUCIÓN 3: Importar por Partes (Si el JSON es muy grande)

A veces Firebase rechaza archivos JSON muy grandes (1,350 códigos es bastante).

### Opción A: Dividir el JSON

Crea versiones más pequeñas del JSON:

**Archivo 1: `codigos_clases_ABC.json`**
```json
{
  "validCodes": {
    // Solo códigos de clases A, B, C
  }
}
```

**Archivo 2: `codigos_clases_DEF.json`**
```json
{
  "validCodes": {
    // Solo códigos de clases D, E, F
  }
}
```

Importa cada uno por separado.

### Opción B: Usar la API REST

Puedes subir usando cURL desde terminal:

```bash
curl -X PUT \
  -d '{
    "validCodes": { ... },
    "courses": {
      "3º_ESO_A": 0,
      "3º_ESO_B": 0,
      "3º_ESO_C": 0,
      "3º_ESO_D": 0,
      "3º_ESO_E": 0,
      "3º_ESO_F": 0
    },
    "usedCodes": []
  }' \
  'https://breath-8f51d-default-rtdb.firebaseio.com/.json'
```

---

## 🚨 IMPORTANTE: Seguridad

### ⚠️ Para Testing (Desarrollo)
```json
{
  "rules": {
    ".read": true,
    ".write": true
  }
}
```
**USAR SOLO TEMPORALMENTE**

### ✅ Para Producción (Cuando esté listo)
```json
{
  "rules": {
    "validCodes": {
      ".read": true,
      "$code": {
        ".write": "!data.child('usado').val()"
      }
    },
    "courses": {
      ".read": true,
      ".write": true
    },
    "usedCodes": {
      ".read": true,
      ".write": true
    }
  }
}
```

Esto permite:
- ✅ Leer códigos
- ✅ Escribir solo si el código NO ha sido usado
- ✅ Actualizar puntos de clases
- ❌ Impide modificar códigos ya usados

---

## 🔍 Verificar que Funcionó

### En Firebase Console:
1. Ve a **Realtime Database** → **Datos**
2. Deberías ver:
   ```
   breath-8f51d-default-rtdb
   ├── validCodes
   │   ├── ABC12345
   │   ├── XYZ67890
   │   └── ... (1,350 códigos)
   ├── courses
   │   ├── 3º_ESO_A: 0
   │   ├── 3º_ESO_B: 0
   │   └── ...
   └── usedCodes: []
   ```

### En tu Aplicación:
1. Abre `pantalla_normalizada.html` en un navegador
2. Deberías ver las 6 clases con 0 puntos
3. Si ves "Error de conexión" → problema de reglas

---

## ❓ Troubleshooting Adicional

### Problema: "Permission Denied"
**Causa:** Reglas muy restrictivas
**Solución:** Usar las reglas de testing mostradas arriba

### Problema: "Invalid Data"
**Causa:** Formato JSON incorrecto
**Solución:** Usa el script Python que genera el JSON correcto

### Problema: "Network Error"
**Causa:** URL de Firebase incorrecta
**Solución:** Verifica en `pantalla_normalizada.html` línea 544:
```javascript
databaseURL: "https://breath-8f51d-default-rtdb.firebaseio.com"
```

### Problema: "Quota Exceeded"
**Causa:** Plan gratuito de Firebase tiene límites
**Solución:** 
- Revisa tu uso en Firebase Console
- Considera upgrade si es necesario
- O reduce la frecuencia de actualización en pantalla.html (línea 659: `setInterval(updateDisplay, 3000)` → cambiar 3000 a 5000 o más)

---

## 📞 Si Nada Funciona

1. **Comparte el error exacto** que ves (screenshot)
2. **Verifica tu plan de Firebase** (Spark/Blaze)
3. **Revisa la consola del navegador** (F12) para ver errores JavaScript
4. **Prueba con un JSON más pequeño** primero (10 códigos de prueba)

---

## 🎯 Resumen Rápido

**Método más rápido:**
1. Firebase Console → Realtime Database → Reglas
2. Poner `.read: true, .write: true`
3. Publicar
4. Importar JSON desde la pestaña Datos

**Método más robusto:**
1. Descargar credenciales de Firebase
2. `pip install firebase-admin`
3. `python subir_firebase.py`

¡Con alguno de estos métodos debería funcionar! 🚀

# 🔄 GUÍA: Resetear Códigos en Firebase

## 📋 Dos Métodos de Reseteo

---

## 🔧 MÉTODO 1: Resetear UN Código Específico

Usa este método cuando solo quieres resetear 1 o 2 códigos de prueba.

### ✅ PASO 1: Cambiar Reglas a Abiertas

Firebase Console → Realtime Database → **Reglas**

**Pega esto:**
```json
{
  "rules": {
    ".read": true,
    ".write": true
  }
}
```

Clic en **"Publicar"**

---

### ✅ PASO 2: Borrar el Código de la Lista `usedCodes`

Firebase Console → Realtime Database → **Datos**

1. Ve a `usedCodes`
2. Busca el índice que contiene tu código (ej: `"223DGX9G"`)
   - Aparecerá como: `0: "223DGX9G"`
3. Haz clic en **el número** (0)
4. **⋮ (tres puntos) → Eliminar**
5. Confirmar

✅ Ahora `usedCodes` estará vacío o sin ese código

---

### ✅ PASO 3: Cambiar `usado` a `false`

1. Ve a `validCodes/223DGX9G/usado`
   - Navega expandiendo: validCodes → 223DGX9G → usado
2. Haz clic en el valor `true`
3. Cámbialo a `false`
4. Presiona **Enter**

✅ El código ahora se puede usar de nuevo

---

### ✅ PASO 4: (Opcional) Restar Puntos

Si quieres también restar los puntos que sumó ese código:

1. Ve a `courses/3º_ESO_A` (o la clase correspondiente)
2. Verás un número (ej: `1`)
3. Haz clic en el número
4. Cámbialo a `0` (o resta los puntos del código)
5. Presiona **Enter**

✅ Los puntos se han restado

---

### ✅ PASO 5: Volver a Reglas Seguras

Firebase Console → Realtime Database → **Reglas**

**Borra todo y pega esto:**
```json
{
  "rules": {
    ".read": true,
    "validCodes": {
      "$code": {
        "usado": {
          ".write": "!data.exists() || data.val() === false"
        }
      }
    },
    "courses": {
      ".write": true
    },
    "usedCodes": {
      ".write": true
    }
  }
}
```

Clic en **"Publicar"**

✅ **¡Listo!** Código resetado y sistema seguro de nuevo

---

## 📊 Resultado del Método 1

**Antes:**
```
validCodes/
  └── 223DGX9G
      └── usado: true

usedCodes/
  └── 0: "223DGX9G"

courses/
  └── 3º_ESO_A: 1
```

**Después:**
```
validCodes/
  └── 223DGX9G
      └── usado: false  ✅

usedCodes/
  (vacío o sin ese código)  ✅

courses/
  └── 3º_ESO_A: 0  ✅
```

---

## ⚡ Resumen Rápido - Método 1

```
1. Reglas → Abiertas → Publicar
2. usedCodes/0 → Eliminar (solo el índice, no la carpeta)
3. validCodes/223DGX9G/usado → Cambiar a false
4. courses/3º_ESO_A → Restar puntos
5. Reglas → Seguras → Publicar
✅ Código resetado
```

**Tiempo:** 2-3 minutos

---

---

## 🔄 MÉTODO 2: Reseteo Completo (Todos los Códigos)

Usa este método cuando quieres borrar TODO y empezar de cero.

### ✅ PASO 1: Cambiar Reglas a Abiertas

Firebase Console → Realtime Database → **Reglas**

**Pega esto:**
```json
{
  "rules": {
    ".read": true,
    ".write": true
  }
}
```

Clic en **"Publicar"**

---

### ✅ PASO 2: Borrar TODO

Firebase Console → Realtime Database → **Datos**

1. Haz clic en la **raíz** del proyecto
   - Aparecerá como: `breath-8f51d-default-rtdb`
2. **⋮ (tres puntos) → Eliminar**
3. Confirmar
4. **Espera 5 segundos** (se borra todo)

✅ Base de datos vacía

---

### ✅ PASO 3: Importar JSON Fresco

Firebase Console → Realtime Database → **Datos**

1. **⋮ (tres puntos) → Importar JSON**
2. Clic en **"Examinar"** o **"Browse"**
3. Selecciona tu archivo: `codigos_firebase_XXXXXXXX.json`
   - Este archivo lo tienes guardado de cuando ejecutaste `generar_codigos.py`
4. Seleccionar **"Importar"**
5. **Espera 10-15 segundos** (se importan los 1,350 códigos)

✅ Todos los códigos están frescos (`usado: false`)

---

### ✅ PASO 4: Verificar Importación

Comprueba que todo se importó correctamente:

```
validCodes (1350)  ← Debe decir 1350
courses
  ├── 3º_ESO_A: 0
  ├── 3º_ESO_B: 0
  └── ...
usedCodes (vacío o no aparece)
```

✅ Si ves esto, la importación fue exitosa

---

### ✅ PASO 5: Volver a Reglas Seguras

Firebase Console → Realtime Database → **Reglas**

**Borra todo y pega esto:**
```json
{
  "rules": {
    ".read": true,
    "validCodes": {
      "$code": {
        "usado": {
          ".write": "!data.exists() || data.val() === false"
        }
      }
    },
    "courses": {
      ".write": true
    },
    "usedCodes": {
      ".write": true
    }
  }
}
```

Clic en **"Publicar"**

✅ **¡Listo!** Todo resetado, 1,350 códigos frescos, sistema seguro

---

## 📊 Resultado del Método 2

**Antes (con códigos usados):**
```
validCodes (1350)
  ├── 223DGX9G {usado: true}
  ├── ABC12345 {usado: true}
  └── ...

courses
  ├── 3º_ESO_A: 25
  ├── 3º_ESO_B: 18
  └── ...

usedCodes
  ├── 0: "223DGX9G"
  ├── 1: "ABC12345"
  └── ...
```

**Después (todo fresco):**
```
validCodes (1350)
  ├── 223DGX9G {usado: false}  ✅
  ├── ABC12345 {usado: false}  ✅
  └── ...

courses
  ├── 3º_ESO_A: 0  ✅
  ├── 3º_ESO_B: 0  ✅
  └── ...

usedCodes
  (vacío)  ✅
```

---

## ⚡ Resumen Rápido - Método 2

```
1. Reglas → Abiertas → Publicar
2. Datos → Raíz → Eliminar → Confirmar
3. ⋮ → Importar JSON → codigos_firebase_XXXXXXXX.json
4. Esperar importación (10-15 seg)
5. Reglas → Seguras → Publicar
✅ Reseteo completo
```

**Tiempo:** 2-3 minutos

---

---

## 📂 Dónde Encontrar el Archivo JSON

### Si Lo Tienes Guardado:

Busca en tu ordenador el archivo:
```
codigos_firebase_20260113_214212.json
```

(La fecha puede ser diferente)

**Ubicación típica:**
- Windows: `C:\Users\TuUsuario\Documents\breathe\`
- Mac: `/Users/TuUsuario/Documents/breathe/`
- Donde ejecutaste `generar_codigos.py`

---

### Si NO Lo Encuentras:

#### Opción A: Generarlo de Nuevo

```bash
python generar_codigos.py
```

- Genera un nuevo `codigos_firebase_XXXXXXXX.json`
- **CUIDADO:** Los códigos serán DIFERENTES
- Si ya distribuiste códigos a profesores, NO hagas esto

#### Opción B: Descargar de Firebase (Backup)

Si subiste los códigos a Firebase:

1. Firebase Console → Realtime Database → Datos
2. Clic en la **raíz** (breath-8f51d-default-rtdb)
3. **⋮ → Exportar JSON**
4. Guardar como: `backup_YYYYMMDD.json`
5. Este archivo te sirve para reimportar

---

---

## 🎯 ¿Cuándo Usar Cada Método?

| Situación | Método Recomendado |
|-----------|-------------------|
| Probé 1-2 códigos | **Método 1** (individual) |
| Probé muchos códigos | **Método 2** (completo) |
| Antes del día del juego real | **Método 2** (completo) |
| Después del juego (para mostrar resultados) | Ninguno (dejar como está) |
| Error grave en la base de datos | **Método 2** (completo) |

---

## ⚠️ IMPORTANTE: No Olvides las Reglas

**Cada vez que cambies a reglas abiertas:**
```json
{
  "rules": {
    ".read": true,
    ".write": true  ← PELIGRO
  }
}
```

**SIEMPRE vuelve a las reglas seguras después:**
```json
{
  "rules": {
    ".read": true,
    "validCodes": {
      "$code": {
        "usado": {
          ".write": "!data.exists() || data.val() === false"
        }
      }
    },
    "courses": {
      ".write": true
    },
    "usedCodes": {
      ".write": true
    }
  }
}
```

**Si dejas las reglas abiertas:**
- ⚠️ Cualquiera puede modificar todo
- ⚠️ Alumnos podrían hacer trampa fácilmente
- ⚠️ Alguien podría borrar la base de datos

---

## 📋 Checklist de Reseteo

Antes de hacer el reseteo completo (Método 2):

- [ ] Tengo el archivo `codigos_firebase_XXXXXXXX.json`
- [ ] He hecho backup de Firebase (⋮ → Exportar JSON)
- [ ] Los profesores tienen sus archivos TXT
- [ ] Estoy seguro de que quiero borrar todo
- [ ] Sé que después debo volver a reglas seguras

---

## 🆘 Solución de Problemas

### Problema: "No puedo importar JSON"

**Causa:** Reglas muy restrictivas

**Solución:**
1. Verifica que las reglas estén en modo abierto
2. Publica las reglas
3. Refresca la página de Firebase
4. Intenta importar de nuevo

---

### Problema: "Importación se queda en 0%"

**Causa:** Archivo JSON muy grande o conexión lenta

**Solución:**
1. Espera 30 segundos más
2. Refresca la página
3. Verifica si los datos se importaron (cuenta los códigos)
4. Si no, intenta de nuevo

---

### Problema: "Aparecen menos de 1,350 códigos"

**Causa:** Importación incompleta

**Solución:**
1. Borrar todo de nuevo (raíz → Eliminar)
2. Verificar que el JSON tenga 1,350 códigos (abrirlo en editor de texto)
3. Importar de nuevo

---

### Problema: "No encuentro el archivo JSON"

**Solución:**
1. Busca en tu ordenador: `codigos_firebase_*.json`
2. Si no lo tienes, genera de nuevo: `python generar_codigos.py`
3. **CUIDADO:** Si ya distribuiste códigos, esto genera códigos NUEVOS diferentes

---

## 💾 Hacer Backup Antes de Resetear

**Siempre recomendado:**

Antes de hacer Método 2 (borrar todo):

1. Firebase Console → Datos
2. Clic en raíz
3. **⋮ → Exportar JSON**
4. Guardar como: `backup_antes_reseteo_YYYYMMDD.json`

**Por si acaso necesitas volver atrás.**

---

## ✅ Resumen Final

**Método 1 (1 código):**
- Reglas abiertas → Borrar de usedCodes → Cambiar usado a false → Reglas seguras
- **Tiempo:** 2-3 min

**Método 2 (reseteo completo):**
- Reglas abiertas → Borrar raíz → Importar JSON → Reglas seguras
- **Tiempo:** 2-3 min

**Archivo JSON:**
- Buscar `codigos_firebase_XXXXXXXX.json` en tu ordenador
- O exportar de Firebase (⋮ → Exportar JSON)
- O regenerar con `python generar_codigos.py` (solo si no has distribuido códigos)

**IMPORTANTE:**
- Siempre volver a reglas seguras
- Hacer backup antes de borrar todo
- Verificar que se importaron los 1,350 códigos

---

*Guía de Reseteo - Proyecto BREATHE*  
*IES Diego Velázquez - Torrelodones, Madrid*

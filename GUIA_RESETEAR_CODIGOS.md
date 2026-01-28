# 🔄 GUÍA: Resetear Códigos en Firebase (CORREGIDA)

## 📋 Dos Métodos de Reseteo

---

## 🗑️ MÉTODO 1: Borrar Carpetas Completas (Reseteo Total)

Usa este método cuando quieres **borrar TODO** y empezar de cero.

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

### ✅ PASO 2: Borrar Carpeta `usedCodes` Completa

Firebase Console → Realtime Database → **Datos**

1. Haz clic en la carpeta **`usedCodes`**
2. **⋮ (tres puntos) → Eliminar**
3. Confirmar

✅ Carpeta `usedCodes` eliminada

**NOTA:** La carpeta desaparece completamente. Se volverá a crear automáticamente cuando uses el próximo código.

---

### ✅ PASO 3: Borrar Carpeta `courses` Completa

Firebase Console → Realtime Database → **Datos**

1. Haz clic en la carpeta **`courses`**
2. **⋮ (tres puntos) → Eliminar**
3. Confirmar

✅ Carpeta `courses` eliminada

**NOTA:** La carpeta desaparece completamente. Se volverá a crear automáticamente cuando uses el próximo código.

---

### ✅ PASO 4: Cambiar TODOS los códigos a `usado: false`

**Opción A - Manual (si son pocos):**

Para cada código que usaste:
1. Ve a `validCodes/CODIGO/usado`
2. Cambia `true` a `false`
3. Enter

**Opción B - Borrar TODO y Reimportar (RECOMENDADO):**

1. Haz clic en la **raíz** (breath-8f51d-default-rtdb)
2. **⋮ → Eliminar** → Confirmar
3. **⋮ → Importar JSON**
4. Seleccionar `codigos_firebase_XXXXXXXX.json`
5. Importar
6. Esperar 10-15 segundos

✅ TODOS los códigos vuelven a `usado: false`

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

✅ **¡Listo!** Todo resetado completamente

---

## 📊 Resultado del Método 1

**Antes:**
```
validCodes/
  ├── 223DGX9G {usado: true}
  ├── ABC12345 {usado: true}
  └── ...

usedCodes/
  ├── 0: "223DGX9G"
  ├── 1: "ABC12345"
  └── ...

courses/
  ├── 3º_ESO_A: 25  ← PUNTOS
  ├── 3º_ESO_B: 18  ← PUNTOS
  └── ...
```

**Después:**
```
validCodes/
  ├── 223DGX9G {usado: false}  ✅
  ├── ABC12345 {usado: false}  ✅
  └── ...

usedCodes/
  (NO APARECE - se creará con el próximo código)  ✅

courses/
  (NO APARECE - se creará con el próximo código)  ✅
```

---

## ⚡ Resumen Rápido - Método 1

```
1. Reglas → Abiertas → Publicar
2. usedCodes → Eliminar carpeta completa
3. courses → Eliminar carpeta completa
4. validCodes → Cambiar todos a usado:false (o reimportar JSON)
5. Reglas → Seguras → Publicar
✅ Reseteo total
```

**Tiempo:** 3-5 minutos

**Cuándo usar:** Antes del día del juego real, después de muchas pruebas

---

---

## 🔧 MÉTODO 2: Borrar Códigos Específicos

Usa este método cuando solo quieres **resetear 1 o 2 códigos** de prueba.

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

### ✅ PASO 2: Borrar el Código Específico de `usedCodes`

Firebase Console → Realtime Database → **Datos**

1. Ve a `usedCodes`
2. Busca el índice que contiene tu código
   - Ejemplo: `0: "223DGX9G"`
3. Haz clic en **el número** (0)
4. **⋮ → Eliminar**
5. Confirmar

✅ Código borrado de la lista

**NOTA:** Si borras el último código, la carpeta `usedCodes` desaparecerá completamente (es normal).

---

### ✅ PASO 3: Cambiar `usado` a `false` del Código Específico

1. Ve a `validCodes/223DGX9G/usado`
2. Haz clic en `true`
3. Cámbialo a `false`
4. Enter

✅ El código se puede usar de nuevo

---

### ✅ PASO 4: Restar los Puntos en `courses`

**MUY IMPORTANTE:** Tienes que restar los PUNTOS que sumó ese código.

1. Ve a `courses/3º_ESO_A` (la clase del código)
2. Verás un número (ej: `25`)
3. **Calcula:** `25 - puntos_del_código`
   - Si el código era de 3 puntos: `25 - 3 = 22`
4. Cambia el valor a `22`
5. Enter

✅ Puntos ajustados correctamente

**💡 Ejemplo:**
- Clase tenía: 25 puntos
- Código usado: 3 puntos
- Nuevo total: 25 - 3 = **22 puntos**

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

✅ **¡Listo!** Código específico resetado

---

## 📊 Resultado del Método 2

**Antes:**
```
validCodes/
  └── 223DGX9G {usado: true, puntos: 3}

usedCodes/
  └── 0: "223DGX9G"

courses/
  └── 3º_ESO_A: 25  ← PUNTOS totales
```

**Después:**
```
validCodes/
  └── 223DGX9G {usado: false, puntos: 3}  ✅

usedCodes/
  (vacío o sin ese código)  ✅

courses/
  └── 3º_ESO_A: 22  ← 25 - 3 = 22 ✅
```

---

## ⚡ Resumen Rápido - Método 2

```
1. Reglas → Abiertas → Publicar
2. usedCodes/0 → Eliminar código específico
3. validCodes/223DGX9G/usado → Cambiar a false
4. courses/3º_ESO_A → Restar puntos del código (ej: 25-3=22)
5. Reglas → Seguras → Publicar
✅ Código específico resetado
```

**Tiempo:** 2-3 minutos

**Cuándo usar:** Prueba rápida con 1-2 códigos

---

---

## 🎯 ¿Cuándo Usar Cada Método?

| Situación | Método Recomendado |
|-----------|-------------------|
| Probé 1-2 códigos | **Método 2** (específico) |
| Probé muchos códigos (5+) | **Método 1** (total) |
| Antes del día del juego real | **Método 1** (total) |
| Me confundí con 1 código | **Método 2** (específico) |
| Quiero empezar completamente de cero | **Método 1** (total) |

---

## ❓ Preguntas Frecuentes

### ¿Qué contiene la carpeta `courses`?

**R:** PUNTOS totales de cada clase, NO cantidad de códigos.

```
courses/
  ├── 3º_ESO_A: 25    ← 25 PUNTOS (puede venir de 3 códigos de 8+10+7 pts)
  ├── 3º_ESO_B: 18    ← 18 PUNTOS
```

---

### ¿Por qué desaparecen `usedCodes` y `courses`?

**R:** Firebase elimina automáticamente las carpetas vacías. Es normal. Se vuelven a crear automáticamente cuando uses códigos.

---

### ¿Cómo sé cuántos puntos tenía el código que borré?

**R:** Antes de borrar, mira:
```
validCodes/223DGX9G/puntos: 3  ← Aquí dice cuántos puntos vale
```

Usa ese número para restar en `courses`.

---

### ¿Qué pasa si me equivoco restando puntos?

**R:** Puedes corregirlo:
1. Reglas → Abiertas
2. Ve a `courses/3º_ESO_A`
3. Cambia al valor correcto
4. Reglas → Seguras

---

### ¿Tengo que borrar `courses` obligatoriamente?

**R:** Depende del método:
- **Método 1** (total): SÍ, borra la carpeta completa
- **Método 2** (específico): NO borres la carpeta, solo resta los puntos

---

## 🔍 Entendiendo `courses`

### Ejemplo Detallado:

```
3º ESO A usa estos códigos:
  - Código ABC (3 puntos)
  - Código XYZ (10 puntos)
  - Código DEF (2 puntos)

courses/3º_ESO_A: 15  ← 3 + 10 + 2 = 15 PUNTOS
```

**Si reseteo código XYZ:**
```
courses/3º_ESO_A: 5  ← 15 - 10 = 5 PUNTOS
```

---

## 📂 Dónde Encontrar el Archivo JSON (para Método 1)

### Si Lo Tienes Guardado:

Busca en tu ordenador:
```
codigos_firebase_20260113_214212.json
```

**Ubicación típica:**
- Windows: `C:\Users\TuUsuario\Documents\breathe\`
- Mac: `/Users/TuUsuario/Documents\breathe/`

---

### Si NO Lo Encuentras:

#### Opción A: Exportar de Firebase

1. Firebase Console → Datos → Raíz
2. **⋮ → Exportar JSON**
3. Guardar como: `backup.json`
4. Usar para reimportar

#### Opción B: Generar de Nuevo (⚠️ CUIDADO)

```bash
python generar_codigos.py
```

**⚠️ SOLO si NO has distribuido códigos a profesores**
(Los códigos nuevos serán diferentes)

---

## ⚠️ RECORDATORIO CRÍTICO

**Siempre vuelve a reglas seguras después:**

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

**Si no lo haces:**
- ⚠️ Cualquiera puede modificar todo
- ⚠️ Alumnos pueden hacer trampa
- ⚠️ Podrían borrar la base de datos

---

## 💾 Hacer Backup Siempre

Antes de borrar carpetas completas:

1. Firebase Console → Datos → Raíz
2. **⋮ → Exportar JSON**
3. Guardar como: `backup_YYYYMMDD.json`

**Por si necesitas recuperar.**

---

## ✅ Resumen Final

### Método 1 (Borrar TODO):
1. ✅ Borrar carpeta `usedCodes` completa
2. ✅ Borrar carpeta `courses` completa
3. ✅ Cambiar todos los códigos a `usado: false` (o reimportar JSON)
4. ✅ Volver a reglas seguras

**Resultado:** Todo a cero, empezar de nuevo

---

### Método 2 (Códigos específicos):
1. ✅ Borrar código de `usedCodes` (índice específico)
2. ✅ Cambiar `usado: false` del código
3. ✅ Restar PUNTOS en `courses/3º_ESO_X`
4. ✅ Volver a reglas seguras

**Resultado:** Solo esos códigos reseteados

---

## 🎯 Diferencia Clave

**Método 1:**
- Borra carpetas COMPLETAS
- Todo desaparece
- Se recrea al usar códigos

**Método 2:**
- Borra elementos ESPECÍFICOS
- Las carpetas siguen existiendo
- Solo se ajustan valores

---

*Guía de Reseteo Corregida - Proyecto BREATHE*  
*IES Diego Velázquez - Torrelodones, Madrid*

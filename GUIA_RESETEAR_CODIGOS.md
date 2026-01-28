# 🔄 GUÍA: Resetear Códigos en Firebase (ACTUALIZADA)

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

### ✅ PASO 2: Borrar el Código de `usedCodes`

Firebase Console → Realtime Database → **Datos**

1. Ve a `usedCodes`
2. Busca el índice que contiene tu código (ej: `"223DGX9G"`)
   - Aparecerá como: `0: "223DGX9G"`
3. Haz clic en **el número** (0)
4. **⋮ (tres puntos) → Eliminar**
5. Confirmar

✅ Código borrado de la lista

**⚠️ IMPORTANTE:** 
- Si borras el **último código** de `usedCodes`, **la carpeta completa desaparece**
- Esto es **NORMAL** en Firebase (carpetas vacías desaparecen automáticamente)
- La carpeta se volverá a crear sola cuando uses el próximo código
- **No es un error** ✅

---

### ✅ PASO 3: Cambiar `usado` a `false`

1. Ve a `validCodes/223DGX9G/usado`
   - Navega expandiendo: validCodes → 223DGX9G → usado
2. Haz clic en el valor `true`
3. Cámbialo a `false`
4. Presiona **Enter**

✅ El código ahora se puede usar de nuevo

---

### ✅ PASO 4: Resetear Puntos de la Clase

**SÍ, también debes hacer esto:**

1. Ve a `courses/3º_ESO_A` (o la clase correspondiente)
2. Verás un número (ej: `1`, `3`, `10`)
3. Haz clic en el número
4. **Opciones:**
   - **Volver a 0:** Cambia a `0`
   - **Restar puntos del código:** Resta los puntos (ej: si tenía 10 y el código era de 3 pts → pon `7`)
5. Presiona **Enter**

✅ Los puntos se han ajustado

**💡 Consejo:** Si solo hiciste una prueba con 1-2 códigos, lo más fácil es **poner todos los cursos a 0**.

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
  └── 3º_ESO_A: 3
```

**Después:**
```
validCodes/
  └── 223DGX9G
      └── usado: false  ✅

usedCodes/
  (DESAPARECE - es normal)  ✅

courses/
  └── 3º_ESO_A: 0  ✅
```

**⚠️ NOTA:** La carpeta `usedCodes` desaparece porque está vacía. Firebase elimina automáticamente las carpetas vacías.

---

## ⚡ Resumen Rápido - Método 1

```
1. Reglas → Abiertas → Publicar
2. usedCodes/0 → Eliminar (la carpeta desaparecerá si estaba vacía)
3. validCodes/223DGX9G/usado → Cambiar a false
4. courses/3º_ESO_A → Poner a 0 (o restar puntos)
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

✅ Base de datos completamente vacía

**Esto borra:**
- ✅ Todos los `validCodes` (los 1,350)
- ✅ Todos los `usedCodes`
- ✅ Todos los `courses` con sus puntos
- ✅ TODO

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
  ├── 3º_ESO_C: 0
  ├── 3º_ESO_D: 0
  ├── 3º_ESO_E: 0
  └── 3º_ESO_F: 0
usedCodes (NO aparece - es normal)  ✅
```

✅ Si ves esto, la importación fue exitosa

**NOTA:** 
- `usedCodes` NO aparecerá hasta que uses el primer código
- Esto es NORMAL ✅

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
  (NO APARECE - se creará cuando uses códigos)  ✅
```

---

## ⚡ Resumen Rápido - Método 2

```
1. Reglas → Abiertas → Publicar
2. Datos → Raíz → Eliminar → Confirmar
3. ⋮ → Importar JSON → codigos_firebase_XXXXXXXX.json
4. Esperar importación (10-15 seg)
5. Verificar: validCodes (1350), courses (todos a 0)
6. Reglas → Seguras → Publicar
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
- **⚠️ CUIDADO:** Los códigos serán DIFERENTES
- **Solo hazlo si NO has distribuido códigos a profesores**
- Si ya distribuiste códigos, NO uses esta opción

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

## ❓ Preguntas Frecuentes

### ¿Por qué desaparece la carpeta `usedCodes`?

**R:** Firebase elimina automáticamente las carpetas vacías. Es una característica del sistema, no un error. La carpeta se volverá a crear automáticamente cuando uses el próximo código.

---

### ¿Tengo que resetear los puntos de `courses` también?

**R:** **SÍ**. Si no los reseteas, las clases mantendrán los puntos de las pruebas anteriores. Lo más fácil es poner todos a 0.

---

### ¿Puedo borrar solo `usedCodes` y dejar el resto?

**R:** Técnicamente sí, pero entonces:
- Los códigos seguirán marcados como `usado: true` en `validCodes`
- Las clases mantendrán sus puntos en `courses`
- Los códigos NO se podrán reutilizar

**Mejor:** Usa Método 1 (resetear código completo) o Método 2 (reseteo total).

---

### ¿Qué pasa si no vuelvo a poner las reglas seguras?

**R:** 
- ⚠️ Cualquiera puede modificar TODO en tu Firebase
- ⚠️ Alumnos podrían hacer trampa fácilmente
- ⚠️ Alguien podría borrar toda la base de datos

**SIEMPRE vuelve a las reglas seguras.**

---

## ⚠️ RECORDATORIO CRÍTICO: Las Reglas

**Cada vez que cambies a reglas abiertas:**
```json
{
  "rules": {
    ".read": true,
    ".write": true  ← PELIGRO: Todo se puede modificar
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

**Tiempo máximo con reglas abiertas:** 5 minutos

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
- [ ] Entiendo que `usedCodes` no aparecerá hasta usar códigos

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
2. Si no lo tienes, exporta de Firebase (⋮ → Exportar JSON)
3. Si es imposible recuperarlo, genera de nuevo: `python generar_codigos.py`
   - **⚠️ CUIDADO:** Solo si NO has distribuido códigos a profesores

---

### Problema: "La carpeta `usedCodes` desapareció"

**Solución:**
- ✅ Esto es NORMAL
- Firebase elimina carpetas vacías automáticamente
- Se volverá a crear sola cuando uses el próximo código
- **No es un error, no hagas nada**

---

### Problema: "Los puntos siguen después de resetear"

**Causa:** Olvidaste resetear `courses`

**Solución:**
1. Reglas → Abiertas
2. Ve a cada `courses/3º_ESO_X`
3. Ponlos a `0`
4. Reglas → Seguras

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
- Reglas abiertas → Borrar de usedCodes → Cambiar usado a false → **Resetear courses** → Reglas seguras
- **Tiempo:** 2-3 min
- **Carpeta usedCodes desaparecerá si estaba vacía** (normal)

**Método 2 (reseteo completo):**
- Reglas abiertas → Borrar raíz → Importar JSON → Reglas seguras
- **Tiempo:** 2-3 min
- **Todo vuelve a 0**, usedCodes no aparecerá hasta usar códigos (normal)

**Qué se resetea en ambos:**
- ✅ validCodes/{codigo}/usado → false
- ✅ usedCodes → vacío (carpeta puede desaparecer)
- ✅ courses → puntos a 0

**IMPORTANTE:**
- Siempre volver a reglas seguras
- Hacer backup antes de borrar todo
- Verificar que se importaron los 1,350 códigos
- `usedCodes` desaparecerá si está vacía (es normal)

---

*Guía de Reseteo Actualizada - Proyecto BREATHE*  
*IES Diego Velázquez - Torrelodones, Madrid*

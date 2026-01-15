# 🔥 GUÍA FIREBASE - Configuración Completa

## 📖 Índice

1. [Crear Proyecto Firebase](#paso-1-crear-proyecto-firebase)
2. [Configurar Realtime Database](#paso-2-configurar-realtime-database)
3. [Configurar Reglas de Seguridad](#paso-3-configurar-reglas-de-seguridad)
4. [Subir Códigos](#paso-4-subir-códigos)
5. [Verificar Funcionamiento](#paso-5-verificar-funcionamiento)
6. [Solución de Problemas](#solución-de-problemas)

---

## ⏱️ Tiempo Total: 15 minutos

**Requisitos:**
- ✅ Cuenta de Google
- ✅ Navegador web
- ✅ Códigos ya generados (`codigos_firebase_XXXXXXXX.json`)

---

## 📋 PASO 1: Crear Proyecto Firebase

### 1.1 Acceder a Firebase

Abre tu navegador y ve a:
```
https://console.firebase.google.com/
```

### 1.2 Iniciar Sesión

- Haz clic en **"Ir a la consola"** (arriba derecha)
- Inicia sesión con tu cuenta de Google
- Si no tienes, crea una (es gratis)

### 1.3 Crear Nuevo Proyecto

1. Clic en **"Agregar proyecto"** o **"Create a project"**

2. **Nombre del proyecto:**
   ```
   breath-8f51d
   ```
   (o el nombre que prefieras)

3. Clic en **"Continuar"**

4. **Google Analytics:** 
   - **Desactívalo** (no lo necesitas)
   - Desmarca la casilla
   - Clic en **"Crear proyecto"**

5. **Espera 30 segundos** mientras Firebase crea el proyecto

6. Clic en **"Continuar"**

✅ **¡Proyecto creado!**

---

## 📋 PASO 2: Configurar Realtime Database

### 2.1 Crear Base de Datos

1. En el **menú lateral izquierdo**, busca:
   ```
   Compilación → Realtime Database
   ```
   (o "Build → Realtime Database")

2. Clic en **"Crear base de datos"** (botón azul)

### 2.2 Seleccionar Ubicación

1. **Ubicación:** Selecciona
   ```
   Estados Unidos (us-central1)
   ```
   (Recomendado para mejor velocidad)

2. Clic en **"Siguiente"**

### 2.3 Configurar Reglas Iniciales

**MUY IMPORTANTE:** Selecciona:
```
🟢 Comenzar en modo de prueba
```
(NO selecciones "modo bloqueado")

Clic en **"Habilitar"**

### 2.4 Esperar

Espera 10-15 segundos mientras Firebase crea la base de datos.

Verás una pantalla con:
```
breath-8f51d-default-rtdb
https://breath-8f51d-default-rtdb.firebaseio.com
```

✅ **¡Base de datos creada!**

---

## 📋 PASO 3: Configurar Reglas de Seguridad

### 3.1 Ir a Reglas

En la pantalla de Realtime Database:
1. Arriba, haz clic en la pestaña **"Reglas"**

### 3.2 Verás algo como:

```json
{
  "rules": {
    ".read": "now < 1234567890000",
    ".write": "now < 1234567890000"
  }
}
```

### 3.3 REEMPLAZAR con estas Reglas Seguras

**BORRA TODO** y pega esto:

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

### 3.4 Publicar

Clic en **"Publicar"** (botón azul arriba derecha)

### 3.5 ¿Qué hacen estas reglas?

✅ **Lectura abierta** - Cualquiera puede leer datos (necesario para pantalla)
✅ **Escritura en courses** - Se pueden sumar puntos
✅ **Escritura en usedCodes** - Se pueden registrar códigos usados
✅ **Protección de códigos** - NO se pueden reutilizar códigos ya usados
❌ **Bloquea trampa** - Impide cambiar `usado: true` a `false`

✅ **¡Reglas configuradas!**

---

## 📋 PASO 4: Subir Códigos

Ahora vamos a subir los 1,350 códigos a Firebase.

### 4.1 Preparar el Archivo

Necesitas el archivo:
```
codigos_firebase_XXXXXXXX.json
```

Este archivo lo generaste con `python generar_codigos.py`

### 4.2 Importar a Firebase

#### Opción A: Manual (Recomendada)

1. En Firebase Console → **Realtime Database** → **Datos**

2. Haz clic en los **3 puntos verticales (⋮)** arriba derecha

3. Clic en **"Importar JSON"**

4. **Selecciona** tu archivo `codigos_firebase_XXXXXXXX.json`

5. **Importante:** Cuando pregunte, selecciona:
   ```
   ⚠️ Sobrescribir
   ```
   (Esto borrará cualquier dato anterior)

6. Clic en **"Importar"**

7. **Espera 5-10 segundos**

#### Opción B: Con Script Python

Si tienes Python y ya configuraste las credenciales:

```bash
pip install firebase-admin
python subir_firebase.py
```

### 4.3 Verificar

Después de importar, deberías ver en **Datos**:

```
breath-8f51d-default-rtdb
├── validCodes (1350 elementos)
│   ├── ABC12345
│   ├── XYZ67890
│   └── ...
├── courses
│   ├── 3º_ESO_A: 0
│   ├── 3º_ESO_B: 0
│   └── ...
└── usedCodes: []
```

✅ **¡Códigos subidos!**

---

## 📋 PASO 5: Verificar Funcionamiento

### 5.1 Abrir Interfaz de Alumnos

Abre en tu navegador:
```
index_FINAL_v2.html
```

### 5.2 Probar un Código

1. **Selecciona:** 3º ESO A

2. **Busca un código real** en Firebase:
   - Firebase Console → Realtime Database → Datos
   - Expande `validCodes`
   - Copia un código (ej: `ABC12345`)
   - Verifica que su campo `clase` sea `"3º ESO A"`

3. **Introduce el código** en la interfaz

4. **Verifica el mensaje:**
   ```
   ✅ ¡Excelente 3º ESO A!
   Has ganado X puntos de oxígeno
   ```

### 5.3 Verificar en Firebase

1. Ve a Firebase Console → Realtime Database → Datos

2. Busca el código que usaste en `validCodes`

3. Verifica:
   ```
   ABC12345
     ├── usado: true  ← Cambió de false a true
     └── ...
   ```

4. Ve a `courses/3º_ESO_A`
   ```
   3º_ESO_A: X  ← Tiene los puntos sumados
   ```

### 5.4 Abrir Pantalla

Abre en otra pestaña:
```
pantalla_normalizada_FINAL.html
```

Deberías ver:
- 6 tanques de oxígeno
- 3º ESO A tiene puntos
- El resto en 0
- Porcentajes con decimales

✅ **¡TODO FUNCIONA!** 🎉

---

## 🔄 Resetear para Nuevas Pruebas

### Cuándo resetear:
- Después de hacer pruebas
- Antes del día del juego real
- Si quieres empezar de cero

### Cómo resetear:

#### Opción A: Manual

1. **Cambiar reglas temporalmente** a:
```json
{
  "rules": {
    ".read": true,
    ".write": true
  }
}
```
Publicar

2. **Firebase Console → Datos**
3. Clic en **raíz** (breath-8f51d-default-rtdb)
4. **⋮ → Eliminar** → Confirmar
5. **⋮ → Importar JSON** → Seleccionar `codigos_firebase_XXXXXXXX.json`
6. **Volver a poner reglas seguras** (las del Paso 3)

#### Opción B: Script Automático

```bash
python resetear_firebase.py
```

Escribe `SI` para confirmar.

✅ **Todo vuelve a 0, códigos frescos**

---

## 🆘 Solución de Problemas

### Problema 1: "Error de conexión" en la pantalla

**Síntoma:**
```
Última actualización: Error de conexión (20:24:34)
```

**Causa:** Reglas de Firebase muy restrictivas

**Solución:**
1. Firebase Console → Realtime Database → Reglas
2. Verifica que diga `.read: true` en la raíz
3. Publicar
4. Refresca la pantalla

---

### Problema 2: "Código inválido" pero el código existe

**Síntoma:** Introduces un código válido pero dice que es inválido

**Causa:** El código no coincide con la clase seleccionada

**Solución:**
1. Ve a Firebase → validCodes → [tu código]
2. Mira el campo `clase`
3. Asegúrate de seleccionar ESA clase en la interfaz
4. Ejemplo: Si `clase: "3º ESO C"`, selecciona 3º ESO C

---

### Problema 3: Los códigos desaparecen de Firebase

**Síntoma:** Introduces un código y todo `validCodes` se borra

**Causa:** Bug en código JavaScript antiguo

**Solución:**
1. Asegúrate de usar `index_FINAL_v2.html` (no versiones antiguas)
2. Reimporta los códigos a Firebase
3. Verifica que el código NO tenga instrucciones de borrar

---

### Problema 4: No puedo importar JSON

**Síntoma:** Firebase no me deja importar

**Causa:** Reglas muy restrictivas

**Solución:**
1. Cambiar TEMPORALMENTE a reglas abiertas:
```json
{
  "rules": {
    ".read": true,
    ".write": true
  }
}
```
2. Importar JSON
3. Volver a reglas seguras (Paso 3)

---

### Problema 5: La pantalla no se actualiza

**Síntoma:** Añado puntos pero la pantalla no cambia

**Causa:** Caché del navegador o código antiguo

**Solución:**
1. **Refresco forzado:**
   - Windows/Linux: `Ctrl + Shift + R`
   - Mac: `Cmd + Shift + R`
2. Verificar que usas `pantalla_normalizada_FINAL.html`
3. Ver consola del navegador (F12) para errores

---

## 📊 Estructura de Datos en Firebase

### validCodes (Los códigos)
```json
"ABC12345": {
  "clase": "3º ESO A",
  "grupo": "Grupo_1",
  "actividad": "Actividad_1",
  "puntos": 1,
  "usado": false
}
```

### courses (Puntos de clases)
```json
{
  "3º_ESO_A": 0,
  "3º_ESO_B": 0,
  "3º_ESO_C": 0,
  "3º_ESO_D": 0,
  "3º_ESO_E": 0,
  "3º_ESO_F": 0
}
```

### usedCodes (Lista de usados)
```json
[
  "ABC12345",
  "XYZ67890"
]
```

---

## 🔐 Seguridad

### ¿Es seguro?

**Para un proyecto educativo: SÍ**

✅ Solo tus alumnos conocen la URL
✅ Los códigos se pueden usar solo UNA vez
✅ Impide la trampa más común (reutilizar códigos)
✅ No hay datos personales sensibles
✅ Es temporal (unas semanas)

### ¿Qué NO protege?

⚠️ Alguien técnico podría modificar puntos directamente
⚠️ Alguien podría borrar toda la base de datos

**Pero:** Estas acciones son MUY evidentes y fáciles de detectar.

### Recomendación:

Durante el juego: Usa las reglas del Paso 3
Después del juego: Cambia a solo lectura:
```json
{
  "rules": {
    ".read": true,
    ".write": false
  }
}
```

---

## 💾 Backup

### Hacer Backup Manual:

1. Firebase Console → Realtime Database → Datos
2. **⋮ → Exportar JSON**
3. Guardar como: `backup_YYYYMMDD.json`

**Recomendación:** Haz backup cada día durante el juego.

---

## 📈 Monitorear Uso

### Ver Actividad:

Firebase Console → Realtime Database → **Uso**

Verás:
- Lecturas/segundo
- Escrituras/segundo
- Conexiones simultáneas
- Almacenamiento usado

**Plan Gratuito (Spark):**
- ✅ 10 GB almacenamiento
- ✅ 100,000 conexiones simultáneas
- ✅ Más que suficiente para tu proyecto

---

## ✅ Checklist Final

Antes de empezar el juego, verifica:

- [ ] Firebase creado y configurado
- [ ] Realtime Database habilitada
- [ ] Reglas de seguridad publicadas
- [ ] 1,350 códigos importados
- [ ] Probado con un código real
- [ ] Pantalla muestra 6 tanques
- [ ] Códigos distribuidos a profesores
- [ ] Backup hecho

---

## 🎉 ¡Listo para el Juego!

Tu Firebase está configurado profesionalmente y listo para soportar la competición BREATHE.

**Características:**
- ⚡ Actualizaciones en tiempo real
- 🔒 Seguro contra trampas comunes
- 💾 Datos persistentes (nunca se pierden)
- 🌐 Accesible desde cualquier dispositivo
- 🆓 100% gratuito

---

**¡Que comience la misión de supervivencia en Marte!** 🚀

---

*Tiempo de configuración: 15 minutos*  
*Dificultad: Media*  
*Coste: $0.00*

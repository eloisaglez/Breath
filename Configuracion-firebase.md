# 🔥 GUÍA FIREBASE - Configuración Paso a Paso

## 🎯 ¿Qué vas a conseguir?

Después de seguir esta guía (10-15 minutos), tendrás:
- ✅ Los datos guardados en la nube (Firebase) para siempre
- ✅ Actualizaciones en tiempo real en todas las pantallas
- ✅ Funciona desde cualquier ordenador/navegador
- ✅ Los puntos NUNCA se pierden
- ✅ **100% GRATIS**

---

## 📋 PASO 1: Crear cuenta en Firebase (2 minutos)

### 1. Ve a Firebase
Abre tu navegador y ve a:
```
https://firebase.google.com
```

### 2. Inicia sesión
- Haz clic en **"Ir a la consola"** (arriba a la derecha)
- Inicia sesión con tu cuenta de Google
- Si no tienes, créala (es gratis)

---

## 📋 PASO 2: Crear proyecto (3 minutos)

### 1. Crear nuevo proyecto
- Haz clic en **"Agregar proyecto"** (o "Add project")
- Te pedirá 3 pasos:

### 2. Paso 1/3: Nombre del proyecto
```
Nombre: breath
```
- Haz clic en **Continuar**

### 3. Paso 2/3: Google Analytics
- **Desactiva** Google Analytics (no lo necesitas)
- Desmarca la casilla
- Haz clic en **Crear proyecto**

### 4. Espera 30 segundos
- Firebase está creando tu proyecto
- Cuando termine, haz clic en **Continuar**

✅ **¡Proyecto creado!**

---

## 📋 PASO 3: Configurar Realtime Database (3 minutos)

### 1. En el menú lateral izquierdo
- Busca **"Compilación"** o **"Build"**
- Haz clic en **"Realtime Database"**

### 2. Crear base de datos
- Haz clic en **"Crear base de datos"** (botón azul)

### 3. Ubicación
- Selecciona: **Estados Unidos (us-central1)** (recomendado)
- Haz clic en **Siguiente**

### 4. Reglas de seguridad
**MUY IMPORTANTE:** Selecciona:
```
🔘 Comenzar en modo de prueba
```
(NO selecciones "modo bloqueado")

- Haz clic en **Habilitar**

### 5. Espera 10 segundos
- Firebase está creando la base de datos

✅ **¡Base de datos creada!**

---

## 📋 PASO 4: Obtener configuración (2 minutos)

### 1. Volver a inicio del proyecto
- En el menú lateral, haz clic en **⚙️ (engranaje)** arriba
- Haz clic en **"Configuración del proyecto"**

### 2. Bajar hasta "Tus apps"
- Verás el mensaje: "No hay apps en tu proyecto"
- Haz clic en el icono **</>** (Web)

### 3. Registrar app
- Apodo de la app: `breath-web`
- **NO marques** "Firebase Hosting"
- Haz clic en **Registrar app**

### 4. Copiar configuración
Verás un bloque de código que empieza con `const firebaseConfig = {` y contiene varios campos como `apiKey`, `authDomain`, `databaseURL`, etc.

**🚨 IMPORTANTE:** Copia TODO este bloque (desde `{` hasta `}`) incluyendo todas las líneas con sus valores.

### 5. Pégalo en un lugar seguro
- Notepad
- Notes
- TextEdit
- Lo necesitarás en el siguiente paso

### 6. Continuar
- Haz clic en **"Ir a la consola"**

✅ **¡Configuración obtenida!**

---

## 📋 PASO 5: Configurar reglas de seguridad (2 minutos)

**Importante:** Para que funcione, necesitas configurar las reglas.

### 1. En el menú lateral izquierdo
- **Compilación** → **Realtime Database**
- Arriba, haz clic en la pestaña **"Reglas"**

### 2. Verás algo así:
```json
{
  "rules": {
    ".read": "now < 1234567890000",
    ".write": "now < 1234567890000"
  }
}
```

### 3. REEMPLAZA todo por esto:
```json
{
  "rules": {
    ".read": true,
    ".write": true
  }
}
```

### 4. Publicar
- Haz clic en **Publicar** (botón azul)

⚠️ **Nota:** Estas reglas son para uso educativo. Cualquiera puede leer/escribir, pero para un proyecto escolar está bien.

✅ **¡Reglas configuradas!**

---

## 📋 PASO 6: Configurar los archivos HTML (5 minutos)

Ahora vamos a poner tu configuración de Firebase en los archivos HTML.

### 1. Abre index.html y pantalla.html

Con un editor de texto:
- TextEdit (Mac)
- Notepad++ (Windows)
- VSCode
- Cualquier editor

### 2. Busca la sección de `firebaseConfig`
Localiza donde dice `const firebaseConfig = {` en ambos archivos. Verás algo con valores de ejemplo o placeholders.

### 3. REEMPLAZA con tu configuración
Pega la configuración completa que copiaste en el **Paso 4** (sustituyendo todo el contenido del objeto `firebaseConfig`).

**⚠️ IMPORTANTE:** Asegúrate de que:
- Has copiado TODOS los valores correctamente
- No hay espacios extra
- Las comillas están bien puestas

### 4. Guarda ambos archivos
- Guarda `index.html`
- Guarda `pantalla.html`

✅ **¡Archivos configurados!**

---

## 📋 PASO 7: Subir a GitHub (3 minutos)

### 1. Verifica los nombres de archivo
Asegúrate de que tus archivos se llamen exactamente:
- `index.html`
- `pantalla.html`

### 2. Subir a GitHub

1. Ve a tu repositorio en GitHub
2. **Reemplaza** los archivos con las nuevas versiones que contienen la configuración de Firebase
3. Sube o verifica que esté `codigos.json` (si lo usas)
4. Haz clic en **Commit changes**

✅ **¡Archivos subidos!**

---

## 📋 PASO 8: ¡PROBAR! (2 minutos)

### 1. Abre tu página de estudiantes
```
https://tu-usuario.github.io/tu-repositorio/
```

### 2. Verás arriba:
```
🟢 Conectado a la nube
```

### 3. Introduce un código de prueba
- Introduce uno de tus códigos
- Haz clic en "Añadir Oxígeno"

### 4. Abre la pantalla en OTRA pestaña
```
https://tu-usuario.github.io/tu-repositorio/pantalla.html
```

### 5. ¡Verás los puntos!
- Se actualiza automáticamente
- En tiempo real
- Sin recargar la página

### 6. Prueba desde otro navegador
- Abre Chrome
- Abre Safari  
- ¡Los puntos están ahí!

### 7. Cierra todo y vuelve a abrir
- Cierra todas las pestañas
- Abre de nuevo al día siguiente
- ¡Los puntos siguen ahí!

✅ **¡FUNCIONA!** 🎉

---

## 🔍 VERIFICAR QUE TODO FUNCIONA

**Checklist:**

- [ ] Arriba dice: "🟢 Conectado a la nube"
- [ ] Puedo introducir códigos
- [ ] Los puntos se guardan
- [ ] En pantalla veo los puntos actualizados
- [ ] Si cierro y vuelvo a abrir, los puntos siguen ahí
- [ ] Funciona en diferentes navegadores

---

## 🆘 SOLUCIÓN DE PROBLEMAS

### Problema 1: Dice "Firebase no configurado"

**Causa:** No copiaste bien la configuración

**Solución:**
1. Verifica que hayas reemplazado TODOS los valores
2. Asegúrate de que no queden valores de ejemplo
3. Revisa que las comillas estén bien puestas

### Problema 2: Dice "🔴 Sin conexión"

**Causa:** Las reglas de Firebase no están bien configuradas

**Solución:**
1. Ve a Firebase Console
2. **Realtime Database** → **Reglas**
3. Asegúrate de que diga:
```json
{
  "rules": {
    ".read": true,
    ".write": true
  }
}
```
4. Haz clic en **Publicar**

### Problema 3: Los datos no se guardan

**Causa:** La URL de la base de datos es incorrecta

**Solución:**
1. Ve a Firebase Console
2. **Realtime Database**
3. Arriba verás la URL (algo como: `https://breath-xxxxx.firebaseio.com`)
4. Verifica que sea la misma que copiaste en `databaseURL`

### Problema 4: Funciona en 1 PC pero no en otros

**Causa:** El otro dispositivo tiene la versión antigua en caché

**Solución:** En el dispositivo que falla, haz una recarga forzada:
- **Windows/Linux:** `Ctrl + Shift + R`
- **Mac:** `Cmd + Shift + R`  
- O borra la caché del navegador

---

## 📊 VER DATOS EN FIREBASE

Para ver tus datos en tiempo real:

1. Ve a **Firebase Console**
2. **Realtime Database**
3. Pestaña **"Datos"**
4. Verás la estructura con los puntos de los cursos y códigos usados

```
breathData/
  ├── courses/
  │   ├── 3º ESO A: 10
  │   ├── 3º ESO B: 0
  │   └── ...
  ├── totalPoints: 10
  └── usedCodes/
      └── 0: "CODIGO-EJEMPLO"
```

¡Puedes ver en tiempo real cómo se actualizan cuando usas códigos!

---

## 💡 VENTAJAS DE FIREBASE

✅ **Gratis:** Hasta 10GB de datos y 100K conexiones simultáneas
✅ **Tiempo real:** Las pantallas se actualizan solas
✅ **Persiste:** Los datos nunca se pierden
✅ **Multi-dispositivo:** Funciona en todos los navegadores
✅ **Profesional:** Usado por millones de apps

---

## 🎉 ¡LISTO!

Ahora tienes un sistema profesional que:
- Guarda datos en la nube
- Actualiza en tiempo real
- Funciona desde cualquier lugar
- NUNCA pierde datos

**¡Disfruta de Breath!** 🌬️💨

---

## 📞 ¿Necesitas ayuda?

Si algo no funciona:
1. Revisa esta guía paso a paso
2. Verifica la sección "Solución de problemas"
3. Asegúrate de haber copiado bien la configuración de Firebase

---

**Tiempo total:** 10-15 minutos  
**Dificultad:** Fácil (copiar/pegar)  
**Coste:** $0.00 (Gratis para siempre)

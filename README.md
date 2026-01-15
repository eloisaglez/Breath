# 🌬️ BREATHE - Mars Colony 2056

## 🚀 Proyecto de Gamificación Educativa

Sistema de gamificación para estudiantes de 3º ESO que simula la supervivencia de una colonia en Marte. Los estudiantes ganan puntos de oxígeno completando tareas en diferentes asignaturas (Física y Química, Matemáticas, Biología y Tecnología).

---

## 📊 Características Principales

✅ **1,350 códigos únicos** generados automáticamente
✅ **Sistema de normalización** para competición justa entre clases
✅ **Distribución por asignaturas** (F&Q, Mates, Bio, Tec)
✅ **Tiempo real** - Actualización automática cada 3 segundos
✅ **Firebase** - Datos en la nube, nunca se pierden
✅ **Visualización épica** - Tanques de oxígeno con porcentajes decimales

---

## 🎯 Estructura del Proyecto

### Para Profesores:
```
📂 codigos_por_asignatura/
  ├── FyQ_3_ESO_A.txt  (Física y Química - 3º ESO A)
  ├── MAT_3_ESO_A.txt  (Matemáticas - 3º ESO A)
  ├── BIO_3_ESO_A.txt  (Biología - 3º ESO A)
  ├── TEC_3_ESO_A.txt  (Tecnología - 3º ESO A)
  └── ... (×6 clases = 24 archivos)
```

### Para Alumnos:
```
index_FINAL_v2.html → Interfaz para introducir códigos
```

### Para Visualización:
```
pantalla_normalizada_FINAL.html → Pantalla de competición
```

### Scripts Python:
```
generar_codigos.py    → Genera los 1,350 códigos
subir_firebase.py     → Sube códigos a Firebase
resetear_firebase.py  → Resetea todo (para pruebas)
```

---

## 🎓 Distribución de Actividades

| Asignatura | Actividades | Códigos por Clase (7 grupos) | Códigos por Clase (8 grupos) |
|------------|-------------|------------------------------|------------------------------|
| **Física y Química** | 2 (Act. 1-2) | 42 códigos | 48 códigos |
| **Matemáticas** | 2 (Act. 3-4) | 42 códigos | 48 códigos |
| **Biología** | 2 (Act. 5-6) | 42 códigos | 48 códigos |
| **Tecnología** | 4 (Act. 7-10) | 84 códigos | 96 códigos |

**Clases:**
- 3º ESO A, B, F: 7 grupos cada una
- 3º ESO C, D, E: 8 grupos cada una

---

## 🔧 Instalación y Uso

### PASO 1: Generar Códigos

```bash
python generar_codigos.py
```

**Genera:**
- `codigos_firebase_XXXXXXXX.json` → Para Firebase
- Carpeta `codigos_por_asignatura/` → Para profesores (24 archivos TXT)
- Carpeta `codigos_por_grupo/` → Opcional (45 archivos individuales)

---

### PASO 2: Subir a Firebase

**Opción A - Manual:**
1. Firebase Console → Realtime Database → Datos
2. ⋮ → "Importar JSON"
3. Seleccionar `codigos_firebase_XXXXXXXX.json`
4. Importar

**Opción B - Automático:**
```bash
pip install firebase-admin
python subir_firebase.py
```

---

### PASO 3: Distribuir Códigos a Profesores

Imprime y entrega los archivos de `codigos_por_asignatura/`:

**Profesor de Física y Química recibe:**
- `FyQ_3_ESO_A.txt` hasta `FyQ_3_ESO_F.txt` (6 archivos)

**Profesor de Matemáticas recibe:**
- `MAT_3_ESO_A.txt` hasta `MAT_3_ESO_F.txt` (6 archivos)

Y así sucesivamente.

---

### PASO 4: Abrir Interfaces

**Para Alumnos:**
```
Abre: index_FINAL_v2.html
```
Los alumnos:
1. Seleccionan su clase
2. Introducen el código que les dio el profesor
3. ¡Ganan puntos!

**Para Visualización:**
```
Abre: pantalla_normalizada_FINAL.html
```
Proyecta en clase para ver la competición en tiempo real.

---

## 🎮 Cómo Funciona

### En Clase:

1. **Grupo termina una actividad** (ej: Actividad 1 de F&Q)
2. **Profesor evalúa la calidad:**
   - Regular → Da código de 1 punto
   - Bien → Da código de 2 puntos  
   - Excelente → Da código de 3 puntos
3. **Grupo introduce el código** en su navegador
4. **Tanque de su clase sube** en la pantalla proyectada
5. **Sistema aplica normalización** automáticamente

---

## 📐 Sistema de Normalización

**Problema:** Clases con 7 grupos vs clases con 8 grupos (desventaja del 14.3%)

**Solución:** Normalización automática
- Clases de 7 grupos: puntos × 1.143
- Clases de 8 grupos: puntos × 1.0

**Resultado:** Todas las clases pueden alcanzar 240 puntos (100% de oxígeno)

**Transparente:** Los alumnos NO ven la normalización, solo ven sus puntos reales.

---

## 🔒 Reglas de Seguridad Firebase

### Durante el Proyecto:
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

**Protege contra:** Reutilización de códigos (trampa más común)

---

## 🔄 Resetear Entre Pruebas

```bash
python resetear_firebase.py
```

**Hace:**
1. ✅ Backup automático
2. ✅ Borra todos los datos
3. ✅ Sube códigos frescos (sin usar)
4. ✅ Pone puntos en 0

---

## 📊 Estructura en Firebase

```
breath-8f51d-default-rtdb/
├── validCodes/
│   ├── ABC12345 {clase, grupo, actividad, puntos, usado}
│   └── ... (1,350 códigos)
├── courses/
│   ├── 3º_ESO_A: 0
│   ├── 3º_ESO_B: 0
│   └── ...
└── usedCodes: []
```

---

## 🎯 Características de la Pantalla

**Cuando NO hay puntos (inicio):**
```
💨 El oxígeno del planeta se agota. ¿Qué clase salvará a la colonia?
🚀 (todas las clases muestran cohetes)
```

**Cuando HAY puntos:**
```
🥇 🥈 🥉 4️⃣ 5️⃣ 6️⃣ (medallas según posición)
Porcentajes con decimales (0.1%, 0.7%, 24.5%)
Actualización en tiempo real cada 3 segundos
```

---

## 💡 Consejos Pedagógicos

✅ **Transparencia:** Explica a los alumnos el sistema de normalización
✅ **Honestidad:** Anima a los profesores a evaluar con criterio
✅ **Motivación:** Proyecta la pantalla durante las clases
✅ **Celebración:** Reconoce el esfuerzo de todas las clases

---

## 📞 Soporte

**Archivos Importantes:**
- `generar_codigos.py` - Genera códigos
- `index_FINAL_v2.html` - Interfaz alumnos  
- `pantalla_normalizada_FINAL.html` - Visualización
- `resetear_firebase.py` - Reseteo rápido

**Firebase Console:** https://console.firebase.google.com/

---

## 🎉 ¡Que Comience la Misión!

**La supervivencia de la colonia de Marte está en manos de 3º ESO.** 🚀

---

*Proyecto BREATHE - Mars Colony 2056*  
*IES Diego Velázquez - Torrelodones, Madrid*

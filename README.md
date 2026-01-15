# 🌬️ BREATHE - Mars Colony 2056

Sistema de gamificación educativa para 3º ESO. Los estudiantes ganan puntos de oxígeno completando tareas en Física y Química, Matemáticas, Biología y Tecnología.

---

## 🚀 Inicio Rápido

### 1. Generar Códigos
```bash
python generar_codigos.py
```
Genera 1,350 códigos únicos en `codigos_firebase_XXXXXXXX.json` y archivos TXT por asignatura.

### 2. Subir a Firebase
```bash
python subir_firebase.py
```
O importar manualmente: Firebase Console → Realtime Database → Importar JSON

### 3. Abrir Interfaces
- **Alumnos:** `index_FINAL_v2.html`
- **Pantalla:** `pantalla_normalizada_FINAL.html`

### 4. Distribuir Códigos
Entregar archivos de `codigos_por_asignatura/` a cada profesor.

---

## 📂 Estructura

```
📄 index_FINAL_v2.html              → Interfaz alumnos
📄 pantalla_normalizada_FINAL.html  → Visualización
🐍 generar_codigos.py               → Genera códigos
🐍 subir_firebase.py                → Sube a Firebase
🐍 resetear_firebase.py             → Resetea todo
📂 codigos_por_asignatura/          → 24 archivos para profesores
📊 codigos_firebase_XXXXXXXX.json   → Para importar a Firebase
```

---

## 🎓 Distribución de Actividades

| Asignatura | Actividades |
|------------|-------------|
| Física y Química | 2 (Act. 1-2) |
| Matemáticas | 2 (Act. 3-4) |
| Biología | 2 (Act. 5-6) |
| Tecnología | 4 (Act. 7-10) |

**Clases:** 3º ESO A, B, C, D, E, F  
**Grupos:** A, B, F = 7 grupos | C, D, E = 8 grupos  
**Total:** 1,350 códigos (45 grupos × 10 actividades × 3 niveles)

---

## 📐 Sistema de Normalización

**Problema:** Clases con diferente número de grupos (7 vs 8)  
**Solución:** Multiplicador automático (7 grupos × 1.143 | 8 grupos × 1.0)  
**Resultado:** Todas las clases pueden alcanzar 240 puntos

---

## 🔄 Resetear

```bash
python resetear_firebase.py
```
Vuelve todo a 0 con códigos frescos.

---

## 🔒 Reglas Firebase

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

Impide reutilizar códigos ya usados.

---

## 📚 Documentación Completa

- **GUIA_FIREBASE_COMPLETA.md** - Configuración de Firebase
- **MANUAL_PROFESORES.md** - Para profesores participantes

---

**IES Diego Velázquez - Torrelodones, Madrid**

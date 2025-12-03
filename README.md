# 🌬️ Breathe - Sistema de Gamificación Educativa

## 📖 ¿Qué es Breathe?

**Breathe** es un sistema de gamificación educativa que visualiza el progreso de los estudiantes mediante tanques de oxígeno que se van llenando conforme ganan puntos en clase. Es una herramienta motivadora y visualmente atractiva para fomentar la participación y el esfuerzo en el aula.

## ✨ Características

- 🎮 **Gamificación visual**: Los alumnos ven su progreso representado en tanques de oxígeno
- ⚡ **Tiempo real**: Las actualizaciones se reflejan instantáneamente en la pantalla de proyección
- 🌐 **En la nube**: Los datos se guardan en Firebase, sin riesgo de pérdida
- 📱 **Multiplataforma**: Funciona en cualquier navegador (PC, tablet, proyector)
- 🎯 **Códigos únicos**: Sistema de códigos secretos para asignar puntos a cursos específicos
- 🆓 **100% Gratis**: Sin costes, utilizando Firebase en modo gratuito

## 🎯 ¿Cómo funciona?

### Para el profesor:

1. **Página de control** (`index.html`): 
   - Introduce el código secreto de tu curso
   - Añade puntos cuando los alumnos lo merecen
   - Los puntos se guardan automáticamente en la nube

### Para la visualización en clase:

2. **Pantalla de proyección** (`pantalla.html`):
   - Muestra los tanques de oxígeno de cada curso
   - Se actualiza en tiempo real cuando añades puntos
   - Perfecto para proyectar en clase y motivar a los alumnos

## 🚀 Estructura del proyecto

```
breathe/
├── index.html                    # Página para que los alumnos introduzcan códigos
├── pantalla.html                 # Pantalla de visualización para proyectar
├── generar-codigos.html          # Herramienta offline para generar códigos
├── panel-profesor.html           # 🚧 Panel online (en desarrollo - Fase 2)
├── codigos.json                  # Base de datos de códigos válidos
└── CONFIGURACION-FIREBASE.md     # Guía de instalación
```

## 💻 Uso

### 🔑 Sistema de códigos secretos:

Los alumnos **NO ven** la lista de códigos. Tú decides cuándo y cómo entregarlos:
- 📄 **Físico**: Tarjetas impresas, post-its, fichas
- 📧 **Digital**: Email, Google Classroom, Moodle
- 🎯 **En clase**: Proyectado, dictado, premio por tarea completada
- 🎁 **Oculto**: Dentro de un ejercicio resuelto, como recompensa

### Como profesor:

#### **Generar códigos (offline):**
1. Abre `generar-codigos.html` en tu ordenador
2. Crea códigos con descripción y puntos (5-50 pts)
3. Descarga el archivo `codigos.json`
4. Sube `codigos.json` a GitHub
5. Distribuye los códigos como prefieras (papel, digital, etc.)

#### **🚧 Panel de profesor online (Fase 2 - En desarrollo):**
En el futuro podrás:
- Generar códigos desde cualquier dispositivo
- Ver códigos usados en tiempo real
- Añadir/eliminar códigos sobre la marcha
- Todo automático, sin descargar/subir archivos

### Para los alumnos:

1. Abren la página (`index.html`)
2. Seleccionan su curso
3. Introducen el código que les diste
4. ¡Ganan puntos de oxígeno!

### Para proyectar en clase:

1. Abre `pantalla.html` en el ordenador conectado al proyector
2. Los alumnos verán los tanques de oxígeno llenarse en tiempo real
3. Modo pantalla completa (F11) para mejor visualización

## 🔧 Instalación

Para instalar y configurar Breath en tu propio entorno, consulta la guía completa:

📋 **[Ver guía de configuración de Firebase](CONFIGUARACION-FIREBASE.md)**

La configuración toma aproximadamente 10-15 minutos y es completamente gratuita.

## 🎓 Aplicación educativa

Breath es ideal para:

- ✅ Fomentar la participación activa en clase
- ✅ Motivar el trabajo en equipo entre cursos
- ✅ Crear competencias sanas entre grupos
- ✅ Reconocer el esfuerzo y los logros
- ✅ Hacer el aprendizaje más visual y divertido

---

## 🔧 Herramientas para Profesores

### 📊 Fase Actual: Sistema Offline + Firebase

**Generador de Códigos** (`generar-codigos.html`)
- ✅ Funciona sin internet (offline)
- ✅ Crea códigos únicos instantáneamente
- ✅ Asigna valor en puntos (5-50 puntos)
- ✅ Añade descripción de la tarea
- ✅ Genera múltiples códigos a la vez
- ✅ Descarga `codigos.json` para subir a GitHub
- ✅ Puede cargar y editar códigos existentes

**Flujo actual:**
```
Profesor (offline) → Genera códigos → Descarga JSON → Sube a GitHub
                                                            ↓
Alumno → Introduce código → Sistema valida → Firebase guarda puntos
```

### 🚧 Fase 2: Panel de Profesor Automatizado (En desarrollo)

**Panel de Profesor Online** (`panel-profesor.html`)
- 🔜 Acceso con contraseña
- 🔜 Genera códigos desde cualquier dispositivo
- 🔜 Ve códigos activos/usados en tiempo real
- 🔜 Añade/elimina códigos sobre la marcha
- 🔜 Estadísticas de uso
- 🔜 Todo en Firebase (sin archivos JSON manuales)

**Flujo futuro:**
```
Profesor (online) → Panel con contraseña → Crea código → Firebase (automático)
                                                               ↓
Alumno → Introduce código → Sistema valida → Firebase actualiza puntos
```

**Ventajas de la Fase 2:**
- ⚡ Actualizaciones instantáneas
- 🌐 Accesible desde cualquier lugar
- 🔄 Sincronización automática
- 📊 Estadísticas en tiempo real
- 🔒 Seguro y privado (con contraseña)

> **🔑 Importante:** Los alumnos NUNCA ven la lista de códigos en ninguna de las dos fases. Solo introducen los códigos que tú les entregas cuando y como decidas.

---

## 🛠️ Tecnologías utilizadas

- **HTML5/CSS3/JavaScript**: Frontend de la aplicación
- **Firebase Realtime Database**: Almacenamiento en tiempo real en la nube
- **GitHub Pages**: Hosting gratuito de la aplicación

## 📝 Notas

- Los códigos son secretos y los distribuye el profesor cuando decide
- Cada código solo se puede usar UNA vez
- Los datos persisten incluso si cierras el navegador
- Puedes tener múltiples cursos funcionando simultáneamente
- Las actualizaciones son instantáneas en todas las pantallas abiertas
- El archivo `generar-codigos.html` NO se sube a GitHub (solo uso local del profesor)

## 🤝 Contribuciones

Este proyecto es de código abierto y cualquier mejora es bienvenida. Si tienes ideas para nuevas funcionalidades o mejoras visuales, no dudes en contribuir.

## 📄 Licencia

Este proyecto es libre de usar para fines educativos.

---

<div align="center">

**Hecho con ❤️ para motivar a los estudiantes**

🌬️ Breath - Respira y aprende 💨

</div>

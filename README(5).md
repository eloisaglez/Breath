# 🌬️ Breath - Sistema de Gamificación Educativa

## 📖 ¿Qué es Breath?

**Breath** es un sistema de gamificación educativa que visualiza el progreso de los estudiantes mediante tanques de oxígeno que se van llenando conforme ganan puntos en clase. Es una herramienta motivadora y visualmente atractiva para fomentar la participación y el esfuerzo en el aula.

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
breath/
├── index.html          # Página de control del profesor
├── pantalla.html       # Pantalla de visualización para proyectar
└── CONFIGURACION-FIREBASE.md  # Guía de instalación
```

## 💻 Uso

### Como profesor:

1. Abre `index.html` en tu navegador
2. Introduce el código secreto de tu curso (ejemplo: `3ESO-A`, `1BACH-B`)
3. Haz clic en "Añadir Oxígeno" para dar puntos a tu curso
4. Los puntos se guardan automáticamente

### Para proyectar en clase:

1. Abre `pantalla.html` en el ordenador conectado al proyector
2. Los alumnos verán los tanques de oxígeno llenarse en tiempo real
3. Cada curso tiene su propio tanque identificado por su código

## 🔧 Instalación

Para instalar y configurar Breath en tu propio entorno, consulta la guía completa:

📋 **[Ver guía de configuración de Firebase](CONFIGURACION-FIREBASE.md)**

La configuración toma aproximadamente 10-15 minutos y es completamente gratuita.

## 🎓 Aplicación educativa

Breath es ideal para:

- ✅ Fomentar la participación activa en clase
- ✅ Motivar el trabajo en equipo entre cursos
- ✅ Crear competencias sanas entre grupos
- ✅ Reconocer el esfuerzo y los logros
- ✅ Hacer el aprendizaje más visual y divertido

## 🛠️ Tecnologías utilizadas

- **HTML5/CSS3/JavaScript**: Frontend de la aplicación
- **Firebase Realtime Database**: Almacenamiento en tiempo real en la nube
- **GitHub Pages**: Hosting gratuito de la aplicación

## 📝 Notas

- Los códigos de curso son secretos y solo los conoce el profesor
- Los datos persisten incluso si cierras el navegador
- Puedes tener múltiples cursos funcionando simultáneamente
- Las actualizaciones son instantáneas en todas las pantallas abiertas

## 🤝 Contribuciones

Este proyecto es de código abierto y cualquier mejora es bienvenida. Si tienes ideas para nuevas funcionalidades o mejoras visuales, no dudes en contribuir.

## 📄 Licencia

Este proyecto es libre de usar para fines educativos.

---

<div align="center">

**Hecho con ❤️ para motivar a los estudiantes**

🌬️ Breath - Respira y aprende 💨

</div>

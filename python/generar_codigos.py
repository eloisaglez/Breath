"""
Sistema de Generación de Códigos BREATHE - Mars Colony
=======================================================

Este script genera códigos únicos para validar actividades del proyecto BREATHE.

CONFIGURACIÓN:
- 10 actividades por grupo DISTRIBUIDAS POR ASIGNATURAS:
  * Física y Química: 2 actividades (Act. 1-2)
  * Matemáticas: 2 actividades (Act. 3-4)
  * Biología: 2 actividades (Act. 5-6)
  * Tecnología: 4 actividades (Act. 7-10)
- Cada grupo hace las 10 actividades
- 3 niveles de puntuación por actividad:
  * 1 punto: tarea regular
  * 2 puntos: tarea bien hecha
  * 3 puntos: tarea excelente (100%)
- 6 clases de 3º ESO (A, B, C, D, E, F)
- Clases A, B, F: 7 grupos cada una (21 grupos)
- Clases C, D, E: 8 grupos cada una (24 grupos)
- Total: 45 grupos

IMPORTANTE - SISTEMA DE NORMALIZACIÓN:
El sistema aplica automáticamente un factor de corrección para que las clases
con 7 grupos no estén en desventaja frente a las de 8 grupos.

Factor aplicado:
- Clases de 7 grupos (A, B, F): puntos × 1.143 (8/7)
- Clases de 8 grupos (C, D, E): puntos × 1.0 (sin cambio)

Este ajuste es INVISIBLE para los alumnos. Todos ven los mismos valores de código
(1, 2 o 3 puntos), pero el sistema equilibra automáticamente en el backend.

TOTAL DE CÓDIGOS GENERADOS: 1,350 códigos únicos
(45 grupos × 10 actividades × 3 niveles)
"""

import random
import string
from datetime import datetime

# Configuración
ACTIVIDADES = 10
NIVELES = [1, 2, 3]  # puntos por nivel
CLASES = {
    '3º ESO A': 7,
    '3º ESO B': 7,
    '3º ESO C': 8,
    '3º ESO D': 8,
    '3º ESO E': 8,
    '3º ESO F': 7
}

# Distribución de actividades por asignatura
ASIGNATURAS = {
    'Física y Química': {
        'actividades': [1, 2],
        'abreviatura': 'FyQ'
    },
    'Matemáticas': {
        'actividades': [3, 4],
        'abreviatura': 'MAT'
    },
    'Biología': {
        'actividades': [5, 6],
        'abreviatura': 'BIO'
    },
    'Tecnología': {
        'actividades': [7, 8, 9, 10],
        'abreviatura': 'TEC'
    }
}

def generar_codigo_unico(longitud=8):
    """Genera un código alfanumérico único de 8 caracteres"""
    caracteres = string.ascii_uppercase + string.digits
    # Excluimos algunos caracteres que se pueden confundir
    caracteres = caracteres.replace('O', '').replace('0', '').replace('I', '').replace('1', '')
    return ''.join(random.choice(caracteres) for _ in range(longitud))

def generar_todos_los_codigos():
    """Genera todos los códigos necesarios para el sistema"""
    codigos_generados = set()
    codigos_por_clase = {}
    
    for clase, num_grupos in CLASES.items():
        codigos_por_clase[clase] = {}
        
        for grupo in range(1, num_grupos + 1):
            nombre_grupo = f'Grupo_{grupo}'
            codigos_por_clase[clase][nombre_grupo] = {}
            
            for actividad in range(1, ACTIVIDADES + 1):
                codigos_por_clase[clase][nombre_grupo][f'Actividad_{actividad}'] = {}
                
                for nivel in NIVELES:
                    # Generar código único
                    while True:
                        codigo = generar_codigo_unico()
                        if codigo not in codigos_generados:
                            codigos_generados.add(codigo)
                            break
                    
                    codigos_por_clase[clase][nombre_grupo][f'Actividad_{actividad}'][f'{nivel}_puntos'] = codigo
    
    return codigos_por_clase

def guardar_codigos_txt(codigos):
    """Guarda los códigos en un archivo de texto legible"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f'codigos_breathe_{timestamp}.txt'
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("=" * 80 + "\n")
        f.write("CÓDIGOS BREATHE - MARS COLONY 2056\n")
        f.write("Sistema de Validación de Actividades\n")
        f.write("=" * 80 + "\n\n")
        
        f.write("IMPORTANTE - NORMALIZACIÓN AUTOMÁTICA:\n")
        f.write("Las clases con 7 grupos (A, B, F) tienen sus puntos multiplicados por 1.143\n")
        f.write("Las clases con 8 grupos (C, D, E) mantienen sus puntos sin cambios\n")
        f.write("Este ajuste es automático e invisible para los alumnos.\n")
        f.write("Todos los códigos valen visualmente 1, 2 o 3 puntos.\n\n")
        
        f.write("ESTRUCTURA:\n")
        f.write("- Cada GRUPO hace 10 actividades\n")
        f.write("- Cada actividad puede conseguir 1, 2 o 3 puntos\n")
        f.write("- Máximo por grupo: 30 puntos\n")
        f.write("- Cada código solo puede usarse UNA vez\n\n")
        
        f.write("=" * 80 + "\n\n")
        
        for clase, grupos in codigos.items():
            f.write(f"\n{'=' * 80}\n")
            f.write(f"CLASE: {clase} ({CLASES[clase]} grupos)\n")
            f.write(f"{'=' * 80}\n\n")
            
            for grupo, actividades in grupos.items():
                f.write(f"  {grupo}:\n")
                f.write(f"  {'-' * 60}\n")
                
                for actividad, niveles in actividades.items():
                    f.write(f"    {actividad}:\n")
                    for nivel, codigo in niveles.items():
                        f.write(f"      {nivel}: {codigo}\n")
                f.write("\n")
    
    print(f"✓ Códigos guardados en: {filename}")
    return filename

def guardar_codigos_por_clase(codigos):
    """Guarda un archivo separado para cada clase con sus grupos (para imprimir)"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    for clase, grupos in codigos.items():
        clase_limpia = clase.replace('º', '').replace(' ', '_')
        filename = f'codigos_{clase_limpia}_{timestamp}.txt'
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("=" * 70 + "\n")
            f.write(f"BREATHE - CÓDIGOS PARA {clase}\n")
            f.write(f"Total de grupos: {CLASES[clase]}\n")
            f.write("=" * 70 + "\n\n")
            
            f.write("INSTRUCCIONES:\n")
            f.write("1. Cada GRUPO tiene sus propios códigos para 10 actividades\n")
            f.write("2. Cada actividad tiene 3 códigos posibles según calidad:\n")
            f.write("   • 1 punto: trabajo regular/básico\n")
            f.write("   • 2 puntos: trabajo bien hecho\n")
            f.write("   • 3 puntos: trabajo excelente (100%)\n")
            f.write("3. Cada código solo puede usarse UNA VEZ\n")
            f.write("4. El grupo introduce el código en el sistema BREATHE\n")
            f.write("5. Máximo por grupo: 30 puntos (10 actividades × 3 puntos)\n\n")
            
            f.write("=" * 70 + "\n\n")
            
            for grupo, actividades in grupos.items():
                f.write(f"\n{'*' * 70}\n")
                f.write(f"{grupo.upper()}\n")
                f.write(f"{'*' * 70}\n\n")
                
                for actividad, niveles in actividades.items():
                    f.write(f"  {actividad}:\n")
                    f.write("  " + "-" * 50 + "\n")
                    for nivel, codigo in niveles.items():
                        f.write(f"    {nivel:12} → {codigo}\n")
                    f.write("\n")
        
        print(f"✓ Archivo para {clase}: {filename}")

def guardar_codigos_por_grupo(codigos):
    """Guarda un archivo individual para cada grupo (opcional)"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    import os
    os.makedirs('codigos_por_grupo', exist_ok=True)
    
    for clase, grupos in codigos.items():
        clase_limpia = clase.replace('º', '').replace(' ', '_')
        
        for grupo, actividades in grupos.items():
            grupo_limpio = grupo.replace(' ', '_')
            filename = f'codigos_por_grupo/{clase_limpia}_{grupo_limpio}_{timestamp}.txt'
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("=" * 60 + "\n")
                f.write(f"BREATHE - {clase} - {grupo}\n")
                f.write("=" * 60 + "\n\n")
                
                f.write("TUS CÓDIGOS PARA LAS 10 ACTIVIDADES:\n\n")
                
                for actividad, niveles in actividades.items():
                    f.write(f"{actividad}:\n")
                    f.write("-" * 40 + "\n")
                    for nivel, codigo in niveles.items():
                        f.write(f"  {nivel:12} → {codigo}\n")
                    f.write("\n")
                
                f.write("\n" + "=" * 60 + "\n")
                f.write("RECUERDA:\n")
                f.write("- Cada código solo se puede usar UNA vez\n")
                f.write("- Elige el código según la calidad de tu trabajo\n")
                f.write("- Máximo: 30 puntos (10 actividades × 3 puntos)\n")
    
    print(f"✓ Archivos individuales por grupo creados en: codigos_por_grupo/")

def generar_json_firebase(codigos):
    """Genera estructura JSON para importar a Firebase (opcional)"""
    import json
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f'codigos_firebase_{timestamp}.json'
    
    # Estructura para Firebase
    firebase_data = {
        "validCodes": {}
    }
    
    for clase, grupos in codigos.items():
        for grupo, actividades in grupos.items():
            for actividad, niveles in actividades.items():
                for nivel, codigo in niveles.items():
                    puntos = int(nivel.split('_')[0])
                    firebase_data["validCodes"][codigo] = {
                        "clase": clase,
                        "grupo": grupo,
                        "actividad": actividad,
                        "puntos": puntos,
                        "usado": False
                    }
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(firebase_data, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Archivo JSON para Firebase: {filename}")
    return filename

def guardar_codigos_por_asignatura(codigos):
    """Guarda archivos separados por asignatura y clase para cada profesor"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    import os
    os.makedirs('codigos_por_asignatura', exist_ok=True)
    
    for asignatura, info in ASIGNATURAS.items():
        actividades_asignatura = info['actividades']
        abrev = info['abreviatura']
        
        # Archivo por cada asignatura y clase
        for clase, num_grupos in CLASES.items():
            clase_limpia = clase.replace('º', '').replace(' ', '_')
            filename = f'codigos_por_asignatura/{abrev}_{clase_limpia}_{timestamp}.txt'
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("=" * 80 + "\n")
                f.write(f"BREATHE - CÓDIGOS PARA {asignatura.upper()}\n")
                f.write(f"Clase: {clase} ({num_grupos} grupos)\n")
                f.write(f"Actividades: {len(actividades_asignatura)} ({', '.join(map(str, actividades_asignatura))})\n")
                f.write("=" * 80 + "\n\n")
                
                f.write("INSTRUCCIONES PARA EL PROFESOR:\n")
                f.write(f"- Tienes {len(actividades_asignatura)} actividades para evaluar\n")
                f.write(f"- Cada grupo realizará estas {len(actividades_asignatura)} actividades\n")
                f.write("- Según la calidad del trabajo, darás un código:\n")
                f.write("  • 1 punto: trabajo regular/básico\n")
                f.write("  • 2 puntos: trabajo bien hecho\n")
                f.write("  • 3 puntos: trabajo excelente (100%)\n")
                f.write("- El grupo introducirá el código en el sistema BREATHE\n")
                f.write("- Cada código solo puede usarse UNA vez\n\n")
                
                f.write("=" * 80 + "\n\n")
                
                # Organizar códigos por actividad y luego por grupo
                for actividad_num in actividades_asignatura:
                    f.write(f"\n{'*' * 80}\n")
                    f.write(f"ACTIVIDAD {actividad_num}\n")
                    f.write(f"{'*' * 80}\n\n")
                    
                    grupos = codigos[clase]
                    for grupo_nombre in sorted(grupos.keys()):
                        actividad_key = f'Actividad_{actividad_num}'
                        if actividad_key in grupos[grupo_nombre]:
                            f.write(f"  {grupo_nombre}:\n")
                            f.write("  " + "-" * 60 + "\n")
                            
                            niveles = grupos[grupo_nombre][actividad_key]
                            for nivel, codigo in niveles.items():
                                f.write(f"    {nivel:12} → {codigo}\n")
                            f.write("\n")
            
            print(f"✓ {asignatura} - {clase}: {filename}")
    
    print(f"\n✓ Archivos por asignatura creados en: codigos_por_asignatura/")
    print(f"  Total: {len(ASIGNATURAS)} asignaturas × {len(CLASES)} clases = {len(ASIGNATURAS) * len(CLASES)} archivos")

def mostrar_resumen(codigos):
    """Muestra un resumen de los códigos generados"""
    print("\n" + "=" * 80)
    print("RESUMEN DE GENERACIÓN DE CÓDIGOS")
    print("=" * 80)
    
    total_codigos = 0
    total_grupos = 0
    
    for clase, grupos in codigos.items():
        num_grupos = len(grupos)
        total_grupos += num_grupos
        codigos_clase = sum(len(niveles) for grupo in grupos.values() 
                           for niveles in grupo.values())
        total_codigos += codigos_clase
    
    print(f"\nTotal de códigos generados: {total_codigos}")
    print(f"Total de grupos: {total_grupos}")
    print(f"Actividades por grupo: {ACTIVIDADES}")
    print(f"Niveles por actividad: {len(NIVELES)}")
    print(f"Códigos por grupo: {ACTIVIDADES * len(NIVELES)}")
    
    print("\nDistribución por clase:")
    for clase, grupos in codigos.items():
        num_grupos = len(grupos)
        codigos_clase = num_grupos * ACTIVIDADES * len(NIVELES)
        print(f"  {clase}: {num_grupos} grupos × 30 códigos = {codigos_clase} códigos")
    
    print("\nPuntuación máxima por clase:")
    for clase, num_grupos in CLASES.items():
        max_puntos = num_grupos * ACTIVIDADES * 3
        print(f"  {clase}: {num_grupos} grupos × 30 pts = {max_puntos} puntos")
    
    print("\n" + "=" * 80)

if __name__ == "__main__":
    print("Generando códigos BREATHE...")
    print("=" * 80 + "\n")
    
    # Generar todos los códigos
    codigos = generar_todos_los_codigos()
    
    # Guardar en diferentes formatos
    print("\n1. Generando archivo maestro...")
    guardar_codigos_txt(codigos)
    
    print("\n2. Generando archivos por clase...")
    guardar_codigos_por_clase(codigos)
    
    print("\n3. Generando archivos individuales por grupo...")
    guardar_codigos_por_grupo(codigos)
    
    print("\n4. Generando archivos por ASIGNATURA (para profesores)...")
    guardar_codigos_por_asignatura(codigos)
    
    print("\n5. Generando JSON para Firebase...")
    generar_json_firebase(codigos)
    
    # Mostrar resumen
    mostrar_resumen(codigos)
    
    print("\n✓ Generación completada exitosamente!")
    print("\n" + "=" * 80)
    print("ARCHIVOS GENERADOS:")
    print("=" * 80)
    print("\n📁 ARCHIVOS PRINCIPALES:")
    print("  1. codigos_breathe_XXXXXXXX.txt")
    print("     → Archivo maestro con TODOS los códigos organizados\n")
    
    print("📁 POR CLASE (para distribuir a las clases):")
    print("  2. codigos_3_ESO_X_XXXXXXXX.txt (6 archivos)")
    print("     → Un archivo por cada clase con todos sus grupos\n")
    
    print("📁 POR GRUPO (para dar a cada grupo su hoja):")
    print("  3. codigos_por_grupo/ (45 archivos)")
    print("     → Cada grupo tiene su propio archivo con sus 10 actividades\n")
    
    print("📁 POR ASIGNATURA (para cada profesor):")
    print("  4. codigos_por_asignatura/ (24 archivos)")
    print("     → Física y Química: 6 archivos (uno por clase)")
    print("     → Matemáticas: 6 archivos (uno por clase)")
    print("     → Biología: 6 archivos (uno por clase)")
    print("     → Tecnología: 6 archivos (uno por clase)")
    print("     Cada profesor recibe solo sus actividades\n")
    
    print("📁 FIREBASE:")
    print("  5. codigos_firebase_XXXXXXXX.json")
    print("     → Para importar a Firebase\n")
    
    print("=" * 80)
    print("\n💡 RECOMENDACIÓN DE USO:")
    print("   • Carpeta 'codigos_por_asignatura/' → Dar a cada PROFESOR")
    print("   • Cada profesor gestiona sus códigos para sus actividades")
    print("   • Los profesores pueden llevar los códigos a clase y darlos")
    print("     según evalúen el trabajo de cada grupo")
    print("=" * 80)

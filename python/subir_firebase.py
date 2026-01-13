"""
Script para SUBIR códigos directamente a Firebase
==================================================

Este script carga los códigos generados directamente a Firebase
sin necesidad de importar JSON manualmente.

REQUISITOS:
pip install firebase-admin

ANTES DE EJECUTAR:
1. Descarga tu archivo de credenciales de Firebase
2. Ve a: Firebase Console → Configuración del proyecto → Cuentas de servicio
3. Clic en "Generar nueva clave privada"
4. Guarda el archivo como 'firebase-credentials.json' en este directorio
"""

import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import sys

def inicializar_firebase():
    """Inicializa la conexión a Firebase"""
    try:
        # Intenta usar el archivo de credenciales
        cred = credentials.Certificate('firebase-credentials.json')
        
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://breath-8f51d-default-rtdb.firebaseio.com'
        })
        print("✓ Conexión a Firebase establecida")
        return True
    except FileNotFoundError:
        print("❌ ERROR: No se encuentra 'firebase-credentials.json'")
        print("\nPasos para obtenerlo:")
        print("1. Ve a: https://console.firebase.google.com/")
        print("2. Selecciona tu proyecto 'breath-8f51d'")
        print("3. Configuración del proyecto → Cuentas de servicio")
        print("4. Clic en 'Generar nueva clave privada'")
        print("5. Guarda el archivo como 'firebase-credentials.json'")
        return False
    except Exception as e:
        print(f"❌ ERROR al conectar: {e}")
        return False

def subir_codigos_a_firebase(archivo_json):
    """Sube los códigos desde el archivo JSON a Firebase"""
    try:
        # Leer el archivo JSON
        with open(archivo_json, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"\n📁 Cargando datos desde: {archivo_json}")
        print(f"   Total de códigos válidos: {len(data.get('validCodes', {}))}")
        
        # Referencia a la base de datos
        ref = db.reference('/')
        
        # Subir datos
        print("\n⬆️  Subiendo a Firebase...")
        
        # Subir códigos válidos
        if 'validCodes' in data:
            codes_ref = ref.child('validCodes')
            codes_ref.set(data['validCodes'])
            print(f"   ✓ {len(data['validCodes'])} códigos válidos subidos")
        
        # Inicializar puntos de clases si no existen
        courses_ref = ref.child('courses')
        existing_courses = courses_ref.get()
        
        if existing_courses is None:
            print("\n   Inicializando puntos de clases...")
            courses_data = {
                '3º_ESO_A': 0,
                '3º_ESO_B': 0,
                '3º_ESO_C': 0,
                '3º_ESO_D': 0,
                '3º_ESO_E': 0,
                '3º_ESO_F': 0
            }
            courses_ref.set(courses_data)
            print("   ✓ Puntos inicializados en 0")
        else:
            print("   ℹ️  Los puntos de clases ya existen, no se sobrescriben")
        
        # Inicializar lista de códigos usados si no existe
        used_codes_ref = ref.child('usedCodes')
        if used_codes_ref.get() is None:
            used_codes_ref.set([])
            print("   ✓ Lista de códigos usados inicializada")
        
        print("\n✅ ¡Datos subidos exitosamente a Firebase!")
        return True
        
    except FileNotFoundError:
        print(f"❌ ERROR: No se encuentra el archivo {archivo_json}")
        print("   Asegúrate de haber ejecutado 'generar_codigos.py' primero")
        return False
    except Exception as e:
        print(f"❌ ERROR al subir datos: {e}")
        return False

def verificar_subida():
    """Verifica que los datos se hayan subido correctamente"""
    try:
        ref = db.reference('/')
        data = ref.get()
        
        print("\n🔍 Verificando datos en Firebase...")
        
        if data:
            valid_codes = data.get('validCodes', {})
            courses = data.get('courses', {})
            used_codes = data.get('usedCodes', [])
            
            print(f"   ✓ Códigos válidos: {len(valid_codes)}")
            print(f"   ✓ Clases configuradas: {len(courses)}")
            print(f"   ✓ Códigos usados: {len(used_codes)}")
            
            # Mostrar puntos actuales
            print("\n   Puntos actuales por clase:")
            for clase, puntos in sorted(courses.items()):
                print(f"      {clase}: {puntos} pts")
            
            return True
        else:
            print("   ⚠️  No se encontraron datos")
            return False
            
    except Exception as e:
        print(f"❌ ERROR al verificar: {e}")
        return False

def limpiar_datos():
    """Función de emergencia para resetear los datos"""
    respuesta = input("\n⚠️  ¿ESTÁS SEGURO que quieres BORRAR todos los datos? (escribe 'SI' para confirmar): ")
    
    if respuesta.strip().upper() == 'SI':
        try:
            ref = db.reference('/')
            ref.delete()
            print("✓ Datos borrados. Ejecuta este script de nuevo para subir datos frescos.")
        except Exception as e:
            print(f"❌ ERROR al borrar: {e}")
    else:
        print("❌ Operación cancelada")

if __name__ == "__main__":
    print("=" * 70)
    print("SUBIR CÓDIGOS BREATHE A FIREBASE")
    print("=" * 70)
    
    # Inicializar Firebase
    if not inicializar_firebase():
        sys.exit(1)
    
    # Buscar el archivo JSON más reciente
    import glob
    import os
    
    json_files = glob.glob('codigos_firebase_*.json')
    
    if not json_files:
        print("\n❌ No se encontró ningún archivo codigos_firebase_*.json")
        print("   Ejecuta 'python generar_codigos.py' primero")
        sys.exit(1)
    
    # Usar el más reciente
    archivo_json = max(json_files, key=os.path.getctime)
    
    # Menú de opciones
    print("\n¿Qué quieres hacer?")
    print("1. Subir códigos a Firebase (recomendado)")
    print("2. Solo verificar datos actuales")
    print("3. RESETEAR todos los datos (peligroso)")
    print("4. Salir")
    
    opcion = input("\nOpción (1-4): ").strip()
    
    if opcion == '1':
        if subir_codigos_a_firebase(archivo_json):
            verificar_subida()
    elif opcion == '2':
        verificar_subida()
    elif opcion == '3':
        limpiar_datos()
    elif opcion == '4':
        print("👋 Saliendo...")
    else:
        print("❌ Opción inválida")
    
    print("\n" + "=" * 70)

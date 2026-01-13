"""
Script para RESETEAR Firebase - Volver a códigos frescos
=========================================================

Este script borra todos los datos de Firebase y sube códigos frescos.
Útil para después de hacer pruebas y querer empezar de cero.

USO:
python resetear_firebase.py

IMPORTANTE: Esto BORRA todos los datos y los reemplaza con códigos sin usar.
"""

import json
import sys

try:
    import firebase_admin
    from firebase_admin import credentials
    from firebase_admin import db
except ImportError:
    print("❌ ERROR: Necesitas instalar firebase-admin")
    print("   Ejecuta: pip install firebase-admin")
    sys.exit(1)

def inicializar_firebase():
    """Inicializa la conexión a Firebase"""
    try:
        # Si ya está inicializado, no hacer nada
        firebase_admin.get_app()
        print("✓ Ya conectado a Firebase")
        return True
    except ValueError:
        # No está inicializado, inicializar ahora
        pass
    
    try:
        cred = credentials.Certificate('firebase-credentials.json')
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://breath-8f51d-default-rtdb.firebaseio.com'
        })
        print("✓ Conexión a Firebase establecida")
        return True
    except FileNotFoundError:
        print("❌ ERROR: No se encuentra 'firebase-credentials.json'")
        print("\nNecesitas las credenciales de Firebase.")
        print("Lee SOLUCION_FIREBASE.md para obtenerlas.")
        return False
    except Exception as e:
        print(f"❌ ERROR al conectar: {e}")
        return False

def hacer_backup():
    """Crea un backup antes de borrar"""
    print("\n📦 Creando backup de seguridad...")
    try:
        ref = db.reference('/')
        data = ref.get()
        
        if data:
            import datetime
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f'backup_firebase_{timestamp}.json'
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            print(f"   ✓ Backup guardado en: {filename}")
            return True
        else:
            print("   ℹ️  No hay datos para hacer backup")
            return True
            
    except Exception as e:
        print(f"   ⚠️  No se pudo hacer backup: {e}")
        respuesta = input("   ¿Continuar sin backup? (si/no): ")
        return respuesta.lower() in ['si', 's', 'yes', 'y']

def borrar_todo():
    """Borra todos los datos de Firebase"""
    print("\n🗑️  Borrando todos los datos...")
    try:
        ref = db.reference('/')
        ref.delete()
        print("   ✓ Datos borrados")
        return True
    except Exception as e:
        print(f"   ❌ ERROR al borrar: {e}")
        return False

def subir_codigos_frescos():
    """Sube códigos frescos sin usar"""
    print("\n⬆️  Subiendo códigos frescos...")
    
    # Buscar archivo JSON más reciente
    import glob
    import os
    
    json_files = glob.glob('codigos_firebase_*.json')
    
    if not json_files:
        print("   ❌ No se encuentra codigos_firebase_*.json")
        print("   Ejecuta 'python generar_codigos.py' primero")
        return False
    
    archivo_json = max(json_files, key=os.path.getctime)
    print(f"   📁 Usando: {archivo_json}")
    
    try:
        with open(archivo_json, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        ref = db.reference('/')
        
        # Subir códigos válidos
        if 'validCodes' in data:
            codes_ref = ref.child('validCodes')
            codes_ref.set(data['validCodes'])
            print(f"   ✓ {len(data['validCodes'])} códigos subidos")
        
        # Inicializar puntos en 0
        courses_data = {
            '3º_ESO_A': 0,
            '3º_ESO_B': 0,
            '3º_ESO_C': 0,
            '3º_ESO_D': 0,
            '3º_ESO_E': 0,
            '3º_ESO_F': 0
        }
        courses_ref = ref.child('courses')
        courses_ref.set(courses_data)
        print("   ✓ Puntos inicializados en 0")
        
        # Lista vacía de códigos usados
        used_codes_ref = ref.child('usedCodes')
        used_codes_ref.set([])
        print("   ✓ Lista de códigos usados limpia")
        
        return True
        
    except Exception as e:
        print(f"   ❌ ERROR: {e}")
        return False

def verificar():
    """Verifica que todo está correcto"""
    print("\n🔍 Verificando...")
    try:
        ref = db.reference('/')
        data = ref.get()
        
        if data:
            valid_codes = data.get('validCodes', {})
            courses = data.get('courses', {})
            used_codes = data.get('usedCodes', [])
            
            print(f"   ✓ Códigos válidos: {len(valid_codes)}")
            print(f"   ✓ Clases: {len(courses)}")
            print(f"   ✓ Códigos usados: {len(used_codes)}")
            
            # Verificar que todos los puntos están en 0
            todos_en_cero = all(puntos == 0 for puntos in courses.values())
            if todos_en_cero:
                print("   ✓ Todos los tanques en 0 puntos")
            else:
                print("   ⚠️  ATENCIÓN: Algunos tanques tienen puntos")
                for clase, puntos in sorted(courses.items()):
                    if puntos != 0:
                        print(f"      {clase}: {puntos} pts")
            
            return True
        else:
            print("   ❌ No hay datos en Firebase")
            return False
            
    except Exception as e:
        print(f"   ❌ ERROR: {e}")
        return False

if __name__ == "__main__":
    print("=" * 70)
    print("RESETEAR FIREBASE - BREATHE")
    print("=" * 70)
    
    print("\n⚠️  ATENCIÓN: Este script va a:")
    print("   1. Crear un backup de tus datos actuales")
    print("   2. BORRAR todos los datos de Firebase")
    print("   3. Subir códigos FRESCOS (sin usar)")
    print("   4. Poner todos los puntos en 0")
    
    respuesta = input("\n¿Estás seguro? (escribe 'SI' para continuar): ")
    
    if respuesta.strip().upper() != 'SI':
        print("\n❌ Operación cancelada")
        sys.exit(0)
    
    # Inicializar Firebase
    if not inicializar_firebase():
        sys.exit(1)
    
    # Proceso de reseteo
    if not hacer_backup():
        print("\n❌ No se pudo hacer backup. Abortando.")
        sys.exit(1)
    
    if not borrar_todo():
        print("\n❌ No se pudo borrar datos. Abortando.")
        sys.exit(1)
    
    if not subir_codigos_frescos():
        print("\n❌ No se pudieron subir códigos. Abortando.")
        sys.exit(1)
    
    if not verificar():
        print("\n⚠️  Verifica manualmente en Firebase Console")
    
    print("\n" + "=" * 70)
    print("✅ ¡RESETEO COMPLETADO!")
    print("=" * 70)
    print("\nTu Firebase ahora tiene:")
    print("  • Códigos frescos sin usar")
    print("  • Todos los puntos en 0")
    print("  • Lista de códigos usados vacía")
    print("\n¡Listo para empezar el juego desde cero!")
    print("=" * 70)

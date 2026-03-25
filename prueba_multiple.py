import pyttsx3
import time

# Configuración inicial
velocidad_actual = 150

def crear_motor_voz():
    """Crear y configurar un nuevo motor de voz"""
    motor = pyttsx3.init()
    motor.setProperty('rate', velocidad_actual)
    motor.setProperty('volume', 0.8)

    # Obtener voces disponibles
    voices = motor.getProperty('voices')
    if len(voices) > 1:
        motor.setProperty('voice', voices[1].id)
    else:
        motor.setProperty('voice', voices[0].id)

    return motor

print("🧪 PRUEBA AUTOMÁTICA - MÚLTIPLES REPRODUCCIONES")
print("=" * 50)

textos_prueba = [
    "Primera reproducción",
    "Segunda reproducción",
    "Tercera reproducción",
    "Cuarta reproducción",
    "Quinta reproducción"
]

for i, texto in enumerate(textos_prueba, 1):
    print(f"\n🔊 Reproduciendo texto {i}: '{texto}' (velocidad: {velocidad_actual})...")

    try:
        # Crear un nuevo motor para cada reproducción
        motor_temp = crear_motor_voz()
        motor_temp.say(texto)
        motor_temp.runAndWait()
        motor_temp.stop()  # Limpiar recursos

        print(f"✅ Texto {i} completado exitosamente!")
    except Exception as e:
        print(f"❌ Error en texto {i}: {e}")

    # Pequeña pausa entre reproducciones
    time.sleep(1)

print("\n🎉 Prueba completada!")
print("Si escuchaste todos los textos, el problema está solucionado.")
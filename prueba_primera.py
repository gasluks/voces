import pyttsx3

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

print("🧪 PRUEBA RÁPIDA - PRIMERA REPRODUCCIÓN")
print("=" * 40)

texto_prueba = "Hola, esta es una prueba de voz"

try:
    print(f"🔊 Reproduciendo: '{texto_prueba}'...")

    # Crear un nuevo motor para la reproducción
    motor_temp = crear_motor_voz()
    motor_temp.say(texto_prueba)
    motor_temp.runAndWait()
    motor_temp.stop()  # Limpiar recursos

    print("✅ Primera reproducción completada exitosamente!")
except Exception as e:
    print(f"❌ Error: {e}")

print("\n🎉 Prueba completada!")
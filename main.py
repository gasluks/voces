import pyttsx3

# Inicializar el motor de síntesis de voz
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Velocidad de voz (75-300)
engine.setProperty('volume', 0.8)  # Volumen (0.0-1.0)

# Obtener voces disponibles
voices = engine.getProperty('voices')

print("\n📋 Voces disponibles:")
for i, voice in enumerate(voices):
    print(f"   {i}: {voice.name} (ID: {voice.id})")

# Buscar una voz en español
voz_española = None
for voice in voices:
    # Buscar voces que contengan "Spanish" en el nombre
    if 'spanish' in voice.name.lower():
        voz_española = voice
        break

# Si no encontramos español por nombre, buscar por idioma
if not voz_española:
    for voice in voices:
        if hasattr(voice, 'languages') and voice.languages:
            if any('es' in str(lang).lower() for lang in voice.languages):
                voz_española = voice
                break

# Si encuentras una voz en español, usarla
if voz_española:
    engine.setProperty('voice', voz_española.id)
    print(f"✅ Usando voz en español: {voz_española.name}\n")
else:
    # Si no hay voz en español, usar la segunda disponible (muchas veces es una voz femenina)
    if len(voices) > 1:
        engine.setProperty('voice', voices[1].id)
        print(f"⚠️  Sin voces en español. Usando: {voices[1].name}\n")
    else:
        engine.setProperty('voice', voices[0].id)
        print(f"⚠️  Sin voces en español. Usando: {voices[0].name}\n")

velocidad_actual = 150

def mostrar_menu():
    print("\n📊 VELOCIDAD DE LECTURA")
    print(f"   Velocidad actual: {velocidad_actual} palabras por minuto")
    print("   Rango válido: 50 - 300 (predeterminado: 150)\n")

def crear_motor_voz():
    """Crear y configurar un nuevo motor de voz"""
    motor = pyttsx3.init()
    motor.setProperty('rate', velocidad_actual)
    motor.setProperty('volume', 0.8)

    # Configurar voz
    if voz_española:
        motor.setProperty('voice', voz_española.id)
    elif len(voices) > 1:
        motor.setProperty('voice', voices[1].id)
    else:
        motor.setProperty('voice', voices[0].id)

    return motor

while True:
    # Pedir entrada del usuario
    texto = input("📝 Escribe (texto/velocidad/salir): ").strip()

    # Verificar si el usuario quiere salir
    if texto.lower() == 'salir':
        print("\n¡Hasta luego! 👋")
        break

    # Cambiar velocidad
    if texto.lower() == 'velocidad':
        mostrar_menu()
        try:
            nueva_velocidad = input("🎚️  Nueva velocidad (50-300): ").strip()
            if nueva_velocidad:
                nueva_velocidad = int(nueva_velocidad)
                if 50 <= nueva_velocidad <= 300:
                    velocidad_actual = nueva_velocidad
                    print(f"✅ Velocidad cambiada a {velocidad_actual}\n")
                else:
                    print("⚠️  La velocidad debe estar entre 50 y 300.\n")
            else:
                print("⚠️  Cancelado.\n")
        except ValueError:
            print("❌ Por favor, ingresa un número válido.\n")
        continue

    # Validar que no esté vacío
    if not texto:
        print("⚠️  Por favor, escribe algo.\n")
        continue

    # Convertir texto a voz
    try:
        print(f"🔊 Reproduciendo (velocidad: {velocidad_actual})...")

        # Crear un nuevo motor para cada reproducción
        motor_temp = crear_motor_voz()
        motor_temp.say(texto)
        motor_temp.runAndWait()
        motor_temp.stop()  # Limpiar recursos

        print("✅ Completado!\n")
    except Exception as e:
        print(f"❌ Error: {e}\n")
        print("🔄 Intentando con configuración alternativa...\n")
        try:
            # Si falla, intentar con configuración básica
            motor_temp = pyttsx3.init()
            motor_temp.setProperty('rate', velocidad_actual)
            motor_temp.setProperty('volume', 0.8)
            motor_temp.say(texto)
            motor_temp.runAndWait()
            motor_temp.stop()
            print("✅ Completado con configuración alternativa!\n")
        except Exception as e2:
            print(f"❌ Error crítico: {e2}\n") 
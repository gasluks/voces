import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

print("\n" + "="*60)
print("📋 VOCES DISPONIBLES EN TU SISTEMA")
print("="*60)

for i, voice in enumerate(voices):
    print(f"\n{i}. {voice.name}")
    print(f"   ID: {voice.id}")
    if hasattr(voice, 'languages'):
        print(f"   Idiomas: {voice.languages}")

print("\n" + "="*60)

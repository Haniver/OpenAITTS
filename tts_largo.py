from pathlib import Path
from openai import OpenAI
import os
from credenciales import OPENAI_KEY  # Se importa la variable OPENAI_KEY

# Solicitar información al usuario
source_file = input("Introduce el nombre base del archivo de origen (e.g., 'source.txt'): ")
start_number = int(input("Introduce el número desde el cual empezar a procesar (e.g., '3'): "))
voice_name = input("Introduce el nombre de la voz a utilizar (e.g., 'alloy', 'echo', 'fable', etc.): ")

# Inicializar el cliente de OpenAI
client = OpenAI(
    api_key=OPENAI_KEY  # Se utiliza la variable importada en lugar del token hardcodeado
)

base_name, ext = os.path.splitext(source_file)
current_number = start_number

while True:
    input_file_name = f"{base_name} - {current_number:02d}{ext}"
    if not Path(input_file_name).exists():
        print(f"El archivo {input_file_name} no existe. Proceso terminado.")
        break
    with open(input_file_name, 'r', encoding='utf-8') as f:
        text = f.read()

    # Establecer el nombre del archivo MP3 de salida
    speech_file_path = Path(__file__).parent / f"{base_name} - {current_number:02d}.mp3"

    # Crear el discurso
    response = client.audio.speech.create(
        model="tts-1",
        voice=voice_name,
        input=text
    )

    response.stream_to_file(speech_file_path)
    print(f"Archivo generado: {speech_file_path}")

    current_number += 1

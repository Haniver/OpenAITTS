from pydub import AudioSegment
import os

def merge_mp3_files(base_name):
    # Obtener todos los archivos que coinciden con el nombre base
    files = [f for f in os.listdir() if f.startswith(base_name) and f.endswith('.mp3')]
    files.sort()  # Ordenar los archivos por nombre

    # Crear un objeto AudioSegment vacío
    combined = AudioSegment.empty()

    # Combinar todos los archivos
    for file in files:
        audio = AudioSegment.from_mp3(file)
        combined += audio

    # Exportar el archivo combinado
    output_file = f"{base_name}.mp3"
    combined.export(output_file, format="mp3")
    print(f"Archivos combinados en {output_file}")

if __name__ == "__main__":
    base_name = input("Introduce el nombre general de los archivos MP3: ")
    merge_mp3_files(base_name)
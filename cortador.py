import os
import re  # importación agregada para procesamiento de patrones

def split_text_file(input_file):
    max_chars = 4096  # Límite máximo de caracteres

    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    sentences = text.split('.')
    chunks = []
    current_chunk = ''
    
    for sentence in sentences:
        if sentence.strip() == '':
            continue
        sentence += '.'
        if len(current_chunk) + len(sentence) <= max_chars:
            current_chunk += sentence
        else:
            chunks.append(current_chunk)
            current_chunk = sentence

    if current_chunk:
        chunks.append(current_chunk)

    base_name, ext = os.path.splitext(input_file)

    for i, chunk in enumerate(chunks, start=1):
        # Procesar el bloque para agregar punto al final de cada línea si no lo tiene
        processed_lines = []
        for line in chunk.splitlines():
            # Se verifica si la línea no termina en '.', '!', '?', ':' o ';' o con puntos suspensivos (posiblemente seguidos de comillas)
            if line.strip() and not re.search(r'[.?!:;…](?:[\"\'’”])?\s*$', line):
                processed_lines.append(line.rstrip() + '.')
            else:
                processed_lines.append(line)
        chunk = "\n".join(processed_lines)
        output_file = f"{base_name} - {i:02d}{ext}"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(chunk)
        print(f"Archivo creado: {output_file}")

if __name__ == "__main__":
    input_file = input("Por favor, introduce el nombre del archivo de entrada (e.g., 'source.txt'): ")
    split_text_file(input_file)

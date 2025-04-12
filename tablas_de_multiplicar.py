from pathlib import Path
from openai import OpenAI
from credenciales import OPENAI_KEY  # Se importa la variable OPENAI_KEY

client = OpenAI(
    api_key=OPENAI_KEY
)

# Mapeo de la última cifra del producto a la voz (en minúsculas)
voice_map = {
    1: "sage",
    2: "ash",
    3: "coral",
    4: "echo",
    5: "fable",
    6: "onyx",
    7: "nova",
    8: "alloy",
    9: "shimmer",
    0: "sage"
}

# Función para convertir números (1 a 100) a palabras en español
def numero_a_palabras(n):
    num_words = {
        0: "cero",
        1: "uno",
        2: "dos",
        3: "tres",
        4: "cuatro",
        5: "cinco",
        6: "seis",
        7: "siete",
        8: "ocho",
        9: "nueve",
        10: "diez",
        11: "once",
        12: "doce",
        13: "trece",
        14: "catorce",
        15: "quince",
        20: "veinte",
        30: "treinta",
        40: "cuarenta",
        50: "cincuenta",
        60: "sesenta",
        70: "setenta",
        80: "ochenta",
        90: "noventa",
        100: "cien"
    }
    if n in num_words:
        return num_words[n]
    elif 16 <= n <= 19:
        return "dieci" + num_words[n - 10]
    elif 21 <= n <= 29:
        veinti = {
            21: "veintiuno",
            22: "veintidós",
            23: "veintitrés",
            24: "veinticuatro",
            25: "veinticinco",
            26: "veintiséis",
            27: "veintisiete",
            28: "veintiocho",
            29: "veintinueve"
        }
        return veinti[n]
    else:
        tens = (n // 10) * 10
        ones = n % 10
        return num_words[tens] + " y " + num_words[ones]

# Generar pares (a, b) donde ambos están entre 2 y 9, y a >= b.
multiplication_pairs = [(a, b) for a in range(2, 10) for b in range(2, a + 1)]

# Procesar cada par, generar la frase y crear el audio con la voz correspondiente
for i, (a, b) in enumerate(multiplication_pairs):
    product = a * b
    # Seleccionar la voz en función del último dígito del producto
    voice = voice_map[product % 10]
    # Construir la frase con la primera letra del primer número en mayúscula
    a_text = numero_a_palabras(a).capitalize()
    b_text = numero_a_palabras(b)
    product_text = numero_a_palabras(product)
    phrase = f"{a_text} por {b_text}, {product_text}."
    
    # Generar la ruta del archivo de audio (por ejemplo, speech_1.mp3, speech_2.mp3, etc.)
    speech_file_path = Path(__file__).parent / f"speech_{i+1}.mp3"
    
    try:
        response = client.audio.speech.create(
            model="tts-1",
            voice=voice,
            input=phrase
        )
        response.stream_to_file(speech_file_path)
        print(f"Guardado: {speech_file_path} | Voz: {voice} | Texto: '{phrase}'")
    except Exception as e:
        print(f"Error generando audio para '{phrase}': {e}")

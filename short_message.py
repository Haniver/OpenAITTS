from pathlib import Path
from openai import OpenAI
from credenciales import OPENAI_KEY  # Se importa la variable OPENAI_KEY

client = OpenAI(
    api_key=OPENAI_KEY,
)

speech_file_path = Path(__file__).parent / "speech_7.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="sage",
  input="""
    Cinco por dos, diez.
  """
)

response.stream_to_file(speech_file_path)
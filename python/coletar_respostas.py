import google.genai as genai

import psycopg2

from dotenv import load_dotenv
import os

from pathlib import Path
load_dotenv(dotenv_path=Path(__file__).parent.parent / ".env")

from datetime import date
hoje = date.today()

API_KEY = os.getenv("API_KEY_GEMINI")
DB_PASSWORD = os.getenv("DB_PASSWORD")

client = genai.Client(api_key=API_KEY)

resposta_teste = client.models.generate_content(
    model = "models/gemini-2.5-flash",
    config = {"system_instruction": "Resposta direta e curta em, no máximo, uma frase, deixando o texto do prompt mais rebuscado. Não enviar introdução ou fechamento antes da frase corrigida solicitada, apenas enviar a frase corrigida."},
    contents = "melhore o texto para setor de SAC: posso te ajudar em mais o que?"
)

print(resposta_teste.text)

teste = psycopg2.connect(
    host = "localhost",
    port = 5432,
    database = "curadoria_ia",
    user = "postgres",
    password = DB_PASSWORD
)

cursor = teste.cursor()
cursor.execute("INSERT INTO respostas (pergunta_para_ia, resposta_da_ia, qual_ia_gerou, quando_gerou, para_que_foi_usado, tempo_economizado, setor) VALUES (%s, %s, %s, %s, %s, %s, %s)", ("posso te ajudar em mais o que?" , resposta_teste.text, "Gemini", hoje, "melhorar texto", "1", "SAC"))
teste.commit()
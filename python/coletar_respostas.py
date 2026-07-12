# importar a API do Gemini
import google.genai as genai

# importar a biblioteca psycopg2 para conectar ao banco de dados PostgreSQL
import psycopg2

# importar a biblioteca dotenv para carregar variáveis de ambiente do arquivo .env
from dotenv import load_dotenv

# importar a biblioteca os para acessar variáveis de ambiente
import os

# importar a biblioteca pathlib para manipular caminhos de arquivos
from pathlib import Path
# carregar variáveis de ambiente do arquivo .env localizado no diretório pai do arquivo atual
load_dotenv(dotenv_path=Path(__file__).parent.parent / ".env")

# importar a biblioteca datetime para obter a data atual
from datetime import date
# obter a data atual
hoje = date.today()

# carregar a chave da API do Gemini e a senha do banco de dados PostgreSQL a partir das variáveis de ambiente
API_KEY = os.getenv("API_KEY_GEMINI")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# criar um cliente da API do Gemini usando a chave da API
client = genai.Client(api_key=API_KEY)

# gerar uma resposta usando o modelo Gemini-2.5-flash com uma instrução do sistema para fornecer uma resposta direta e curta, melhorando o texto fornecido
resposta_teste = client.models.generate_content(
    model = "models/gemini-2.5-flash",
    config = {"system_instruction": "Resposta direta e curta em, no máximo, uma frase, deixando o texto do prompt mais rebuscado. Não enviar introdução ou fechamento antes da frase corrigida solicitada, apenas enviar a frase corrigida."},
    contents = "melhore o texto para setor de SAC: posso te ajudar em mais o que?"
)

# imprimir a resposta gerada pela IA no console
print(resposta_teste.text)

# conectar ao banco de dados PostgreSQL usando a biblioteca psycopg2 e as credenciais fornecidas
teste = psycopg2.connect(
    host = "localhost",
    port = 5432,
    database = "curadoria_ia",
    user = "postgres",
    password = DB_PASSWORD
)

# criar um cursor para executar comandos SQL no banco de dados
cursor = teste.cursor()

# inserir a pergunta, a resposta gerada pela IA, o nome da IA que gerou a resposta, a data de geração, o propósito do uso, o tempo economizado e o setor no banco de dados
cursor.execute("INSERT INTO respostas (pergunta_para_ia, resposta_da_ia, qual_ia_gerou, quando_gerou, para_que_foi_usado, tempo_economizado, setor) VALUES (%s, %s, %s, %s, %s, %s, %s)", ("posso te ajudar em mais o que?" , resposta_teste.text, "Gemini", hoje, "melhorar texto", "1", "SAC"))

# confirmar as alterações no banco de dados
teste.commit()

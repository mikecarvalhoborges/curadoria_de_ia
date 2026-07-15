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

# importar a biblioteca gspread para interagir com o Google Sheets
import gspread

# autenticar no Google Sheets usando o arquivo de credenciais
gc = gspread.service_account(filename = Path(__file__).parent.parent / "credenciais_sheets.json")

# abrir a planilha
planilha = gc.open("curadoria_ia")

# acessar a primeira aba da planilha
aba_respostas = planilha.sheet1

# carregar a senha do banco de dados a partir das variáveis de ambiente
DB_PASSWORD = os.getenv("DB_PASSWORD")

# conectar ao banco de dados PostgreSQL
teste = psycopg2.connect(
    host = "localhost",
    port = 5432,
    database = "curadoria_ia",
    user = "postgres",
    password = DB_PASSWORD
)

# criar um cursor para executar comandos SQL no banco de dados
cursor_respostas = teste.cursor()

# selecionar todos os dados da tabela "respostas"
cursor_respostas.execute("SELECT * from respostas")

# buscar todos os resultados da consulta
dados = cursor_respostas.fetchall()

aba_respostas.clear() # limpar a aba antes de adicionar os dados
aba_respostas.append_row(["id_resposta", "pergunta_para_ia", "resposta_da_ia", "qual_ia_gerou", "quando_gerou", "para_que_foi_usado", "tempo_economizado", "setor"]) # adicionar o cabeçalho na aba do Google Sheets

# adicionar os dados da tabela "respostas" na aba do Google Sheets
for i in dados:
    linha = list(i) # converter a tupla em lista para poder modificar o valor da data
    linha[4] = str(linha[4])  # converte a data para string
    aba_respostas.append_row(linha) # adicionar a linha na aba do Google Sheets


# acessar a aba de avaliações
aba_avaliacoes = planilha.worksheet("Página2") 

# criar um cursor para executar comandos SQL no banco de dados
cursor_avaliacoes = teste.cursor()

# selecionar todos os dados da tabela "avaliacoes"
cursor_avaliacoes.execute("SELECT * from avaliacoes")

# buscar todos os resultados da consulta
dados_avaliacoes = cursor_avaliacoes.fetchall()

# adicionar os dados da tabela "avaliacoes" na aba do Google Sheets
aba_avaliacoes.clear() 

# adicionar o cabeçalho na aba do Google Sheets
aba_avaliacoes.append_row(["id_avaliacao", "id_resposta_utilizada", "acuracia", "precisao", "fidelidade", "relevancia"])

# adicionar os dados da tabela "avaliacoes" na aba do Google Sheets
for i in dados_avaliacoes:
    linha = list(i) # converter a tupla em lista para poder modificar o valor da data
    linha[2] = float(linha[2])
    linha[3] = float(linha[3])
    linha[4] = float(linha[4])
    linha[5] = float(linha[5])
    aba_avaliacoes.append_row(linha) # adicionar a linha na aba do Google Sheets
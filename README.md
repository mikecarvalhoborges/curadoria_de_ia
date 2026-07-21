# Curadoria de IA
## Análise e comparação de respostas de diferentes IA's, utilizando dados fictícios, com o objetivo de identificar oportunidades e impactos gerados para dois setores de uma empresa.

### Tecnologias usadas: 
- PostgreSQL;
- Python;
- Google Sheets.

### Estrutura do repositório:

```
curadoria_de_ia/
├── banco_de_dados/
├── python/
└── README.md
```

### Aprendizados:
- Automatização de tarefas;
- Utilização de API de Inteligência Artificial (Gemini);
- Conexão entre banco de dados (PostgreSQL), tabela (Google Sheets) e IA (Gemini);
- Modelagem de banco de dados relacional com chaves primárias e estrangeiras;
- Prompt engineering com system instructions;
- Proteção de credenciais com variáveis de ambiente (.env).

### Como rodar:
- Instalar o Python;
- Instalar as bibliotecas (`pip install google-genai psycopg2-binary gspread python-dotenv`);
- Criar a API do Google Gemini;
- Criar as credenciais JSON do Google Sheets;
- Criar o arquivo .env com as credenciais de API's;
- Algo como "Executar o arquivo banco_de_dados/dados.sql no PostgreSQL para criar o banco e as tabelas;
- Ordem de execução dos scripts: `coletar_respostas.py` → `exportar_sheets.py` → ou simplesmente `pipeline.py`.

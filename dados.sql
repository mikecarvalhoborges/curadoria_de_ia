-- criando os tipos de entrada para os setores, para  evitar erros

CREATE TYPE setor_enum AS ENUM ('SAC', 'Vendas');

-- criando a tabela 'respostas'

CREATE TABLE respostas (
    ID_resposta SERIAL,
    Pergunta_para_IA TEXT,
    Resposta_da_IA TEXT,
    Qual_IA_gerou TEXT,
    Quando_gerou DATE,
    Para_que_foi_usado TEXT,
    Tempo_economizado INTEGER,
    Setor setor_enum
);

-- adicionando a chave primária na tabela 'respostas'

ALTER TABLE respostas
ADD CONSTRAINT respostas_pkey PRIMARY KEY (ID_resposta);

-- criando a tabela 'avaliacoes' com referencia a tabela 'respostas'

CREATE TABLE avaliacoes (
    id_avaliacao SERIAL PRIMARY KEY,
    id_resposta_utilizada INTEGER REFERENCES respostas(ID_resposta),
    acuracia NUMERIC(5,4),
    precisao NUMERIC(5,4),
    fidelidade NUMERIC(5,4),
    relevancia NUMERIC(5,4)
);

-- inserindo a primeira linha na tabela 'respostas'

INSERT INTO respostas (pergunta_para_ia, resposta_da_ia, qual_ia_gerou, quando_gerou, para_que_foi_usado, tempo_economizado, setor)
VALUES ('te ajudo em algo mais?', 'Posso lhe auxiliar com algo mais?', 'Gemini', '2026-06-10', 'melhorar texto', 1, 'SAC');

-- inserindo a primeira linha na tabela 'avaliacoes'

INSERT INTO avaliacoes (id_resposta_utilizada, acuracia, precisao, fidelidade, relevancia)
VALUES (1, 0.9500, 0.8900, 0.9780, 0.9876);

-- verificando se a tabela 'respostas' foi criada corretamente e com liunhas e colunas corretas 

SELECT * FROM respostas;

-- verificando se a tabela 'avaliacoes' foi criada corretamente e com liunhas e colunas corretas 

SELECT * FROM avaliacoes;

-- mostrando setor, IA usada e acurácia unindo as duas tabelas

SELECT
	respostas.setor,
	respostas.qual_ia_gerou,
	avaliacoes.acuracia
FROM respostas
JOIN avaliacoes ON respostas.id_resposta = avaliacoes.id_resposta_utilizada;

-- verificando a média de acurácia por setor, unindo as duas tabelas e ordenando pela média de acurácia de forma decrescente 

SELECT
	 respostas.setor, 
	 ROUND(AVG(avaliacoes.acuracia), 2) * 100 AS acuracia_media
FROM respostas JOIN avaliacoes ON respostas.id_resposta = avaliacoes.id_resposta_utilizada 
GROUP BY respostas.setor 
ORDER BY acuracia_media DESC;

-- verificando a média de acurácia por setor, unindo as duas tabelas e ordenando pela média de acurácia de forma decrescente + contando quantos registros têm cada setor

SELECT
	 respostas.setor, 
	 ROUND(AVG(avaliacoes.acuracia), 2) * 100 AS acuracia_media,
	 COUNT(*) AS total_respostas
FROM respostas JOIN avaliacoes ON respostas.id_resposta = avaliacoes.id_resposta_utilizada 
GROUP BY respostas.setor 
ORDER BY acuracia_media DESC;
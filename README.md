# Base de Conhecimento - Integração de Web Scraping e Banco de Dados Vetorial

## O Que Ele Faz

Este projeto utiliza um agente LLM (Large Language Model) para realizar scraping de dados do site da FinOps, processar essas informações e armazená-las em um banco de dados vetorial. A base de dados resultante permite buscas através de perguntas em linguagem natural, retornando os vetores mais relevantes. Este sistema serve como base para uma base de conhecimento sobre FinOps, que futuramente será integrada com RAG (Geração Aumentada por Recuperação) para oferecer insights aprimorados com IA.

## Como Funciona

- Web Scraping:
O agente LLM extrai conteúdo do site da FinOps, focando em dados relevantes e estruturados.

- Processamento de Dados:
Os dados extraídos são limpos, organizados e convertidos em representações vetoriais adequadas para buscas baseadas em similaridade.

- Armazenamento Vetorial:
Os dados processados são armazenados em um banco de dados vetorial, permitindo buscas eficientes e escaláveis.

- Consulta em Linguagem Natural:
Os usuários podem realizar perguntas em linguagem natural. O sistema recupera os vetores mais relevantes do banco de dados e fornece respostas precisas e contextualizadas.

- Integração Futura:
O banco de dados vetorial será a base de conhecimento para sistemas baseados em RAG, utilizando IA para fornecer insights sobre FinOps com raciocínio avançado e compreensão contextual.

## Parâmetros de Entrada

_- URL do Site: O endereço do site da FinOps para realizar o scraping.
_- Credenciais do Banco de Dados Vetorial: Credenciais para conexão com o banco de dados onde os vetores serão armazenados e consultados.

## Pré-requisitos

Para implantar e utilizar este projeto, são necessários os seguintes pré-requisitos:

- Ambiente de Scraping:
Um ambiente Python com pacotes para web scraping, Para instalar todas as dependências necessárias, execute o seguinte comando no terminal:

```bash
pip install -r requirements.txt
```

- Banco de Dados Vetorial:
Um banco de dados que suporte armazenamento e recuperação de vetores, como Milvus. Podemos utiliar o Milvus em container. No terminal execute o seguinte comando para subir um container do Milvus em seu docker:

```bash
docker-compose up -d
```
## Plataformas Suportadas
O sistema é independente de plataforma e pode ser executado em qualquer ambiente que suporte Python e suas dependências.
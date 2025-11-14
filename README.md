# Tratos Saicon API

API REST para gerenciamento de alimentação de animais (tratos), desenvolvida com FastAPI e PostgreSQL.

---

## Como Executar o Projeto

### Pré-requisitos

- **Docker Desktop** instalado ([Download](https://www.docker.com/products/docker-desktop))
- **Git** instalado


---

## Executar o Projeto (3 passos)

### 1. Clone o repositório

```bash
git clone https://github.com/joaomasc/tratoapi.git
cd tratos-saicon-api
```

### 2. Inicie os containers

```bash
docker-compose up --build
```

### 3. Acesse a API

- **API**: http://localhost:8000
- **Documentação Interativa (Swagger)**: http://localhost:8000/docs

---

## Parar o Projeto

Para parar os containers:

```bash
docker-compose stop
```

Para parar e remover os containers (mantém os dados):

```bash
docker-compose down
```

Parar e remover tudo (inclusive dados do banco):

```bash
docker-compose down -v
```

---

## Executar Localmente (Sem Docker)

> **Nota**: Para rodar sem Docker, você precisa configurar o arquivo `.env` com as credenciais do seu banco PostgreSQL local. Use o arquivo `.env.example` como referência.

---

## Testar a API

### 1. Pelo navegador

Acesse http://localhost:8000/docs e teste diretamente pela interface Swagger.

### 2. Criar um novo trato (exemplo com curl)

```bash
curl -X POST "http://localhost:8000/tratos/" \
  -H "Content-Type: application/json" \
  -d '{
    "animal_batch": "Lote 05A",
    "feed_type": "Engorda Premium",
    "silo_weight_before": 1000.5,
    "silo_weight_after": 850.3
  }'
```

### 3. Listar todos os tratos

```bash
curl http://localhost:8000/tratos/
```

---

## Documentação da API

Acesse a documentação interativa em: **http://localhost:8000/docs**

Nela você pode:
- Ver todos os endpoints disponíveis
- Testar as requisições diretamente no navegador
- Ver parâmetros, tipos de dados e exemplos
- Visualizar os schemas de request/response

## Stack Tecnológica

- **Python 3.11** com FastAPI
- **PostgreSQL 16** 
- **SQLAlchemy 2.0** (ORM)
- **Psycopg3** (Driver PostgreSQL)
- **Pydantic** (Validação de dados)
- **Docker & Docker Compose**

---

## Estrutura do Projeto

```
tratos-saicon-api/
├── app/
│   ├── api/routes/      # Endpoints da API
│   ├── core/            # Configurações
│   ├── database/        # Conexão com BD
│   ├── models/          # Modelos do banco (SQLAlchemy)
│   ├── schemas/         # Validação (Pydantic)
│   └── services/        # Lógica de negócio
├── docker-compose.yml   # Orquestração dos containers
├── Dockerfile           # Imagem Docker da API
├── requirements.txt     # Dependências Python
└── main.py             # Ponto de entrada
```

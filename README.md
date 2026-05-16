# 🍕 Fast API - Sistema de Pedidos

API REST para gerenciamento de usuários e pedidos, desenvolvida com FastAPI e SQLAlchemy.

---

## 🚀 Tecnologias

- **[FastAPI](https://fastapi.tiangolo.com/)** — framework web moderno e de alta performance
- **[SQLAlchemy](https://www.sqlalchemy.org/)** — ORM para banco de dados
- **[Alembic](https://alembic.sqlalchemy.org/)** — migrations de banco de dados
- **[SQLite](https://www.sqlite.org/)** — banco de dados
- **[Pydantic v2](https://docs.pydantic.dev/)** — validação de dados
- **[Passlib + bcrypt](https://passlib.readthedocs.io/)** — criptografia de senhas
- **[Python-Jose](https://python-jose.readthedocs.io/)** — autenticação JWT
- **[Uvicorn](https://www.uvicorn.org/)** — servidor ASGI

---

## 📁 Estrutura do Projeto

```
Fast_Api_teste/
├── alembic/              # Migrations do banco de dados
│   └── versions/
├── alembic.ini           # Configuração do Alembic
├── main.py               # Ponto de entrada da aplicação
├── models.py             # Modelos do banco de dados (SQLAlchemy)
├── schemas.py            # Schemas de validação (Pydantic)
├── dependencies.py       # Dependências (sessão, autenticação)
├── auth_routes.py        # Rotas de autenticação e usuários
├── order_routes.py       # Rotas de pedidos
├── requirements.txt      # Dependências do projeto
├── .env.example          # Exemplo de variáveis de ambiente
└── .gitignore
```

---

## ⚙️ Instalação

**1. Clone o repositório**
```bash
git clone https://github.com/Lugauls/Fast_Api_teste.git
cd Fast_Api_teste
```

**2. Crie e ative um ambiente virtual**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

**3. Instale as dependências**
```bash
pip install -r requirements.txt
```

**4. Configure as variáveis de ambiente**
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

**5. Execute as migrations**
```bash
alembic upgrade head
```

**6. Crie um usuário administrador**
```bash
python criar_admin.py
```

**7. Inicie o servidor**
```bash
uvicorn main:app --reload
```

A API estará disponível em `http://localhost:8000`  
Documentação interativa em `http://localhost:8000/docs`

---

## 🔐 Autenticação

A API utiliza autenticação via **JWT (Bearer Token)**. Para acessar rotas protegidas:

1. Faça login na rota `/auth/login` com email e senha
2. Copie o token retornado
3. Inclua no header das requisições: `Authorization: Bearer <token>`

No Swagger (`/docs`), clique em **Authorize** e cole o token.

---

## 📌 Rotas

### Auth (`/auth`)

| Método | Rota | Descrição | Auth |
|--------|------|-----------|------|
| `POST` | `/auth/login` | Login e geração de token JWT | ❌ |
| `POST` | `/auth/criar_conta` | Criar novo usuário | ✅ Admin |

### Pedidos (`/order`)

| Método | Rota | Descrição | Auth |
|--------|------|-----------|------|
| `GET` | `/order/` | Rota padrão de pedidos | ✅ |
| `GET` | `/order/listar` | Listar todos os pedidos | ✅ Admin |
| `POST` | `/order/pedidos` | Criar novo pedido | ✅ |
| `POST` | `/order/pedidos/cancelar/{id}` | Cancelar pedido | ✅ Admin ou dono |
| `POST` | `/order/pedidos/adicionar-item/{id}` | Adicionar item ao pedido | ✅ Admin ou dono |

---

## 🗄️ Modelos

### Usuario
| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | Integer | Chave primária |
| nome | String | Nome do usuário |
| email | String | Email (único) |
| senha | String | Senha criptografada (bcrypt) |
| ativo | Boolean | Se o usuário está ativo |
| admin | Boolean | Se o usuário é administrador |

### Pedido
| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | Integer | Chave primária |
| status | String | PENDENTE / CANCELADO / FINALIZADO |
| usuario | Integer | FK → Usuario |
| preco | Integer | Preço total calculado |
| itens | Relationship | Itens do pedido |

### ItensPedido
| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | Integer | Chave primária |
| quantidade | Integer | Quantidade do item |
| sabor | String | Sabor |
| tamanho | String | Tamanho |
| valor_unitario | Float | Preço unitário |
| pedido | Integer | FK → Pedido |

---

## 🔄 Migrations (Alembic)

```bash
# Gerar nova migration após alterar os models
alembic revision --autogenerate -m "descrição da alteração"

# Aplicar migrations
alembic upgrade head

# Voltar uma migration
alembic downgrade -1

# Ver migration atual
alembic current
```

> ⚠️ O projeto usa SQLite. O `render_as_batch=True` está configurado no `env.py` para suportar operações de `ALTER TABLE`.

---

## 🧪 Testes

Acesse a documentação interativa do Swagger para testar as rotas:

```
http://localhost:8000/docs
```

Fluxo recomendado para testes:
1. Login com usuário admin → `/auth/login`
2. Autorizar no Swagger com o token recebido
3. Criar um pedido → `/order/pedidos`
4. Adicionar itens → `/order/pedidos/adicionar-item/{id}`
5. Listar pedidos → `/order/listar`

---

## 📝 Variáveis de Ambiente

Crie um arquivo `.env` baseado no `.env.example`:

```env
SECRET_KEY=sua_chave_secreta_aqui
ALGORITHM=HS256
```

---

## 📄 Licença

Projeto desenvolvido para fins de aprendizado com FastAPI.

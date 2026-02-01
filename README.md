# 🔐 Auth Service (Production-Grade)

A MAANG-level authentication service built using **FastAPI**, following
**Clean Architecture, Domain-Driven Design (DDD)** and **production best practices**.

## 🚀 Why This Project?
Most authentication tutorials focus only on CRUD APIs.
This project demonstrates **how MAANG companies actually design auth systems**:
- Clear separation of concerns
- Scalable file structure
- Security-first design
- Dockerized & migration-ready
- Designed for microservices

## 🧠 High-Level Architecture
👉 See: ARCHITECTURE.md

- API Layer (FastAPI routes)
- Domain Layer (Business rules)
- Infrastructure Layer (DB, repositories)
- Service Layer (Use cases)

## 📂 Project Structure
```
auth-service
├─ ARCHITECTURE.md
├─ DECISIONS.md
├─ Dockerfile
├─ PROJECT_VISION.md
├─ README.md
├─ REQUIREMENTS.md
├─ ROADMAP.md
├─ SCALABILITY.md
├─ SECURITY.md
├─ TECH_STACK.md
├─ alembic
│  ├─ README
│  ├─ __pycache__
│  │  └─ env.cpython-312.pyc
│  ├─ env.py
│  ├─ script.py.mako
│  └─ versions
│     ├─ 183474895837_create_users_table.py
│     ├─ 2985f4ece203_add_refresh_token.py
│     └─ __pycache__
│        ├─ 183474895837_create_users_table.cpython-312.pyc
│        ├─ 2985f4ece203_add_refresh_token.cpython-312.pyc
│        └─ ed5f8274fdd8_create_users_table.cpython-312.pyc
├─ alembic.ini
├─ app
│  ├─ __init__.py
│  ├─ __pycache__
│  │  ├─ __init__.cpython-312.pyc
│  │  └─ main.cpython-312.pyc
│  ├─ api
│  │  ├─ __pycache__
│  │  │  └─ router.cpython-312.pyc
│  │  ├─ router.py
│  │  └─ v1
│  │     ├─ __pycache__
│  │     │  └─ dependencies.cpython-312.pyc
│  │     ├─ dependencies.py
│  │     └─ routes
│  │        ├─ __pycache__
│  │        │  └─ auth_routes.cpython-312.pyc
│  │        └─ auth_routes.py
│  ├─ core
│  │  ├─ __pycache__
│  │  │  └─ config.cpython-312.pyc
│  │  └─ config.py
│  ├─ domain
│  │  ├─ __pycache__
│  │  │  └─ models.cpython-312.pyc
│  │  └─ models
│  │     ├─ __pycache__
│  │     │  ├─ refresh_token.cpython-312.pyc
│  │     │  └─ user.cpython-312.pyc
│  │     ├─ refresh_token.py
│  │     └─ user.py
│  ├─ infrastructure
│  │  ├─ __pycache__
│  │  │  ├─ database.cpython-312.pyc
│  │  │  ├─ refresh_token_repo.cpython-312.pyc
│  │  │  └─ repositories.cpython-312.pyc
│  │  ├─ database.py
│  │  ├─ refresh_token_repo.py
│  │  └─ user_repo.py
│  ├─ main.py
│  ├─ schemas
│  │  ├─ __pycache__
│  │  │  └─ auth.cpython-312.pyc
│  │  └─ auth.py
│  ├─ services
│  │  ├─ __pycache__
│  │  │  └─ auth_service.cpython-312.pyc
│  │  └─ auth_service.py
│  └─ utils
│     ├─ __pycache__
│     │  └─ security.cpython-312.pyc
│     └─ security.py
├─ docker-compose.yml
├─ requirements.txt
└─ test_db.py

```
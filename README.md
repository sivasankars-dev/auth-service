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
├─ Dockerfile
├─ PROJECT_VISION.md
├─ README.md
├─ REQUIREMENTS.md
├─ TECH_STACK.md
├─ alembic
│  ├─ README
│  ├─ __pycache__
│  │  └─ env.cpython-312.pyc
│  ├─ env.py
│  ├─ script.py.mako
│  └─ versions
├─ alembic.ini
├─ app
│  ├─ api
│  │  ├─ router.py
│  │  └─ v1
│  │     ├─ dependencies.py
│  │     └─ routes
│  │        └─ auth_routes.py
│  ├─ core
│  │  ├─ __pycache__
│  │  │  └─ config.cpython-312.pyc
│  │  └─ config.py
│  ├─ domain
│  │  └─ models.py
│  ├─ infrastructure
│  │  ├─ __pycache__
│  │  │  └─ database.cpython-312.pyc
│  │  ├─ database.py
│  │  └─ repositories.py
│  ├─ main.py
│  ├─ schemas
│  │  └─ auth.py
│  ├─ services
│  │  └─ auth_service.py
│  └─ utils
│     └─ security.py
├─ docker-compose.yml
└─ requirements.txt

```
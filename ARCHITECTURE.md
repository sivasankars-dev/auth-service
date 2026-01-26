# Architecture – Auth Service (Production-Grade)

A MAANG-level authentication architecture designed to demonstrate how real-world auth systems are structured, secured, and scaled in large organizations.

## Why This Architecture?
Most auth projects stop at login & signup APIs. This architecture shows how MAANG companies actually think about auth systems:
- Clear separation of responsibilities
- Security-first token design
- Microservice-ready boundaries
- Framework-independent business logic
- Production-grade scalability

## Architectural Style
Built using Clean Architecture + Domain-Driven Design (DDD) principles.

Key idea:
- Business logic must not depend on frameworks, databases, or external services.

Client
↓
API Layer (FastAPI)
↓
Service Layer (Use Cases)
↓
Domain Layer (Business Rules)
↓
Infrastructure Layer (PostgreSQL, Repositories)

## Layered Responsibilities
### API Layer

- Handles HTTP requests & responses
- Request validation & dependency injection
- Delegates work to services

### Service Layer

- Implements authentication use cases
- Coordinates domain logic
- Handles token lifecycle

### Domain Layer

- Core entities & business rules
- Pure Python, framework-agnostic
- Most stable layer

### Infrastructure Layer

- Database access (PostgreSQL)
- ORM & repository implementations
- Alembic migrations

## Authentication & Security

- JWT Algorithm: RS256 (asymmetric)
- Access Token: Short-lived
- Refresh Token: Stored securely in DB

### Why RS256?

- Only Auth Service can sign tokens
- Other services verify using public key
- Prevents token forgery in microservices

## Key Management

- Private key stored securely (env / secret manager)
- Public key exposed via JWKS endpoint
- Supports key rotation without downtime

## Deployment & Scalability

- Dockerized, stateless service
- Horizontally scalable
- Cloud & CI/CD friendly


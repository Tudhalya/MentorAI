# Infrastructure

This directory contains all infrastructure-related configuration and scripts.

## Structure

- **`database/`** - Database schemas, init scripts, and migrations
- **`docker/`** - Docker Compose configurations for local development
- **`deployment/`** - Deployment scripts and configs for production

## Local Development Services

### Start Services
```bash
cd docker
docker-compose up -d
```

Or use the convenience script:
```bash
cd docker
./start-services.sh
```

### Services Included

- **Postgres 16** - Main database (port 5432)
- **Chroma** - Vector database (port 8000)

### Database

The Postgres container automatically runs `database/init.sql` on first startup to create the initial schema with tables for:
- `documents` - Uploaded PDF metadata
- `chapters` - Chapter structure
- `nodes` - Content nodes (text, equations, figures)

### Environment

Services are configured for development with:
- Database: `mentorai:mentorai_dev@localhost:5432/mentorai`
- Chroma: `http://localhost:8000`
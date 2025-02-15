# Apache Trino Project

## Overview
This project sets up an Apache Trino environment using Docker and supports data ingestion, validation, and federated queries across multiple databases (MSSQL, MySQL, PostgreSQL).

## Architecture

![Project Architecture](./trino%20project.png)

## Project Structure
```
.
├── etc/
│   ├── catalog/
│   │   ├── mssql.properties
│   │   ├── mysql.properties
│   │   ├── postgresql.properties
│   ├── config.properties
│   ├── jvm.config
│   ├── node.properties
├── ingestor/
│   ├── add-data.py
│   ├── check-data.py
│   ├── federated-query.py
├── docker-compose.yml
├── README.md
```

### Configuration Files
- **`etc/catalog/*.properties`** - Defines database connectivity for Trino.
- **`etc/config.properties`** - General configuration for Trino.
- **`etc/jvm.config`** - JVM settings for Trino.
- **`etc/node.properties`** - Node-specific settings for Trino.

### Python Scripts
- **`add-data.py`** - Populates databases with sample data.
- **`check-data.py`** - Validates the inserted data.
- **`federated-query.py`** - Runs federated queries across multiple databases.

## Setup & Execution

### 1. Start Trino and Database Containers
Ensure you have Docker installed. Then, run:
```sh
docker-compose up -d
```
This will spin up Trino and the associated databases.

### 2. Add Data
Run the following script to insert sample data:
```sh
python ingestor/add-data.py
```

### 3. Check Data
Verify that data is correctly inserted by running:
```sh
python ingestor/check-data.py
```

### 4. Run Federated Query
Execute a federated query across the databases:
```sh
python ingestor/federated-query.py
```

## Notes
- Ensure the required Python dependencies are installed before running scripts.
- Modify the `*.properties` files in `etc/catalog/` to customize database connections.
- Use `docker-compose down` to stop the environment when done.

## Troubleshooting
- **Container Issues:** Run `docker ps` to check running containers.
- **Trino Logs:** Check logs using `docker logs <trino-container-id>`.
- **Database Logs:** Inspect logs for database containers if queries fail.
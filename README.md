## Introduction
This is a project to convert natural language questions to SQL queries. 

## Installation
``` shell
poetry install
ollama pull aya:8B
```
## Create database
``` sql
CREATE DATABASE mydatabase;

\c mydatabase;

CREATE TABLE employees (
    id SERIAL PRIMARY KEY, 
    name VARCHAR(100), 
    position VARCHAR(50) ,
    salary NUMERIC
);
```

## Usage
``` shell
poetry run python main.py
```


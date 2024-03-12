#!/usr/bin/env bash

set -e

psql -v ON_ERROR_STOP=1 --username postgres <<-EOSQL
    DROP DATABASE IF EXISTS postgres_db;
    DROP USER IF EXISTS postgres_user;
    CREATE USER postgres_user;
    CREATE DATABASE postgres_db ENCODING UTF8;
    GRANT ALL PRIVILEGES ON DATABASE postgres_db TO postgres_user;

    ALTER USER postgres_user WITH PASSWORD 'password123';
    ALTER USER postgres_user WITH SUPERUSER;

    CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
EOSQL
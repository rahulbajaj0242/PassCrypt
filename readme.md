# Password Manager

# Description

The Password Manager created allows the user to store their passwords safely in a database. The passwords are encrypted using the cryptography library and key used to encrypt/decrypt them is stored safely in the users local system only.

The Application also has the login system which only allows the authenticated person who knows the master key (stored in the local file) to use the application.

The postgres database was run on docker to make it easy to run and maintain in a development environment

# Concepts Used

- **Python**
- **Postgres** to manage the passwords in the database
- **Docker** to run the postgres and pgAdmin4
- **bcrypt** to encrypt the master password
- **cryptography** to encrypt/decrypt password
- **secrets** to provide functionality to suggest password to user
- **psycopg2** to connect with postgres database in docker
- **os, dotenv** to work with environment variables

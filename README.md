# Hybrid Search With Postgres & PgVector For RAG using Groq

This project demonstrates how to implement a hybrid search engine for Retrieval-Augmented Generation (RAG) using Postgres with PgVector. It showcases the use of asynchronous streaming with Groq's function calling capabilities in a FastAPI application.

![Postgres as a vector Database | Implementing Hybrid search with Postgres for RAG Using Groq.](./demo.png?raw=true "Demo")

## Description

This project utilizes Postgres as a vector database to create a hybrid search engine that combines vector search and text search capabilities. It leverages PgVector for storing and querying vector embeddings, and Groq's Large Language Model for function calling to retrieve information from the database through hybrid search.

## Technologies Used

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-CC2927?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-00ADD8?style=for-the-badge&logo=groq&logoColor=white)

## Features

- FastAPI-based implementation
- Hybrid search combining vector and text search capabilities
- Function calling for executing commands and retrieving information
- Chat interface for real-time communication
- Product search and recommendation system

## Getting Started

### Prerequisites

- Python 3.8 or higher
- PostgreSQL
- PgVector

### Dependencies

Refer to `requirements.txt` for a complete list of dependencies. Key dependencies include:

- FastAPI
- OpenAI API (for generating embeddings)
- Groq (for Large Language Model)
- SQLAlchemy
- PgVector

### Installation

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies:
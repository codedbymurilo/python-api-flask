# 📚 API REST de Gerenciamento de Livros

API REST simples desenvolvida em Python utilizando o framework **Flask** para o gerenciamento de um acervo de livros. A API implementa as operações fundamentais de **CRUD** (Create, Read, Update, Delete) com dados armazenados em memória.

---

## 🎯 Objetivo

Disponibilizar endpoints para consulta, criação, edição e exclusão de cadastros de livros.

---

## 🛠️ Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3BABC3.svg?style=for-the-badge&logo=Flask&logoColor=white)

---

## 🚀 Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

```

### 2. Instalar as dependências

Certifique-se de ter o Python e o `pip` instalados. Em seguida, instale a biblioteca do Flask:

```bash
pip install flask

```

### 3. Executar a aplicação

```bash
python app.py

```

A API iniciará no servidor local no endereço: `http://localhost:5000`

---

## 📌 Endpoints da API

**URL Base:** `http://localhost:5000`

| Método | Endpoint | Descrição | Corpo da Requisição (JSON) |
| --- | --- | --- | --- |
| **GET** | `/livros` | Lista todos os livros cadastrados | Não possui |
| **GET** | `/livros/<id>` | Busca um livro específico pelo ID | Não possui |
| **POST** | `/livros` | Adiciona um novo livro ao acervo | Objeto JSON com dados do livro |
| **PUT** | `/livros/<id>` | Atualiza as informações de um livro existente | Objeto JSON com campos a alterar |
| **DELETE** | `/livros/<id>` | Remove um livro do acervo pelo ID | Não possui |

---

## 📝 Exemplos de Uso

### **1. Cadastrar um novo livro (`POST /livros`)**

**Body (JSON):**

```json
{
  "id": 4,
  "titulo": "O Hobbit",
  "autor": "J.R.R. Tolkien"
}

```

### **2. Atualizar dados de um livro (`PUT /livros/1`)**

**Body (JSON):**

```json
{
  "titulo": "O Senhor dos Anéis - A Sociedade do Anel (Edição Especial)"
}

```

### **3. Deletar um livro (`DELETE /livros/2`)**

Remove o livro correspondente ao `id` informado na URL e retorna a lista atualizada em JSON.

---

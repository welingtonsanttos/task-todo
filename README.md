# Task Todo Application

## English

A simple task management application built with Python and SQLAlchemy. This application allows you to manage tasks with categories and statuses.

### Features

- Create, read, update, and delete tasks
- Organize tasks by categories
- Track task status (e.g., pending, in progress, completed)
- SQLite database for data persistence

### Database Models

- **TaskTodo**: Main task entity with task_id, task_title, task_description, task_status, and task_category
- **TaskCategory**: Categories to organize tasks with category_id, category_description, and insert_date
- **TaskStatus**: Status tracking for tasks with status_id, status_description, and insert_date

### Getting Started

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Initialize the database:
   ```bash
   python init_db.py
   ```

3. Run the application:
   ```bash
   python main.py
   ```

### Project Structure

```
Task-todo/
├── init_db.py              # Database initialization
├── database_config.py      # Database configuration
├── models/                 # SQLAlchemy models
│   ├── task_todo_model.py
│   ├── task_category_model.py
│   └── task_status_model.py
└── main.py                 # Main application
```

---

## Português (Brazil)

Um aplicativo simples de gerenciamento de tarefas construído com Python e SQLAlchemy. Este aplicativo permite que você gerencie tarefas com categorias e status.

### Recursos

- Criar, ler, atualizar e excluir tarefas
- Organizar tarefas por categorias
- Acompanhar o status das tarefas (ex: pendente, em andamento, concluída)
- Banco de dados SQLite para persistência de dados

### Modelos de Dados

- **TaskTodo**: Entidade principal de tarefa com task_id, task_title, task_description, task_status e task_category
- **TaskCategory**: Categorias para organizar tarefas com category_id, category_description e insert_date
- **TaskStatus**: Acompanhamento de status para tarefas com status_id, status_description e insert_date

### Como Começar

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

2. Inicialize o banco de dados:
   ```bash
   python init_db.py
   ```

3. Execute o aplicativo:
   ```bash
   python main.py
   ```

### Estrutura do Projeto

```
Task-todo/
├── init_db.py              # Inicialização do banco de dados
├── database_config.py      # Configuração do banco de dados
├── models/                 # Modelos SQLAlchemy
│   ├── task_todo_model.py
│   ├── task_category_model.py
│   └── task_status_model.py
└── main.py                 # Aplicação principal
```

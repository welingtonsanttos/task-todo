from database_config import engine, Base
from models.task_category_model import TaskCategory
from models.task_todo_model import TaskTodo
from models.task_status_model import TaskStatus

def init_db():
    # Initializes the database by creating all tables defined in the models
    # Base.metadata.create_all() creates the TaskCategory, TaskTodo and TaskStatus tables
    # if they don't already exist in the database
    Base.metadata.create_all(engine)


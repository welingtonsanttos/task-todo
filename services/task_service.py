from sqlalchemy.orm import Session

from DTO.task_creation_dto import TaskCreationDTO
from DTO.task_update_dto import TaskUpdateDTO
from log_config import get_logger
from models.task_todo_model import TaskTodo
from services.task_category_service import TaskCategoryService
from services.task_status_service import TaskStatusService

logger = get_logger(__name__)


class TaskService:

    @staticmethod
    def get_all(session: Session) -> list | None:
        with session as conn:
            return conn.query(TaskTodo).all()

    @staticmethod
    def get_by_id(session: Session, task: int) -> TaskTodo:
        try:
            task = session.query(TaskTodo).filter(TaskTodo.task_id == task).first()
            if task:
                return task
        except Exception as e:
            logger.error(e)
            raise ValueError("Task not found")

    @staticmethod
    def create(session: Session, dto: TaskCreationDTO) -> TaskTodo | None:
        category_service = TaskCategoryService()
        category = category_service.get_category_by_name(session=session, category_descr=dto.task_category)

        status_service = TaskStatusService()
        status = status_service.get_status_by_name(session=session, status_name=dto.status)

        if not status:
            raise ValueError("Status is invalid")

        try:
            logger.info("Creating new task")
            new_task = TaskTodo(task_title=dto.title, task_description=dto.description, status=status,
                                category=category)
            session.add(new_task)
            session.commit()
            session.refresh(new_task)

            if new_task:
                logger.info("Task created successfully")
                return new_task

        except Exception as e:
            session.rollback()
            logger.error(f"Task creation failed: {e}")
            raise ValueError("Failed to create task")

    @staticmethod
    def update(session: Session, dto: TaskUpdateDTO) -> TaskTodo | None:
        try:
            get_task = session.query(TaskTodo).filter(TaskTodo.task_id == dto.id).first()

            if not get_task:
                raise ValueError("Task not found")

            if get_task:
                if dto.title:
                    get_task.task_title = dto.title

                if dto.description:
                    get_task.task_description = dto.description

                if dto.status:
                    status_service = TaskStatusService()
                    status = status_service.get_status_by_name(session=session, status_name=dto.status)
                    get_task.status = status

                if dto.task_category:
                    category_service = TaskCategoryService()
                    category = category_service.get_category_by_name(session=session, category_descr=dto.task_category)
                    get_task.category = category

                session.commit()
                session.refresh(get_task)
                return get_task
        except Exception as e:
            session.rollback()
            logger.error(f"Failed to update task, {e}")
            raise ValueError("Failed to update task")

    @staticmethod
    def delete(session: Session, task: int):
        try:
            if not session.query(TaskTodo).filter(TaskTodo.task_id == task).delete():
                raise
            session.commit()
        except Exception as e:
            session.rollback()
            logger.error(f"Failed to delete task, {e}")
            raise ValueError("Failed to delete task, check if task exists")
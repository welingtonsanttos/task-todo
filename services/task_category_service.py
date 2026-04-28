from datetime import datetime

from sqlalchemy.orm import Session
from sqlalchemy import func

from log_config import get_logger
from models.task_category_model import TaskCategory

logger = get_logger(__name__)

class TaskCategoryService:

    @staticmethod
    def create(session: Session, category_descr: str, ins_date: datetime):
        try:
            new_category = TaskCategory(category_description=category_descr, insert_date=ins_date)
            session.add(new_category)
            session.commit()
            return new_category.category_id
        except Exception as e:
            logger.error(e)
            session.rollback()
            raise ValueError("Error during category creation")

    @staticmethod
    def get_category_by_name(session: Session, category_descr: str) -> TaskCategory:
        try:
            category = session.query(TaskCategory).filter(func.UPPER(TaskCategory.category_description) == category_descr.upper()).first()
            if category:
                return category

            new_category = TaskCategory(
                category_description=category_descr.upper(),
                insert_date=datetime.now()
            )
            session.add(new_category)
            session.commit()
            return new_category
        except Exception as e:
            session.rollback()
            logger.error(e)
            raise ValueError("Error during category search")


    @staticmethod
    def get_category_by_id(session: Session, _id: int) -> TaskCategory:
        return session.query(TaskCategory).filter(TaskCategory.category_id == _id).first()

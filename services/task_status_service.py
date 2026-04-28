from sqlalchemy.orm import Session

from log_config import get_logger
from models.task_status_model import TaskStatus
from sqlalchemy import func

logger = get_logger(__name__)


class TaskStatusService:

    @staticmethod
    def get_status_by_name(session: Session, status_name: str) -> TaskStatus | None:
        try:
            status = session.query(TaskStatus).filter(
                func.UPPER(TaskStatus.status_description) == status_name.upper()).first()
            if status:
                return status
        except Exception as e:
            logger.error(e)
            raise ValueError("Status is invalid")

    @staticmethod
    def get_id_by_name(session: Session, status_name: str) -> TaskStatus:
        try:
            status = session.query(TaskStatus).filter(TaskStatus.status_description == func.UPPER(status_name)).first()

            if status:
                return status
        except Exception as e:
            logger.error(e)
            raise ValueError("Status is invalid")

    @staticmethod
    def get_status_by_id(session: Session, status_id: int) -> TaskStatus:
        try:
            status = session.query(TaskStatus).filter(TaskStatus.status_id == status_id).first()
            if status:
                return status
        except Exception as e:
            logger.error(e)
            raise ValueError("Status not found")

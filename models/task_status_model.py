from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, DATETIME
from database_config import Base

class TaskStatus(Base):
    __tablename__  = 'm_task_status'
    status_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    status_description = Column(String(255))
    insert_date = Column(DATETIME)

    task = relationship("TaskTodo", back_populates="status")

    def __repr__(self):
        return f"<Status(StatusId={self.status_id}, StatusDescr={self.status_description}, InsertDate={self.insert_date})>"

    def __str__(self):
        return f"{self.status_description}"


if __name__ == '__main__':
    pass

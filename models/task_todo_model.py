from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database_config import Base, session
from models.task_status_model import TaskStatus
from models.task_category_model import TaskCategory



class TaskTodo(Base):
    __tablename__  = 'tb_tasks'
    task_id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    task_title = Column(String(255), nullable=False)
    task_description = Column(String(255))
    task_status = Column(Integer, ForeignKey('m_task_status.status_id'))
    task_category = Column(Integer, ForeignKey('m_task_category.category_id'))

    status = relationship("TaskStatus", back_populates="task", lazy="joined")
    category = relationship("TaskCategory", back_populates="task", lazy="joined")


if __name__ == '__main__':
    pass

"""    with session as conn:
        result = conn.query(TaskTodo).all()
        print(result)
"""



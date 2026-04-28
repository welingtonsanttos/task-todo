from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer,DATETIME
from database_config import Base

class TaskCategory(Base):
    __tablename__  = 'm_task_category'
    category_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    category_description = Column(String(255), unique=True, nullable=False)
    insert_date = Column(DATETIME)

    task = relationship("TaskTodo", back_populates="category")

    def __repr__(self):
        return f"<Category(CategoryId={self.category_id}, StatusDescr={self.category_description}, InsertDate={self.insert_date})>"

    def __str__(self):
        return f"{self.category_description}"


if __name__ == '__main__':
    pass

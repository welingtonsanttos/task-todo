class TaskUpdateDTO:
    def __init__(self, _id, title, description, status, task_category):
        self.id: int = _id
        self.title: str = title
        self.description: str = description
        self.status: str = status
        self.task_category: str = task_category

    @classmethod
    def from_dict(cls, data: dict):
        dto = cls(
            _id=data.get("id"),
            title=data.get("title"),
            description=data.get("description"),
            status=data.get("status"),
            task_category=data.get("task_category"))
        dto.validate()
        return dto

    def validate(self):
        if not self.id:
            raise ValueError("Id is required")
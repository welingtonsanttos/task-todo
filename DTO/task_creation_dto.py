class TaskCreationDTO:
    def __init__(self, title, description, status, task_category):
        self.title: str = title
        self.description: str = description
        self.status: str = status
        self.task_category: str = task_category

    @classmethod
    def from_dict(cls, data: dict):
        dto = cls(
            title=data.get("title"),
            description=data.get("description"),
            status=data.get("status"),
            task_category=data.get("task_category"))
        dto.validate()
        return dto

    def validate(self):
        if not self.title:
            raise ValueError("Title is required")

        if not self.status:
            raise ValueError("Status is required")

        if not self.task_category:
            raise ValueError("Task category is required")

        if not self.description:
            raise ValueError("Description is required")

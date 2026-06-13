from flask import Flask, request, jsonify

from DTO.task_creation_dto import TaskCreationDTO
from DTO.task_update_dto import TaskUpdateDTO
from database_config import session
from log_config import get_logger
from services.task_service import TaskService

logger = get_logger(__name__)


class TaskController:
    def __init__(self, v_app):
        self.session = session
        self.app = v_app  # , template_folder="../templates"
        self.register_routes()

    def register_routes(self):
        self.app.add_url_rule('/', 'index', self.index)
        self.app.add_url_rule('/api/v1/all-tasks', 'all_tasks', self.all_tasks, methods=["GET"])
        self.app.add_url_rule('/api/v1/task/', 'task_by_id', self.task_by_id, defaults={"task_id": None},
                              methods=["GET"])
        self.app.add_url_rule('/api/v1/task/<int:task_id>', 'task_by_id', self.task_by_id, methods=["GET"])
        self.app.add_url_rule('/api/v1/create', 'create_task', self.create_task, methods=["POST"])
        self.app.add_url_rule('/api/v1/update', 'update_task', self.update_task, methods=["POST"])
        self.app.add_url_rule('/api/v1/delete/', 'delete_task', self.delete_task, defaults={"task_id": None},
                              methods=["DELETE"])
        self.app.add_url_rule('/api/v1/delete/<int:task_id>', 'delete_task', self.delete_task, methods=["DELETE"])

    @staticmethod
    def index():
        return jsonify({"success": True, "msg": "Index page"}), 200

    def all_tasks(self):
        service = TaskService()
        tasks = service.get_all(self.session)

        if not tasks:
            return jsonify({"success": False, "msg": "No tasks found"}), 404

        response = [{"id": task.task_id,
                     "title": task.task_title,
                     "description": task.task_description,
                     "status": task.status.status_description,
                     "task_category": task.category.category_description
                     } for task in tasks]

        return jsonify({"success": True, "data": response}), 200

    def task_by_id(self, task_id: int):
        service = TaskService()
        task = service.get_by_id(session=self.session, task=task_id)

        if not task_id:
            return jsonify({"success": False, "msg": "Task ID is required --> Path: /api/v1/task/{id}"}), 400

        if not task:
            return jsonify({"success": False, "msg": "Task not found"}), 404

        response = ({"id": task.task_id,
                     "title": task.task_title,
                     "description": task.task_description,
                     "status": task.status.status_description,
                     "task_category": task.category.category_description})

        return jsonify({"success": True, "data": response}), 200

    def create_task(self):
        data = request.get_json()

        try:
            task_dto = TaskCreationDTO.from_dict(data)
        except ValueError as e:
            return jsonify({"success": False, "msg": str(e)}), 400
        else:
            logger.info("Task creation request received")
            try:
                service = TaskService()
                new_task = service.create(session=self.session, dto=task_dto)
            except ValueError as e:
                logger.error(f"Failed to create task: {e}")
                return jsonify({"success": False, "msg": "str(e)"}), 400
            else:
                response = ({"id": new_task.task_id,
                             "title": new_task.task_title,
                             "description": new_task.task_description,
                             "status": new_task.task_status,
                             "task_category": new_task.task_category})
                return jsonify({"success": True, "msg": "Task created successfully", "data": response}), 201

    def update_task(self):
        data = request.get_json()

        try:
            task_dto = TaskUpdateDTO.from_dict(data)
        except ValueError as e:
            return jsonify({"success": False, "msg": str(e)}), 400
        else:
            logger.info("Task Update request received")
            try:
                service = TaskService()
                update_task = service.update(session=self.session, dto=task_dto)
            except ValueError as e:
                return jsonify({"success": False, "msg": str(e)}), 400

            if not update_task:
                return jsonify({"success": False, "msg": "Failed to Update Task"}), 400

            response = ({
                "id": update_task.task_id,
                "title": update_task.task_title,
                "description": update_task.task_description,
                "status": update_task.task_status,
                "task_category": update_task.task_category})

            return jsonify({"success": True, "msg": "Task updated successfully", "data": response}), 200

    def delete_task(self, task_id: int):
        logger.info("Task Delete request received")

        if not task_id:
            return jsonify({"success": False, "msg": "Task ID is required --> Path: /api/v1/delete/{id}"}), 400

        try:
            service = TaskService()
            service.delete(session=self.session, task=task_id)
        except ValueError as e:
            return jsonify({"success": False, "msg": str(e)}), 404
        else:
            return jsonify({"success": True, "msg": f"TaskId: {task_id} deleted successfully"}), 200

    def run(self):
        self.app.run(debug=True)


if __name__ == "__main__":
    app = Flask(__name__)
    controller = TaskController(app)
    controller.run()

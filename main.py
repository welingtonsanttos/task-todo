from controller.task_controller import TaskController
from flask import Flask

app = Flask(__name__)
controller = TaskController(app)

if __name__ == "__main__":
    app.run(debug=True)
from controller.task_controller import TaskController


def run():
    app = TaskController()
    app.run()


if __name__ == "__main__":
    run()

from fire import Fire
from src import AppMain
import json

app = AppMain.App()


def parse_cli(task_type, action_type, task_string, project=None):

    obj = parse_task(task_type=task_type)

    common_actions = {
        'add': obj.add(task_string=task_string),
        'active': print(obj.get_active_one_time_tasks()),
    }

    common_actions[action_type]
    app.on_close_operations()


def parse_task(task_type: str):
    task_dict = {
        'task': app.get_one_time_task_object(),
        'habit': app.get_habit_object(),
    }

    return task_dict[task_type]


if __name__ == '__main__':
    Fire(parse_cli)

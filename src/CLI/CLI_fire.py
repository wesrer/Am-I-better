from fire import Fire
from src import AppMain
from typing import List
from functools import partial
import json

app = AppMain.App()


def parse_cli(task_type,
              action_type,
              *args):

    task_type = task_type.lower()

    perform_actions(task_type=task_type,
                    action_type=action_type,
                    args=args)()

    app.on_close_operations()


def perform_actions(task_type, action_type, args):
    obj = parse_task(task_type=task_type)

    if action_type == "add":
        task_string = ' '.join(args)
        return lambda: obj.add(task_string=task_string)

    elif action_type == "active":
        # FIXME:
        return lambda: print(obj.get_active_one_time_tasks())

    elif action_type == "completed":
        return lambda: print(obj.get_completed_one_time_tasks())

    elif action_type == "delete" or action_type == "del":
        task_id = args[0]

        if task_id != "completed":
            print("task_id_is", task_id)
            return lambda: [obj.delete_active_tasks(id_to_delete=x) for x in args]
        else:
            if args[1] == "all":
                if task_type == "task":
                    return lambda: obj.clear_all_completed_tasks()
                elif task_type == "habit":
                    return lambda: obj.clear_all_inactive_tasks()
            else:
                return lambda: [obj.delete_completed_tasks(id_to_delete=x) for x in args[1:]]

    elif action_type == "mark":
        task_id = args[0]

        if task_type.lower() == "task":
            return lambda: obj.mark_as_completed(id_to_mark_as_completed=task_id)
        elif task_type.lo == "habit":
            return lambda: obj.mark_as_inactive(id_to_mark_as_inactive=task_id)

    else:
        raise ValueError(f"{action_type} is not a valid action on {task_type}")


def parse_task(task_type: str):
    task_dict = {
        'task': app.get_one_time_task_object(),
        'habit': app.get_habit_object(),
    }

    return task_dict[task_type]


if __name__ == '__main__':
    Fire(parse_cli)

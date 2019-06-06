from fire import Fire
from src import AppMain
from typing import List
from functools import partial
import json
import sys

app = AppMain.App()


def parse_cli(task_type,
              action_type="list",
              *args):

    task_type = task_type.lower()

    app.on_start_operations()

    perform_actions(task_type=task_type,
                    action_type=action_type,
                    args=args)

    app.on_close_operations()


# FIXME: implement actual pretty printing
def pprint(task_dict):
    for key, value in task_dict.items():
        print(key, value['taskString'], value['weight'])


def print_header(header_string):
    print('-'*100)

    print(' '*50, header_string.upper())

    print('-'*100)


# FIXME: use this in actual code
def parse_args(args):
    properties = dict()
    properties["task_string"] = [x for x in args.split(" ") if ":" not in x].join(" ")

    for item in [x.split(':') for x in args.split(" ") if ":" in x]:
        properties[item[0]] = item[1]

    return properties

# FIXME: refactor this?
def perform_actions(task_type,
                    action_type,
                    args,
                    weight=3):

    if task_type != "all":
        obj = parse_task(task_type=task_type)
    elif action_type in ["list", "view", "active"]:
        print_header("habits")
        perform_actions(task_type="habit",
                        action_type="list",
                        args=[])
        print_header("tasks")
        perform_actions(task_type="task",
                        action_type="list",
                        args=[])
        return

    if action_type == "add":
        task_string = ' '.join(map(str, args))
        obj.add(task_string=task_string)

    elif action_type in ['update', 'edit']:
        # TODO: implement updating priorities / weight / dates
        #       right now you can only update the string
        try:
            print(type(args[0]))
            if type(args[0]) is int:
                id_to_update = int(args[0])
                task_string = " ".join(args[1:])

                obj.update(id_to_update=id_to_update,
                           option_to_update="task_string",
                           updated_value=task_string)
            elif "id" in args:
                raise NotImplementedError
            else:
                print("inside this why?")
                raise TypeError
        except TypeError as err:
            print(err)
            sys.exit("update needs an id to update")
        except NotImplementedError:
            sys.exit("Using id: isn't implemented yet. Sorry!")

    elif action_type in ["active", "list", "view"]:
        pprint(obj.get_active())

    elif action_type == "completed":
        pprint(obj.get_completed())

    elif action_type == "delete" or action_type == "del":
        task_id = args[0]

        if not (task_id == "completed" or task_id == "inactive"):
            [obj.delete_active(id_to_delete=x) for x in args]
        else:
            if args[1] == "all":
                if task_type == "task":
                    obj.clear_all_completed_tasks()
                elif task_type == "habit":
                    obj.clear_all_inactive_tasks()
            else:
                if task_type == "task":
                    [obj.delete_completed(id_to_delete=x) for x in args[1:]]
                elif task_type == "habit":
                    [obj.delete_inactive(id_to_delete=x) for x in args[1:]]

    elif action_type == "mark":
        task_id = args[0]

        if task_type == "task":
            obj.mark_as_completed(id_to_mark_as_completed=task_id)
        elif task_type == "habit":
            obj.mark_as_completed(id_to_mark_as_inactive=task_id)

    else:
        raise ValueError(f"{action_type} is not a valid action on {task_type}")


def parse_task(task_type: str):

    try:
        if task_type == 'task':
            task_object = app.get_one_time_task_object()
        elif task_type == 'habit':
            task_object = app.get_habit_object()
        else:
            raise ValueError
    except ValueError:
        sys.exit("task type is not recognized")

    return task_object


if __name__ == '__main__':
    Fire(parse_cli)

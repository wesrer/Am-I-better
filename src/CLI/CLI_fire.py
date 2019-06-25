from fire import Fire
from src import AppMain

from src.operations.PrettyPrinter import PrettyPrinter
from src.operations.UserInputParser import UserInputParser
from src.events.Actions import Actions

import sys

app = AppMain.App()

PrettyPrinter = PrettyPrinter()
UserInputParser = UserInputParser()
Actions = Actions()


def parse_cli(task_type,
              action_type="list",
              *args):

    task_type = task_type.lower()

    app.on_start_operations()

    perform_actions(task_type=task_type,
                    action_type=action_type,
                    args=args)

    app.on_close_operations()


# FIXME: refactor this?
def perform_actions(task_type,
                    action_type,
                    args,
                    weight=3,
                    default_behavior_exit: bool = True):

    try:
        if task_type not in ["all", "test", "pandas"]:
            obj = parse_task(task_type=task_type)

        elif action_type in ["list", "view", "active", "list:active", "view:active"]:
            PrettyPrinter.print_header("habits")
            perform_actions(task_type="habit", action_type="list", args=[], default_behavior_exit=False)

            PrettyPrinter.print_header("tasks")
            perform_actions(task_type="task", action_type="list", args=[], default_behavior_exit=False)
            return

        # FIXME: the logic here seems completely wrong
        elif action_type in ["inactive", "list:inactive", "view:inactive"]:
            PrettyPrinter.print_header("habits")
            perform_actions(task_type="habit", action_type="inactive", args=[], default_behavior_exit=False)

            PrettyPrinter.print_header("tasks")
            perform_actions(task_type="task", action_type="inactive", args=[], default_behavior_exit=False)
            return

        if "add" in action_type:
            Actions.add(args=args,
                        task_object=obj)

        elif action_type in ['update', 'edit']:
            Actions.update(args=args,
                           task_object=obj)

        elif action_type in ["active", "list", "view"]:
            PrettyPrinter.pprint(task_dict=obj.get_queue(queue="active"),
                                 task_type=task_type,
                                 default_behavior_exit=default_behavior_exit)

        elif action_type == "completed":
            if len(args) == 0:
                PrettyPrinter.pprint(task_dict=obj.get_queue(queue="completed"),
                                     task_type=task_type,
                                     default_behavior_exit=default_behavior_exit)

        elif action_type == "inactive":
            if len(args) == 0:
                PrettyPrinter.pprint(task_dict=obj.get_queue(queue="inactive"),
                                     task_type=task_type,
                                     queue="inactive",
                                     default_behavior_exit=default_behavior_exit)
            else:
                pass # FIXME: implement this

        elif action_type == "delete" or action_type == "del":
            # TODO: implement flexible positioning of the id and the queue identifier
            #       Right now task_id = args[0], and ids = everything else
            task_id = args[0]

            Actions.delete(task_id=task_id,
                           args=args,
                           task_object=obj,
                           task_type=task_type)

        elif "mark" in action_type:
            Actions.mark(task_type=task_type,
                         action_type=action_type,
                         args=args,
                         task_object=obj)

        # TODO: implement unmarking inactive habits
        elif action_type == "unmark":
            Actions.unmark(task_type=task_type,
                           task_object=obj,
                           args=args)

        else:
            raise ValueError
    except ValueError:
        sys.exit(f"{action_type} is not a valid action on {task_type}")
    except NotImplementedError:
        sys.exit(f"Viewing all inactive")


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

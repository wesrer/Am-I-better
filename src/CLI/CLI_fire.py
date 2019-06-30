from fire import Fire
from src import AppMain

from src.operations.PrettyPrinter import PrettyPrinter
from src.operations.UserInputParser import UserInputParser
from src.operations.ValidValues import ValidValues
from src.events.Actions import Actions

import sys

app = AppMain.App()

PrettyPrinter = PrettyPrinter()
UserInputParser = UserInputParser()
ValidValues = ValidValues()
Actions = Actions()


def parse_cli(task_type,
              action_type="active",
              *args):

    # print("task_type", type(task_type), task_type)
    # print("action_type", type(action_type), action_type)
    # print("args", type(args), args)

    task_type = task_type.lower()
    action_type = action_type.lower()

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
        if task_type in ["all", "list"]:
            queue = action_type  # a better name for what the value is in this case

            if queue in ValidValues.get_valid_queues():
                perform_actions(task_type="habits", action_type=queue, args=[], default_behavior_exit=False)
                perform_actions(task_type="tasks", action_type=queue, args=[], default_behavior_exit=False)
                return

        else:
            obj = parse_task(task_type=task_type)

        if "add" in action_type:
            Actions.add(args=args,
                        task_object=obj)

        elif action_type in ['update', 'edit']:
            Actions.update(args=args,
                           task_object=obj)

        # NOTE: "list" and "view" used to be valid action_types, but I think they complicate the logic
        #       a bit too much and supporting them leads to no long term benefit. I may be wrong, but
        #       I'm not planning on supporting them for version 1 at least
        elif action_type in ValidValues.get_valid_queues():
            if len(args) == 0:
                PrettyPrinter.print_header(task_type)
                PrettyPrinter.pprint(task_dict=obj.get_queue(queue=action_type),
                                     task_type=task_type,
                                     default_behavior_exit=default_behavior_exit)
            else:
                pass # FIXME: implement this

        elif action_type == "delete" or action_type == "del":
            # TODO: implement flexible positioning of the id and the queue identifier
            #       Right now task_id = args[0], and ids = everything else

            if type(args[0]) is int:
                queue = "active"
            elif type(args[0]) is str:
                queue = args[0]

            Actions.delete(queue=queue,
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
        if task_type in ['task', 'tasks']:
            task_object = app.get_one_time_task_object()
        elif task_type in ['habit', 'habits']:
            task_object = app.get_habit_object()
        else:
            raise ValueError
    except ValueError:
        sys.exit("task type is not recognized")

    return task_object


if __name__ == '__main__':
    Fire(parse_cli)

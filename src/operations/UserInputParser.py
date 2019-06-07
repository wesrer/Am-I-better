class UserInputParser:
    def __int__(self):
        pass

    @staticmethod
    def find_properties(args):
        properties = dict()

        for item in [str(x).split(':') for x in str(args).split(" ") if ":" in x]:
            properties[item[0]] = item[1]

        return properties

    # FIXME: find a better module for this to be in
    @staticmethod
    def tuple_to_string(value):
        print(type(value))
        if isinstance(value, tuple):
            return ''.join([str(x) for x in value])
        else:
            return str(value)

    def generate_task_string(self, args):
        task_string = [self.tuple_to_string(x) for x in args if ":" not in str(x)]

        return" ".join(task_string)


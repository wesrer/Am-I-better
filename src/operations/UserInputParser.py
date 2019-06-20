class UserInputParser:
    def __int__(self):
        pass

    # makes a list of all the additional options that the user included
    def find_properties(self, args):
        properties = dict()

        # first split the string into words, and make a list of the words
        # with the ':' character in it
        # loop through the list and split the word into two parts with ':' as the
        # separator. Create a dictionary with the left side is the property name,
        # and the right side as the property value.
        # TODO: add "=" support in the future
        # FIXME:
        for item in [str(x).split(':') for x in args if ":" in x]:
            properties[item[0]] = item[1]

        return properties

    # FIXME: find a better module for this to be in
    @staticmethod
    def tuple_to_string(value, joinwith):
        if isinstance(value, tuple):
            return joinwith.join([str(x) for x in value])
        else:
            return str(value)

    def generate_task_string(self, args):
        task_string = [self.tuple_to_string(x, joinwith='') for x in args if ":" not in str(x)]
        return ' '.join(task_string)

    def generate_list_of_ids(self, args):
        if len(args) == 1:
            for item in args:
                # case 1: when only one is given
                if type(item) is int:
                    return [item]

                # case 2: when a list of ids are given
                elif type(item) is tuple:
                    return [element for element in item]
        else:
            # FIXME: hacky approach. might fix later
            return self.generate_task_string(args).split(' ')




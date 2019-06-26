class UserInputParser:
    def __int__(self):
        pass

    # makes a list of all the additional options that the user included
    @staticmethod
    def find_properties(args):
        properties = dict()

        # first split the string into words, and make a list of the words
        # with the ':' character in it
        # loop through the list and split the word into two parts with ':' as the
        # separator. Create a dictionary with the left side is the property name,
        # and the right side as the property value.
        # TODO: add "=" support in the future
        # FIXME:

        words_with_properties = [str(x).split(':') for x in args if ":" in str(x)]
        for item in words_with_properties:
            properties[item[0]] = item[1]

        return properties

    # FIXME: find a better module for this to be in
    @staticmethod
    def tuple_to_string(value, joinwith):
        if isinstance(value, tuple):
            return joinwith.join([str(x) for x in value])
        else:
            return str(value)

    # FIXME: find a better module for this to be in
    def index_of_first_string(self, args):
        for index, value in enumerate(args, start=0):
            if type(value) is str:
                return index

    def generate_task_string(self, args):

        index_of_first_string = self.index_of_first_string(args=args)
        args_without_ids = args[index_of_first_string:]

        task_string = [self.tuple_to_string(x, joinwith='') for x in args_without_ids if ":" not in str(x)]
        return ' '.join(task_string)

    def generate_list_of_ids(self, args, list_of_ids=None):
        if list_of_ids is None:
            list_of_ids = []

        for item in args:
            if type(item) is int:
                list_of_ids.append(str(item))
            elif type(item) is tuple:
                self.generate_list_of_ids(args=item, list_of_ids=list_of_ids)
            elif type(item) is str:
                return list_of_ids

        return list_of_ids




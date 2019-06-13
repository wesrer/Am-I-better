class PrettyPrinter:
    @staticmethod
    def print_header(header_string):
        print('-'*100)
        print(' '*50, header_string.upper())
        print('-'*100)

    # FIXME: implement actual pretty printing

    @staticmethod
    def pprint(task_dict):
        for key, value in task_dict.items():
            print(key, value['taskString'], value['weight'])

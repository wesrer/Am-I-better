class ValidValues:
    def __init__(self):
        self.valid_queues = ["active", "inactive", "completed", "scheduled"]

    def get_valid_queues(self):
        return self.valid_queues

    def generate_valid_values_for_queue(self):
        pass

    def add_queue(self, queue_name: str):
        self.valid_queues.append(queue_name)

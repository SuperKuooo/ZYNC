class _ObserverLog:
    def __init__(self):
        self.last_success = None
        self.last_attempt = None
        self.total_attempts = None
        self.save_directory = None

    def get_latest_log(self):
        """ Get the details of the handler

        :return: returns all the details in a list
        """
        return [self.last_success, self.last_attempt, self.total_attempts, self.save_directory]


class TransferredFiles:
    number_of_transferred = 0
    def __init__(self, location, time, name):
        self.location = location
        self.time = time
        self.name = name
    
    def get_location(self):
        return self.location

    def get_time(self):
        return self.time
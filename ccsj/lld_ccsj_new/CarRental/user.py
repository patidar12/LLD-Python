from unique_id_generator import UniqueIDGenerator

class User:
    def __init__(self, uname, driving_license):
        self.uid = UniqueIDGenerator.next_id()
        self.uname = uname
        self.driving_license = driving_license

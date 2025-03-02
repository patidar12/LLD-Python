import threading

class UniqueIDGenerator:
    UNIQUE_ID = 0
    __lock = threading.Lock()
    @classmethod
    def next_id(cls):
        with cls.__lock:
            cls.UNIQUE_ID += 1
            return cls.UNIQUE_ID
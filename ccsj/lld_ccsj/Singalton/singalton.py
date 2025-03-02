import threading

class Singalton(type):
    __instances = {}
    _lock = threading.Lock()
    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            with cls._lock:
                if cls not in cls.__instances:
                    cls.__instances[cls] = super(Singalton, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]

# example how to use and create a class singalton.
class MySingalton(metaclass=Singalton):
    pass


# print(MySingalton())
# print(MySingalton())


# to check the behavious of singalton, using multiple threads

def create_singalton_instance():
    singalton_instance = MySingalton()
    print("INstance Id: ", id(singalton_instance))

threads = []

for _ in range(15):
    t = threading.Thread(target=create_singalton_instance)
    threads.append(t)
    t.start()


for t in threads:
    t.join()
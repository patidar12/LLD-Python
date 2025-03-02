class Product:
    def __init__(self, pid: int, name: str):
        self.__pid: int = pid
        self.__name: str = name
    
    def get_pid(self):
        return self.__pid
    
    def get_name(self):
        return self.__name

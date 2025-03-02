from file_system import FileSystem

class File(FileSystem):
    def __init__(self, name: str):
        self.name = name
    
    def ls(self) -> None:
        print("File name: ", self.name)

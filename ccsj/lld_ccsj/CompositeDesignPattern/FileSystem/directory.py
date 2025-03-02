from file_system import FileSystem

class Directory(FileSystem):
    def __init__(self, name: str):
        self.name: str = name
        self.file_system: FileSystem = set()
    
    def add(self, file_system: FileSystem) -> None:
        self.file_system.add(file_system)
    
    def ls(self):
        print("Directory Name: ", self.name)
        for obj in self.file_system:
            obj.ls()

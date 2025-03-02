from typing import List
from file_system import FileSystem

class Directory(FileSystem):
    def __init__(self, name):
        self.name = name
        self.objects: List[FileSystem] = []
    
    def add(self, object: FileSystem):
        self.objects.append(object)
    
    def ls(self):
        print(f"directory name: {self.name}")
        for object in self.objects:
            object.ls()

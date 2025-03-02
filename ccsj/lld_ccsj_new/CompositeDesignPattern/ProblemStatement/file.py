class File:
    def __init__(self, name):
        self.name = name
    
    def ls(self):
        print(f"file name: {self.name}")
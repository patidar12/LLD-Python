class Directory:
    def __init__(self, name):
        self.name = name
        self.objects = []
    
    def add(self, object):
        self.objects.append(object)
    
    def ls(self):
        print(f"directory name: {self.name}")
        for object in self.objects:
            object.ls()



'''
In above scenario in other language we may need to do typecasting,
When calling objects.ls() in loop. Because we don't know wheter it is file or directory objects.
In python function call resolution happen at runtime so it will not raise any error but it is
not clear that it is file or directory ls method.
'''
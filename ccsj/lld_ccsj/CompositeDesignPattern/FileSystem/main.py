from directory import Directory
from file import File
from file_system import FileSystem

class FileDriver:
    
    @classmethod
    def create_file_system(self) -> FileSystem:
        movie_directory = Directory("Movie")
        border = File("Border")
        comedy_movies = Directory("Comedy Movies")
        comedy_movies.add(File("Hangama"))
        movie_directory.add(border)
        movie_directory.add(comedy_movies)
        return movie_directory
    @classmethod
    def print_file_system(self, file_system: FileSystem):
        file_system.ls()


file_system = FileDriver.create_file_system()
FileDriver.print_file_system(file_system)

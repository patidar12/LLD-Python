from directory import Directory
from file import File

class FileSystem:
    def test(self):
        movie_folder = Directory("Movie")
        border = File("Border")
        movie_folder.add(border)
        comedy_movie_folder = Directory("ComedyMovie")
        hulchul = File("HulChul")
        comedy_movie_folder.add(hulchul)
        movie_folder.add(comedy_movie_folder)
        movie_folder.ls()


FileSystem().test()
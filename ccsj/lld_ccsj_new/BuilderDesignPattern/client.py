from enginnering_student_builder import EngineeringStudentBuilder
from mba_student_builder import MbaStudentBuilder
from director import Director

class Client:
    def manage_student_creation(self):
        director_obj1 = Director(EngineeringStudentBuilder())
        director_obj2 = Director(MbaStudentBuilder())

        engineer_student = director_obj1.create_student()
        mba_student =director_obj2.create_student()
        print(engineer_student)
        print(mba_student)

Client().manage_student_creation()
from enginnering_student_builder import EngineeringStudentBuilder
from mba_student_builder import MbaStudentBuilder
from student_builder import StudentBuilder

class Director:
    def __init__(self, builder: StudentBuilder):
        self.student_builder: StudentBuilder = builder
    
    def create_student(self):
        if isinstance(self.student_builder, EngineeringStudentBuilder):
            return self.create_engineering_student()
        if isinstance(self.student_builder, MbaStudentBuilder):
            return self.create_mba_stident()

        
    def create_engineering_student(self):
        student_builder: EngineeringStudentBuilder =self.student_builder
        return student_builder.set_roll_number(1).set_age(22).set_name("sj").set_subjects().build_student()


    def create_mba_stident(self):
        student_builder: MbaStudentBuilder =self.student_builder
        return student_builder.set_roll_number(1).set_age(22).set_name("sj").set_father_name("MyFatherName").set_mother_name("MyMotherName").set_subjects().build_student()


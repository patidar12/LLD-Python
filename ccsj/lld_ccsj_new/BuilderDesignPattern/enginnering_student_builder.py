from student_builder import StudentBuilder

class EngineeringStudentBuilder(StudentBuilder):
    def set_subjects(self):
        self.subjects = ["DSA", "OS", "Computer Architecture"]
        return self

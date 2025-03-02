from student_builder import StudentBuilder

class MbaStudentBuilder(StudentBuilder):
    def set_subjects(self):
        self.subjects = ["Micro Economics", "Business Studies", "Operations Management"]
        return self

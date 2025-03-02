from typing import List

class Student:
    def __init__(self, builder):
        self.roll_number: int = builder.roll_number
        self.age: int = builder.age
        self.name: str = builder.name
        self.father_name: str = builder.father_name
        self.mother_name: str = builder.mother_name
        self.subjects: List[str] = builder.subjects

    def __str__(self):
        result =  f"roll_no: {self.roll_number}  age: {self.age}  name: {self.name}  father_name: {self.father_name} \
        mother_name: {self.mother_name}"
        for subject in self.subjects:
            result = result + "  " + subject
        return result


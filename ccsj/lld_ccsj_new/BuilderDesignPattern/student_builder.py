from typing import List
from abc import ABC, abstractmethod

from student import Student

class StudentBuilder(ABC):
    def __init__(self):
        self.roll_number: int = None
        self.age: int = 0
        self.name: str = None
        self.father_name: str = None
        self.mother_name: str = None
        self.subjects: List[str] = []

    def set_roll_number(self, roll_number: int):
        self.roll_number = roll_number
        return self

    def set_age(self, age: int):
        self.age = age
        return self

    def set_name(self, name: str):
        self.name = name
        return self

    def set_father_name(self, father_name: str):
        self.father_name = father_name
        return self

    def set_mother_name(self, mother_name: str):
        self.mother_name = mother_name
        return self

    def build_student(self):
        return Student(builder=self)

    @abstractmethod
    def set_subjects(self):
        pass
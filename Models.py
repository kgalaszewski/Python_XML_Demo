from enum import Enum

class SchoolPersonType(Enum):
    TEACHER = 1,
    STUDENT = 2

# uncomment if you would like to specify list of available professions
# class TeacherProfession(Enum):
#     MATH = 1,
#     SCIENCE = 2,
#     IT = 3,
#     PHYSICAL_EDUCATION = 4


class Person:
    def __init__(self):
        self.name
        self.age
        self.person_type

    def __repr__(self):
        return f'name={self.name}, age={self.age}, type={self.person_type}'

    def obj_to_dict(self):
        return {
            'Person-Type': self.person_type.name,
            'Name': self.name,
            'Age': self.age
        }
        


class Student(Person):
    def __init__(self, grades_dict: dict):
        self.grades_dict = grades_dict

    def __repr__(self):        
        return f'grades={self.grades_dict} + {super().__repr__()}'
        
    def obj_to_dict(self):
        return {
            **super().obj_to_dict(),
            'Grades': self.grades_dict
        }


class Teacher(Person):
    def __init__(self, profession):
        self.profession = profession

    def __repr__(self):
        return f'profession={self.profession} + {super().__repr__()}'
        
    def obj_to_dict(self):
        return {
            **super().obj_to_dict(),
            'Profession': self.profession
        }

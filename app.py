from Models import Student, Teacher, SchoolPersonType
from XmlSerializing import MySerializer
from colorama import Fore


# pseudo-logger decorator method just for learning purpose
def my_Program_logger(func):
    def wraper(*args, **kwargs):
        try:
            print(Fore.YELLOW + 'Program execution has started ....')
            print(Fore.YELLOW + '----------------------------------')
            func(*args, **kwargs)
            print(Fore.YELLOW + 'Program execution has finished ...')
            print(Fore.YELLOW + '----------------------------------')
        except Exception as ex:
            print(Fore.RED + f'Program execution has failed due to {str(ex)}')
    

class PersonCreator:
    # learning purpose - create person decorator method
    @classmethod
    def create_person(cls, create_student_or_teacher):
        def creation_wrapper(*args, **kwargs):
            person = create_student_or_teacher(*args, **kwargs)
            person.name = input('What is his/her name ? ')
            person.age = input('What is his/her age ? ')
            return person
        return creation_wrapper


class Program:
    def __init__(self):
        self.__run()

    def __run(self):
        val = input("If you want to create a Student, type 's', for Teacher, type 't'")
        if not val or not len(val) == 1:
            raise ValueError('Input is not valid, please try again')

        if 's' in val:
            person = self.__create_student()
            person.person_type = SchoolPersonType.STUDENT
        elif 't' in val:
            person = self.__create_teacher()
            person.person_type = SchoolPersonType.TEACHER
        else:
            print(f'Type {val} is not supported yet in our app')
            return

        serializer = MySerializer()
        serializer.serialize_person(person)

    @PersonCreator.create_person
    def __create_student(self) -> Student:
        grade = input('Enter the grade you would like to give for the student')
        subject = input('What subject does the grade relate to ?')
        student = Student({subject: grade})
        return student

    @PersonCreator.create_person
    def __create_teacher(self) -> Teacher:
        prof = input("What is the teacher's profession ? ")
        teacher = Teacher(prof)        
        return teacher




# START ! ! ! 
# Starting program execution by Instantiating it
Program()    

import Models
from dicttoxml import dicttoxml
import os
from colorama import Fore

# my pseudo logger - just to learn the decorator method in python
def run_pseudo_logger(func):
    def wrapper(*args, **kwargs):
        print(Fore.GREEN + 'Running serializer')
        try:
            func(*args, **kwargs)
            print(Fore.GREEN + 'Successfuly finished serializing')
        except Exception as ex:
            print(Fore.RED + f'Could not serialize person due to {str(ex)}')
        print(Fore.GREEN + 'Serializer finished its job')
    return wrapper


FILE_NAME = 'StudentTeacherList.xml'

class MySerializer:    
    def __init__(self, file_name: str = FILE_NAME):
        self.file_name = file_name

    @run_pseudo_logger
    def serialize_person(self, person: Models.Person):
        serialized_person = dicttoxml(person.obj_to_dict())
        text = self.__read_file()

        if any(text):
            text = text[:-7]
            text += str(serialized_person)[47:-1]
        else:
            text += str(serialized_person)[2:-1]

        self.__write_to_file(text)

    def __read_file(self) -> str:
        text = ''
        if os.path.exists(self.file_name):
            with open(self.file_name, mode="r") as current_file:
                text = current_file.read()
        return text

    def __write_to_file(self, text: str):
        with open(self.file_name, mode='w') as my_file:
            my_file.write(text)



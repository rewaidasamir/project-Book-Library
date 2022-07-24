from Client import Client


class Librarian(Client):
    def __init__(self, id, full_name, age, id_no, phone_number,salary):
        super().__init__(id, full_name, age, id_no,phone_number)
        self.__salary = salary

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary
class Client:

    def __init__(self,id,full_name,age,id_no,phone_number):
        self.id = id
        self.full_name = full_name
        self.age = age
        self.id_no = id_no
        self.phone_number = phone_number

    def set_id(self,id):
        self.id = id

    def set_full_name(self, full_name):
        self.full_name = full_name

    def set_age(self, age):
        self.age = age

    def set_id_no(self, id_no):
        self.id_no = id_no

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def get_phone_number(self):
        return self.phone_number

    def get_id(self):
        return self.id

    def get_full_name(self):
        return self.full_name

    def get_age(self):
        return self.age

    def get_id_no(self):
        return self.id_no



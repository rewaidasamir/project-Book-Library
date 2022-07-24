class Book:
    def __init__(self, id, title, description, author, status: bool):
        self.__id = id
        self.__title = title
        self.__description = description
        self.__author = author
        self.__status = status

    def set_id(self, id):
        self.__id = id

    def set_title(self, title):
        self.__title = title

    def set_description(self, description):
        self.__description = description

    def set_author(self, author):
        self.__author = author

    def set_status(self, status):
        self.__status = status

    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_description(self):
        return self.__description

    def get_author(self):
        return self.__author

    def get_status(self):
        if self.__status:
            return "Active"
        else:
            return "In-active"
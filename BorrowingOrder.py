class BorrowingOrder:
    def __init__(self, id, start_date, end_data, client_id, book_id, status):
        self.__id = id
        self.__start_date = start_date
        self.__end_date = end_data
        self.__client_id = client_id
        self.__book_id = book_id
        self.__status = status

    def set_id(self, id):
        self.__id = id

    def set_start_date(self, start_date):
        self.__start_date = start_date

    def set_end_date(self, end_date):
        self.__end_date = end_date

    def set_client_id(self, client_id):
        self.__client_id = client_id

    def set_book_id(self, book_id):
        self.__book_id = book_id

    def set_status(self, status):
        self.__status = status

    def get_id(self):
        return self.__id

    def get_start_date(self):
        return self.__start_date

    def get_end_date(self):
        return self.__end_date

    def get_client_id(self):
        return self.__client_id

    def get_book_id(self):
        return self.__book_id

    def get_status(self):
        return self.__status
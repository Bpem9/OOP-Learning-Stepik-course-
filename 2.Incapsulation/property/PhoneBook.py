import re


class PhoneBook:
    def __init__(self):
        self.phonebook = []

    def add_phone(self, phone):
        self.phonebook.append(phone)

    def remove_phone(self, indx):
        self.phonebook.pop(indx)

    def get_phone_list(self):
        return self.phonebook


class PhoneNumber:
    def __init__(self, number, fio):
        if re.fullmatch(r'[0-9]{11}', str(number)):
            self.number = number
        if isinstance(fio, str):
            self.fio = fio
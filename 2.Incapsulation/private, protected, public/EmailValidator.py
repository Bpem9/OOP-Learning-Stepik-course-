from random import choice
import re

class EmailValidator:
    __CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._"
    # def __new__(cls, *args, **kwargs):
    #     None
    def __init__(self):
        # self.email = email
        pass

    @staticmethod
    def __is_email_str(email):
        return isinstance(email, str)
    @classmethod
    def get_random_email(cls):
        return ''.join([choice(cls.__CHARS) for _ in range(10)]) + '@gmail.com'
    @classmethod
    def check_email(cls, email):
        if cls.__is_email_str(email):
            name = re.search(r'([a-zA-Z0-9._]+)(?=@)', email).group(0)
            domen = re.search(r'(?<=@)[a-zA-Z._]+', email).group(0)
            if len(domen) <= 50 and len(name) <= 100:
                if '.' in domen and not '..' in email:
                    return True
            return False

email = EmailValidator().get_random_email()
print(email)
print(EmailValidator().check_email(email))
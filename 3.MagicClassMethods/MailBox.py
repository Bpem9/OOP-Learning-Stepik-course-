import sys

class MailBox:
    def __init__(self):
        self.inbox_list = []
    def receive(self):
        lst_in = ['sc_lib@list.ru; От Балакирева; Успехов в IT!',
                  'mail@list.ru; Выгодное предложение; Вам одобрен кредит.',
                  'mail123@list.ru; Розыгрыш; Вы выиграли 1 млн. руб. Переведите 30 тыс. руб., чтобы его получить.']
        for mail in lst_in:
            mail_from, title, content = mail.split('; ')
            self.inbox_list.append(MailItem(mail_from, title, content))
        print(self.inbox_list)


class MailItem:
    def __init__(self, mail_from, title, content):
        self.mail_from = mail_from
        self.title = title
        self.content = content
        self.is_read = False
    def set_read(self, fl_read):
        self.is_read = fl_read
    def __bool__(self):
        return self.is_read
    def __repr__(self):
        return self.title

mail = MailBox()
mail.receive()
mail.inbox_list[0].set_read(True)
mail.inbox_list[-1].set_read(True)
inbox_list_filtered = list(filter(lambda x: bool(x), mail.inbox_list))
print(inbox_list_filtered)
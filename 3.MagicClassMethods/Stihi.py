stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]

class StringText:
    def __init__(self, lst_words):
        self.lst_words = list(lst_words)
    def __len__(self):
        return len(self.lst_words)
    def __lt__(self, other):
        return len(self) < len(other)
    def __le__(self, other):
        return len(self) <= len(other)

blocked_chars = "–?!,.;"

lst_text = [StringText(x.strip(blocked_chars) for x in line.split() if len(x.strip(blocked_chars)) > 0) for line in stich]
lst_text_sorted = sorted(lst_text, reverse=True)
lst_text_sorted = [' '.join(x.lst_words) for x in lst_text_sorted]
print(lst_text_sorted)



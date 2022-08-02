import string
import random
import re


def matching(string):
    pattern2 = r'\w+'
    pattern = r'([\w.@]+)@(gmail.com)$'
    if re.fullmatch(pattern, string):
        print('Совпадает')
    else:
        print('Облом')


def len_domen(string):
    string1 = re.search(r'(?<=@)', string)
    print(len(string1.group(1)))

# matching('alskd')
# matching('09@gmail.com')
# matching('09..@@gmail.com')
len_domen('09..@@gmail.com')
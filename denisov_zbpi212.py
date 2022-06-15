import json
from functools import reduce
from statistics import mean


def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x - 1)



def filter_even(li):
    return list(filter(lambda x: x % 2 == 0, li))



def square(li):
    return list(map(lambda x: pow(x, 2), li))



def bin_search(li, element):
    if len(li) == 0:
        return -1
    left = 0
    right = len(li) - 1
    while left < right:
        index = left + (right - left) // 2
        if li[index] > element:
            right = index - 1
        elif li[index] < element:
            left = index + 1
        else:
            return index
    index = left + (right - left) // 2
    if left == right and li[index] == element:
        return index
    return -1



def is_palindrome(string):
    filtered_string = list(filter(lambda x: x.isalpha(), string.lower()))
    i = 0
    j = 0 if len(filtered_string) == 0 else len(filtered_string) - 1
    while i < j:
        if (ord(filtered_string[i]) != ord(filtered_string[j])):
            return 'NO'
        i += 1
        j -= 1
    return 'YES'



def calculate(path2file):
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '//': lambda x, y: x // y,
        '%': lambda x, y: x % y,
        '**': lambda x, y: pow(x, y),
    }
    with open(path2file) as f:
        lines = f.readlines()
        results = []
        for i in range(len(lines)):
            line_content = lines[i].split()
            results.append(operations[line_content[0]](int(line_content[1]), int(line_content[2])))
        return reduce(lambda x, y: str(x) + ',' + str(y), results)



def substring_slice(path2file_1, path2file_2):
    with open(path2file_1) as f_1, open(path2file_2) as f_2:
        lines = f_1.readlines()
        intervals = f_2.readlines()
        results = []
        for i in range(len(lines)):
            interval = intervals[i].split()
            results.append(lines[i][int(interval[0]):int(interval[1]) + 1])
        return " ".join(results)



def decode_ch(string_of_elements):
    with open('periodic_table.json', encoding="utf-8") as table:
        dict = json.load(table)
        result = ''
        element = ''
        for i in range(len(string_of_elements)):
            element += string_of_elements[i]
            if element in dict and (i == len(string_of_elements) - 1 or string_of_elements[i + 1].isupper()):
                result += dict[element]
                element = ''
        return result



class Student:
    def __init__(self, name, surname, grades=[3, 4, 5]):
        self.name = name
        self.surname = surname
        self.fullname = name + ' ' + surname
        self.grades = grades

    def greeting(self):
        return 'Hello, I am Student'

    def mean_grade(self):
        return mean(self.grades)

    def is_otlichnik(self):
        return 'YES' if self.mean_grade() >= 4.5 else 'NO'

    def __add__(self, other):
        return self.name + ' is friends with ' + other.name

    def __str__(self):
        return self.fullname



class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg
        super().__init__(self.msg)

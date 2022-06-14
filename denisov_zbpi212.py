def fact(x):
    if x <=1:
      return 1
    else:
        return (x* fact(x-1))


def filter_even(li):
  even_li= list(filter(lambda x: x%2==0,li))
  return even_li



def square(li):
  squares_li = list(map(lambda x: x**2,li))
  return squares_li




def bin_search(li, element):
    low=0
    high=len(li)-1
    mid=0
    while low<=high:
        mid = (high + low)//2
        if li[mid]<element:
            low = mid+1
        elif li[mid]>element:
            high = mid-1
        else: 
            return mid
    return -1


def is_palindrome(string):
    string=string.lower()
    string= ''.join(filter(str.isalpha, string))
    
    left=0
    right=len(string)-1
    palindrome='YES'
    
    while left < right:
        if string[left] == string[right]:
            left=left+1
            right=right-1
        else:
            palindrome='NO'
            break
    return palindrome




def calculate(path2file):
    with open (path2file, 'r', encoding='utf-8') as f:
        out=[]
        for line in f:
            lst=line.split()
            lst[1],lst[0] = lst[0],lst[1]
            lst=''.join(lst)
            res=eval(lst)
            out.append(res)
        out=', '.join(str(x) for x in out)
        return(out)




def substring_slice(path2file_1,path2file_2):
     with open(path2file_1) as f1, open(path2file_2) as f2:
          with open("3.txt", "w")as f3:
               n1 = f1.read().splitlines()
               n2 = f2.read().splitlines()
               for i in range(len(n1)):
                   f3.writelines(n1[i] + ' ' + n2[i]+ '\n')
               
     with open('3.txt') as file:
          res=[]
          for line in file:
               line=line.split()
               start, end=int(line[1]), int(line[2])+1
               string=line[0]
               changed= string[start:end]
               res.append(changed)
          res=' '.join(str(x) for x in res)
          return(res)



def decode_ch(sting_of_elements):
    encodedString = ''
    import re
    string= re.sub(r'([A-Z])', r' \1', sting_of_elements).split()
    for el in string:
        encodedString += periodic_table[el]
    return encodedString



class Student:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.fullname= '{} {}'.format(name, surname)
        #print('Student exict') #for me
     
    def greeting(self): #метод экземпляра
        return 'Hello, I am '+ str(Student) 

    grades=[3,4,5] #не очень понимаю зачем нам атрибут класса, если мы его и так подаем каждому студенту подаем аргументом дефолт
    def __init__(self, name, surname, grades=[3,4,5]):
        self.name = name
        self.surname = surname
        self.fullname= '{} {}'.format(name, surname)
        self.grades =grades

    def mean_grade(self): 
        mg = mean(self.grades)
        return mg

    def is_otlichnik(self):   
        if self.mean_grade()>= 4.5:
            return 'YES'
        else:
            return 'NO'

    def __add__(self, other):
        if isinstance(other, Student):
            return '{Name1} is friends with {Name2}'.format(Name1=self.name, Name2=other.name)

    def __str__(self):
        return self.fullname



class MyError(Exception):

     def __init__(self, msg):
          self.msg = msg





# TODO 여기서부터



class Person:
    def __init__(self):
        self.name = ''
        self.age = 0
        self.contact = '000-0000-0000'

    def input_information(self):
        self.name = input('이름:')
        self.age = int(input('나이:'))
        self.contact = input('연락처(XXX-XXXX-XXXX):')

    def print_information(self):
        print(f'이름 : {self.name}\n나이 : {self.age}세\n연락처 : {self.contact}')

    def add_age(self, n: int):
        self.age += n
        print(f'나이가 {n}살 증가하여 {self.age}살이 되었습니다.')

    def is_adult(self):
        return self.age >= 20


p1 = Person()
p1.input_information()
p1.print_information()
p1.add_age(1)
if p1.is_adult():
    print('성인')
else:
    print('미성년')

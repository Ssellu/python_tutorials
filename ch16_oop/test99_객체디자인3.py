
"""
    Person 클래스 발전시키기
     => 함수는 1가지 일만 해야한다.
"""

class Person:
    def __init__(self, name='', age=0, contact='000-0000-0000'):
        self.name = name
        self.age = age
        self.contact = contact

    def introduce(self):
        print(f'저의 이름은 {self.name}이고, 나이는 {self.age}, 연락처는 {self.contact} 입니다.')

    def input_information(self):
        d1 = input('이름:')
        d2 = int(input('나이:'))
        d3 = input('연락처(XXX-XXXX-XXXX):')
        self.save_information(d1, d2, d3)

    def save_information(self, n: str = '없음', a: int = 0, c: str = '000-0000-0000'):
        self.name = n
        self.age = a
        self.contact = c
        print('정보 저장 완료!')

    def add_age(self, n: int):
        self.age += n
        print(f'나이가 {n}살 증가하여 {self.age}살이 되었습니다.')

    def is_adult(self):
        return self.age >= 20

    def get_information(self):
        return f'이름 : {self.name}\n나이 : {self.age}세\n연락처 : {self.contact}'

    def print_information(self):  # get_information()을 통해 문자열을 반환받아 이를 출력한다.
        print(self.get_information())

p1 = Person()
p1.input_information()
p1.print_information()
p1.add_age(1)
if p1.is_adult():
    print('성인')
else:
    print('미성년')

# 방금전 예시와 결과는 똑같지만 기능(역할)별로 메서드가 세부화된 것을 확인하자!

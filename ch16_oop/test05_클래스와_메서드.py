class Person:
    def __init__(self, name: str = '', age: int = 0, contact: str = '000-0000-0000'):
        self.name = name
        self.age = age
        self.contact = contact

    # 메서드 정의 (정의 순서 상관없음)
    def input_information(self):
        self.name = input('이름:')
        self.age = int(input('나이:'))
        self.contact = input('연락처(XXX-XXXX-XXXX):')
        # contact = input('연락처(XXX-XXXX-XXXX):')
        # 이 경우 contact 는 Person 필드가 아니라 input_information() 메서드의 지역변수다.

    def print_information(self):
        print(f'이름 : {self.name}\n나이 : {self.age}세\n연락처 : {self.contact}')


a = Person()
b = Person('홍길동', 15, '010-1111-2222')

a.input_information()
a.print_information()

b.print_information()


"""
     함수의 내용이 특정 객체를 위한 내용이라면 클래스에 담을 것!
"""
class Pokemon0:
    def __init__(self):
        self.name = ''
        self.level = 1

def print_pokemon(p:Pokemon0):
    print(f'{p.name} / LV.{p.level}')

def save_pokemon(p:Pokemon0):
    p.name = input('새 포켓몬 이름:')
    p.level = int(input(f'{p.name}의 레벨:'))


pok1 = Pokemon0()
save_pokemon(pok1)
print_pokemon(pok1)
# 이 방식은 절차적 방식


# 올바른 방식
class Pokemon1:
    def __init__(self):
        self.name = ''
        self.level = 1

    def print_pokemon(self):
        print(f'{self.name} / LV.{self.level}')

    def save_pokemon(self):
        self.name = input('새 포켓몬 이름:')
        self.level = int(input(f'{self.name}의 레벨:'))

pok1 = Pokemon1()
pok1.save_pokemon()
pok1.print_pokemon()
# 객체 스스로 일을 할 줄 알아야 한다!

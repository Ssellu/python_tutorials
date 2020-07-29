"""

    < self >
    : 나
    : 이 객체의 참조값
    : 0번 인자를 받는 특수 매개변수
        ** 0번 인자
            p1.name
            --
             '.' 앞에 등장하는 인스턴스의 참조값이 0번인자다.

    멤버 변수, 즉 필드는 객체가 고유로 소유해야 한다.
    우리도 각자 이름, 나이, 학교 등의 정보를 고유로 소유하듯이,
    객체가 100개라면 각자의 개별 데이터를 가질 수 있어야 한다.


    하지만 멤버 함수의 경우 좀 다르다.
    객체가 100개가 생성되도 메서드 자체의 내용은 동일하다.
    따라서 메서드에서 사용하는 메모리를 모든 객체가 소유할 필요는 없다.


    함수와 메서드는
    매개변수, 지역변수 등의 함수에 사용되는 메모리는 '호출될 때' 생성되고
    '리턴되면' 해제된다.


    따라서 객체를 대상으로 하는 메서드 또한
    메서드를 호출할 때 생성되고 리턴되면 사라진다.
    이때, 메서드 입장에서는 누가 자기를 호출했는지 그에 대한 정보가 필요하다.
    때문에 0번인자라는 개념이 생겼다.
    (__init__() 도 메서드이기 때문에 예외는 없다!)


"""


class Pokemon:
    def __init__(self):
        self.name = ''
        self.level = 1

    def print_pokemon(self):
        print(f'{self.name} / LV.{self.level}')

    def save_pokemon(self):
        self.name = input('새 포켓몬 이름:')
        self.level = int(input(f'{self.name}의 레벨:'))


p1 = Pokemon()
# Pokemon 형태의 인스턴스가 생성된 후 __init__() 이 실행된면서
# self 매개변수에는 생성된 인스턴스의 참조값이 자동으로 대입된다.
# 객체 참조값이 1004라고 가정하면 다음과 같이 실행된다.
# def __init__(self):  # self= p1(1004)
#     1004.name = ''
#     1004.level = 1

p2 = Pokemon()  # 두번째 인스턴스는 2004 참조값을 가진다고 가정하자.
# def __init__(self):  # self= p2(2004)
#     2004.name = ''
#     2004.level = 1

p1.save_pokemon()
# def save_pokemon(self):  # self = 1004
#     1004.name = input('새 포켓몬 이름:')
#     1004.level = int(input(f'{1004.name}의 레벨:'))

p2.save_pokemon()
# def save_pokemon(self):  # self = 2004
#     2004.name = input('새 포켓몬 이름:')
#     2004.level = int(input(f'{2004.name}의 레벨:'))

p1.print_pokemon()
# def print_pokemon(self): # self = 1004
#     print(f'{1004.name} / LV.{1004.level}')

p2.print_pokemon()
# def print_pokemon(self): # self = 2004
#     print(f'{2004.name} / LV.{2004.level}')

#################################################################
# 참고) 파이썬은 self 사용을 권장하지만 꼭 이름이 self 일 필요는 없다.
class Pokemon:
    def __init__(this):
        this.name = ''
        this.level = 1


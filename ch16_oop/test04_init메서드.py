"""
    < 생성자 (Constructor) >
    - 객체 초기화를 담당하는 특수 메서드
    - 형식)
        def __init__(self):
            생성자가 할 일
            (주로 멤버변수 초기화)

        참고) 'def'가 붙으면 무조건 함수 정의다!!!!
            함수 : 일반 함수
            메서드 : 클래스 안에 들어있는 함수!


    - 호출 시점 : 클래스() 가 실행될 때 자동으로 해당 클래스의 __init__() 이 실행된다.
      약속된 형식이니 꼭 기억해두자!

    - 생성자의 리턴값 : 생성된 객체의 참조값

"""


class Person1:
    def __init__(self):
        self.name = ''
        self.age = 0
        self.contact = '000-0000-0000'


p1 = Person1()
# Person 모양 인스턴스 생성 및 생성된 객체 참조값을 p1에 저장 (Person1의 __init__()이 호출된다.)

p1.name = '홍길동'
p1.age = 10
p1.contact = '010-1111-2222'

print(f'{p1.name} {p1.age}세 {p1.contact}')
# 홍길동 10세 010-1111-2222


#########################################################################################
"""
p1.name = '홍길동'
p1.age = 10
p1.contact = '010-1111-2222'

일일히 이런 식의 저장이 귀찮다면..
특히나 인스턴스를 여러 개 생성해서 사용해야 한다면 이렇게 여러 줄로 저장하는 것이 귀찮다.
생성자를 활용해보자.
"""


class Person2:
    def __init__(self, name, age, contact):
        self.name = name  # name 과 self.name 은 다른 대상인 것을 주의하자.
        self.age = age
        self.contact = contact


p1 = Person2('홍길동', 10, '010-1111-2222')
# p1 = Person2()
# p1.name = '홍길동'
# p1.age = 10
# p1.contact = '010-1111-2222'

p2 = Person2('이푸린', 25, '010-3333-4444')
# p1 = Person2()
# p1.name = '이푸린'
# p1.age = 25
# p1.contact = '010-3333-4444'

print(f'{p1.name} {p1.age}세 {p1.contact}')  # 홍길동 10세 010-1111-2222
print(f'{p2.name} {p2.age}세 {p2.contact}')  # 이푸린 25세 010-3333-4444


# __init__()에 매개변수를 선언하니 값 저장이 좀 쉬워졌다.
# 하지만 이 경우는 반드시 인자를 주어야 하는 것 때문에 불편한 점이 또 생겼다.

# p3 = Person2()  # 에러
# (TypeError: __init__() missing 3 required positional arguments: 'name', 'age', and 'contact')

#########################################################################################
class Person3:
    def __init__(self, name='', age=0, contact='000-0000-0000'):
        self.name = name
        self.age = age
        self.contact = contact


p1 = Person3('홍길동', 10, '010-1111-2222')
# p1 = Person3()
# p1.name = '홍길동'
# p1.age = 10
# p1.contact = '010-1111-2222'

p2 = Person3('이푸린', 25)
# p2 = Person3()
# p2.name = '이푸린'
# p2.age = 25
# p2.contact = ''

p3 = Person3('김피카츄', contact='010-5656-7878')
# p3 = Person3()
# p3.name = '이푸린'
# p3.age = 25
# p3.contact = ''

print(f'{p1.name} {p1.age}세 {p1.contact}')  # 홍길동 10세 010-1111-2222
print(f'{p2.name} {p2.age}세 {p2.contact}')  # 이푸린 25세 000-0000-0000
print(f'{p3.name} {p3.age}세 {p3.contact}')  # 김피카츄 0세 010-5656-7878


# 바람직한 생성자의 모양 (기본값 주기 + 자료형 제한하기)
class Person4:
    def __init__(self, name: str = '', age: int = 0, contact: str = '000-0000-0000'):
        self.name = name
        self.age = age
        self.contact = contact

# keyword arguments 또한 자주 사용된다.
class Person5:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.age = kwargs['age']
        self.contact = kwargs['contact']

# 이 경우엔 꼭 key 이름을 함께 넣어주어야 하는 것을 잊지말자
p1 = Person4(name='홍길동', age=10, contact='010-1111-2222')


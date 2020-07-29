def test01(a, b, c):
    print(f'test1() --> a:{a} b:{b} c:{c}')


# 위 단순한 방법으로 매개변수를 작성하면
# 인자의 개수가 매개변수 개수보다 부족하거나 많으면 안된다.

# 이를 여러가지 방법으로 해결해보자.

########################################################################

# 1. 매개변수 기본값을 주는 방법
def test02(a=0, b=0, c=0):
    print(f'test1() --> a:{a} b:{b} c:{c}')


test02()  # test1() --> a:0 b:0 c:0
test02(10)  # test1() --> a:10 b:0 c:0
test02(10, 20)  # test1() --> a:10 b:20 c:0
test02(10, 20, 30)  # test1() --> a:10 b:20 c:30
test02(c=10, b=20, a=30)  # test1() --> a:30 b:20 c:10


# test02(10,20,30,40)   # 에러 (최대 3개까지만 받을 수 있다.)

########################################################################

# 2. 무제한 인자 받기 : 위치적 가변인자 (positional variable arguments) -> tuple 로 받기
def test03(*args):
    print(f'args:{args}')
    for i in range(len(args)):
        print(args[i])
    print(type(args))


test03('abc', 'def', 1, True)  # 개수 제한 없이 인자를 넣을 수 있다.
"""
args:('abc', 'def', 1, True)
abc
def
1
True
<class 'tuple'>
"""

########################################################################

# 참고) 일반 매개변수, args 함께 사용하기
def test04(a, *b):  # *b, a 순서는 안된다.
    print(f'a:{a} b:{b}')


test04(10, 20, 30, 40)  # a:10 b:(20, 30, 40)

########################################################################

# 2. 무제한 인자 받기 : 키워드 가변인자 (keyword variable arguments) -> dictionary 로 받기
def test05(**kwargs):
    print(f'kwargs:{kwargs}')
    for k, v in kwargs.items():
        print(f'key:{k}, value:{v}')
    print(type(kwargs))


test05(name="홍길동", age=10, address="서울시 역삼동", contact="010-1111-2222")
"""
kwargs:{'name': '홍길동', 'age': 10, 'address': '서울시 역삼동', 'contact': '010-1111-2222'}
key:name, value:홍길동
key:age, value:10
key:address, value:서울시 역삼동
key:contact, value:010-1111-2222
<class 'dict'>
"""

# 참고) 여기서 args, kwargs 대신 다른 이름을 사용할 수 있지만 관례상
#  positional arguments 는 args 로, keyword arguments 는 kwargs 로 표기한다.

########################################################################

# 3. args, kwargs 함께 사용하기
def test06(*args, **kwargs):  # **kwargs, *args 순서는 안된다.
    print(f'args:{args}')
    for i in range(len(args)):
        print(args[i])
    print(type(args))

    print(f'kwargs:{kwargs}')
    for k, v in kwargs.items():
        print(f'key:{k}, value:{v}')
    print(type(kwargs))


test06(10, 20, 30, 40, name="홍길동", age=10, address="서울시 역삼동", contact="010-1111-2222")
"""
args:(10, 20, 30, 40)
10
20
30
40
<class 'tuple'>
kwargs:{'name': '홍길동', 'age': 10, 'address': '서울시 역삼동', 'contact': '010-1111-2222'}
key:name, value:홍길동
key:age, value:10
key:address, value:서울시 역삼동
key:contact, value:010-1111-2222
<class 'dict'>
"""

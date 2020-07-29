"""
    함수는 1회 호출 당 1개의 값만 return 한다.
    이때 2개 이상의 값을 return 하는 경우 python 은 이를 tuple 에 패킹하여 return 한다.
"""
def test1():
    a = input("문자열 1 : ")
    b = input("문자열 2 : ")
    c = input("문자열 3 : ")
    return a, b, c  # return (a, b, c) 로도 적을 수 있다.


result = test1()  # 입력 : asd qwe zxc 를 각각 입력 했을 경우
print(result)           # ('asd', 'qwe', 'zxc')
print(type(result))     # <class 'tuple'>
print(result[0])        # asd
print(result[1])        # qwe
print(result[2])        # zxc


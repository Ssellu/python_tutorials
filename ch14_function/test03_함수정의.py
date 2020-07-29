"""
    - 함수 정의 (function definition; 함수 만들기)

    형식)
        def 함수명(매개변수1, 매개변수2, ...):
            함수가 할 일
            return 리턴값


    ** 매개변수 (parameter)
        인자값(재료)를 담는 통로 역할의 변수

    ** 매개변수의 개수는 자유롭게 지정 가능하다.
       인자가 필요없는 함수의 경우, 매개변수는 생략가능하다.

    ** 리턴값 (=결과값)
        => 함수 호출 1회의 결과값
       리턴값 또한 생략이 가능하다.
       이 경우 'return None' 혹은 'return' 을 마지막에 쓰거나, 아예 이를 생략할 수 있다.
       여러 개의 리턴값을 리턴하는 경우 자동으로 tuple 형태로 packing 되어 전달된다.

    ** return 의 의미
        1. 현재 진행 중인 함수를 '종료하고'
        2. 호출되었던 자리로 '돌아가서'
        3. (리턴값이 있다면) 리턴값을 호출된 자리로 '반환하라'
"""


# 함수명 : say_hello()
#   인자 : X
#   하는 일 : print() 로 ㅎㅇㅎㅇ 출력하기
#   리턴 : X
def say_hello():
    print('ㅎㅇㅎㅇ')
    return  # 리턴값이 없으므로 생략 가능


# 함수명 : add_two_nums()
#   인자 : 정수 2개
#   하는 일 : print() 로 두 정수의 합을 출력하기
#   리턴 : X
def add_two_nums(a, b):
    print(f'add_two_nums() 실행! {a} + {b} = {a + b}')
    return


# 함수명 : add_two_nums2()
#   인자 : 정수 2개
#   하는 일 : 두 수의 합을 구하기
#   리턴 : 합
def add_two_nums2(a, b):
    print('add_two_nums2() 실행!')
    res = a + b
    return res
    # 위 두 문장 대신 'return a + b' 도 가능


# 참고) 매개변수의 자료형 제한하기
#  -> 위 a, b에는 모든 형태의 인자가 들어올 수 있다. 이를 int로 제한해보자.
def add_two_nums3(a: int, b: int): # 이 경우 int 가 아닌 다른 형의 인자가 들어오면 에러를 발생시킨다.
    print('add_two_nums3() 실행!')
    return a + b


# 참고) 리턴값의 자료형 알려주기
#  -> return 값의 자료형이 무엇인지 함수 앞부분에 힌트를 제공할 수 있다.
def add_two_nums4(a, b) -> int:  # '->int' : int 형을 return 하는 함수임을 표시
    print('add_two_nums3() 실행!')
    return a + b


# 함수 호출하기
say_hello()  # return 값이 없는 함수는 대체로 행위 자체에 목적을 둔다.
# 출력 결과 : ㅎㅇㅎㅇ

num1 = 10
num2 = 20
add_two_nums(num1, num2)
# 출력 결과 :
# add_two_nums() 실행! 10 + 20 = 30

add_two_nums2(num1, num2)
# 출력 결과 :
# add_two_nums2() 실행!

result = add_two_nums2(num1, num2)
print(result)
# 출력 결과 :
# add_two_nums2() 실행!
# 30

print(add_two_nums3(num1, num2))
# 출력 결과 :
# add_two_nums3() 실행!
# 30
# 리턴값이 있는 함수의 경우, 단독적으로 사용하면 결과값을 확인할 방법이 없다.
# 이 리턴값을 변수에 담거나, print() 로 출력하면서 결과값을 확인한다.

print(add_two_nums3(b=num1, a=num2))
# 매개변수의 이름을 함께 적어주면 순서에 상관없이 인자를 넣을 수 있다.



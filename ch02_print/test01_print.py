"""
    < print() 함수 >
    - 표준출력함수
        ** 표준출력(standard out) : system 창에 출력
            ** system 창 : 운영체제와 사용자간의 상호작용을 위한 TUI(Text User Interface)
                cmd = command prompt = console = terminal

    - 자동 줄바꿈 기능이 있다.
    - sep, end, file 파라미터를 추가할 수 있다.

"""

# 1. 단순하게 출력하기
print(10)
# 결과 : 10

print('Hello, python!')
# 결과 : Hello, python!


# 2. 쉼표(,)를 사용하여 연속 출력하기
print(10, 20, 10+20)
# 결과 : 10 20 30

print('저의 나이는', 25, '살입니다.')
# 결과 : 저의 나이는 25 살입니다.


# 3. 'sep' 파라미터 추가하기 (구분자(separator) 지정) - default : 공백(' ')
print(10, 20, 10+20, sep='/')
# 결과 : 10/20/30

print('저의 나이는', 25, '살입니다.', sep='/')
# 결과 : 저의 나이는/25/살입니다.


# 4. 'end' 파라미터 추가하기 - default : 줄바꿈('\n')
# 주의! end 파라미터는 줄바꿈 기호(\n) 대신 들어갈 문자열을 삽입하는 기능이다.
# 따라서 end 파라미터를 사용했다면 이후 print()에 영향을 준다.
print('Hello, python!', end='ABC')
print('ㅋㅋㅋ')
# 두 print() 의 결과 : Hello, python!ABCㅋㅋㅋ


# 여러 print()를 한 줄로 출력하고자 한다면 end='' 을 사용한다.
print('abc', end='')
print('def', end='')
print('ghij')
# 세 print() 의 결과 : abcdefghij



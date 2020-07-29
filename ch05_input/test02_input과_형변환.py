"""
    input()은 입력값을 str 형으로 가져온다.
    아무리 숫자를 입력해도 형변환을 자동으로 하지 않는다.

"""

name, age = input("이름:"), input("나이:")
print(f'{name}님은 {age}살이군요.')

# print(f'3년 뒤에는 {age + 3}살이네요.')
# TypeError: can only concatenate str (not "int") to str

# 입력된 숫자를 제대로 처리하기 위해선 형변환이 필요하다.
print(f'3년 뒤에는 {int(age) + 3}살이네요.')

# 혹은 input()를 실행한 뒤 바로 형변환이 진행되도록 형변환의 인자로 input()를 넣어도 된다.
age2 = int(input("나이를 다시 입력하세요. : "))
print(f'{name}의 3년 뒤 나이는 {age2 + 3}')


# 형변환을 언제 하느냐에 따라 변수의 자료형에 차이가 있다.
print(type(age))    # <class 'str'>
print(type(age2))   # <class 'int'>

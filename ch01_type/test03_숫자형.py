"""
     1. 숫자형
        1) 정수형 - int 형
        2) 실수형 - float 형

        ** 정수/실수의 구분은 소숫점이다.
         3 => int
         3.0 => float
"""
a = 3
b = 3.0
c = 3.1

print(a)    # 3
print(b)    # 3.0
print(c)    # 3.1
print(f'각 a, b, c의 값 : {a}, {b}, {c}')   # 각 a, b, c의 값 : 3, 3.0, 3.1

# type(대상) : 대상의 자료형을 알려줘!
print(type(a))          # <class 'int'>
print(type(b))          # <class 'float'>
print(type(c))          # <class 'float'>
print(type(1.0))        # <class 'float'>
print(type(3.14))       # <class 'float'>
print(type(10))         # <class 'int'>


# 나눗셈의 결과 자료형은 무조건 float 형이다.
print(10 / 3)       # 3.3333
print(10 / 2)       # 5.0
print(type(10/3))   # <class 'float'>
print(type(10/2))   # <class 'float'>

# 나눗셈을 제외한 연산에서는 정수끼리의 연산은 정수가, 실수가 포함되었다면 실수의 결과자료형을 갖는다.
print(10 * 2)           # 20
print(type(10 * 2))     # <class 'int'>

print(10.0 * 2)         # 20.0
print(type(10.0 * 2))   # <class 'float'>


"""
    < 정수의 진법 표현 >
    2진법(binary) : 0 ~ 1             ( 1 + 1 = 10 )
      표현 : 0b정수 (대소문자 상관없이)
        예 : 0b100111   0B10011     
         
    8진법(octal) : 0 ~ 7              ( 7 + 1 = 10 )
      표현 : 0o정수 (대소문자 상관없이)
        예 : 0o1252   0O7     
        
    10진법(decimal) : 0 ~ 9           ( 9 + 1 = 10 )
      표현 : 정수 
        예 : 10  8101        
        
    16진법(hexadecimal) : 0 ~ F(=15)  ( F + 1 = 10 )
      표현 : 0x정수 
        예 : 0x10  0xA014        
        
"""
b1 = 0b1010011
o1 = 0o11234
h1 = 0x10AA
print(b1)  # 83   (2진수 1010011를 10진수로 출력)
print(o1)  # 4764 (8진수 0o11234를 10진수로 출력)
print(h1)  # 4266 (16진수 0x10AA를 10진수로 출력)
# 참고) print()는 10진수가 출력된다.


# 반대로, 10진수가 아닌 다른 진법으로 값을 출력하고 싶다면
b2 = bin(100)    # 10진수 100을 2진수로 변환
o2 = oct(100)    # 10진수 100을 8진수로 변환
h2 = hex(100)    # 10진수 100을 16진수로 변환
print(b2)        # 0b1100100
print(o2)        # 0o144
print(h2)        # 0x64

# 참고) bin(), oct(), hex()의 결과값은 str형(문자열)이다! (문자열은 연산에 주의해야한다.)
print(type(b2))  # <class 'str'>
print(type(o2))  # <class 'str'>
print(type(h2))  # <class 'str'>

print(b1 + h1)    # 4349 (83 + 4266 (0b1010011 + 0x10AA))
print(b2 + h2)    # 0b11001000x64  ('0b1100100' + '0x64')

"""
    < 대입 연산자 >
    - 변수 대입에 관여하는 연산기호

    =    : a = b
    +=   : a += b   ( a = a + b )
    -=   : a -= b   ( a = a - b )
    *=   : a *= b   ( a = a * b )
    **=  : a **= b  ( a = a ** b )
    /=   : a /= b   ( a = a / b )
    //=  : a //= b  ( a = a // b )
    %=   : a %= b   ( a = a % b )
    <<=  : a << b   ( a = a << b )
    >>=  : a >> b   ( a = a >> b )

"""
a = 10
b = 20
# a = b 와 b = a 는 다르다.
# a = b   ==> a:20  b:20
# b = a   ==> a:10  b:10

# 두 수의 값을 서로 바꾸기
a, b = b, a
print(a)  # 20
print(b)  # 10


num1 = 10
num2 = 3

num1 += num2
print(num1)  # 13

num1 -= num2
print(num1)  # 10

num1 *= num2
print(num1)  # 30

num1 **= num2
print(num1)  # 27000

num1 /= num2
print(num1)  # 9000.0

num1 //= num2
print(num1)  # 3000.0

num1 %= num2
print(num1)  # 0.0

# 주의 : 복합대입 연산자 사용 시 없는 변수에는 대입 불가
a = 10
a += 1000   # 가능

# b += 1000   # 에러
# NameError: name 'b' is not defined

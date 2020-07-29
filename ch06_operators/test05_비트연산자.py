"""
    < bitwise 연산자 >
    - 비트 단위의 산술 연산에 관여하는 연산기호

    & : a & b  (AND 연산) - 양 쪽 비트 모두 1이어야 1을 발생
    | : a | b  (OR 연산)  - 한 쪽 비트만이라도 1이면 1을 발생
    ^ : a ^ b  (XOR 연산) - 배타적 OR 연산. 한 쪽 비트'만' 1이어야 1을 발생
    ~ : ~a     (보수 연산) - 1은 0으로 0은 1로
    << : a << b (Left Shift) - 왼쪽 이동연산 (a의 구성비트를 b칸 왼쪽으로 이동시킨 값)
    >> : a >> b (Right Shift) - 오른쪽 이동연산 (a의 구성비트를 b칸 오른쪽으로 이동시킨 값)

"""
num1 = 14   # 00000000 00000000 00000000 00001110
num2 = 27   # 00000000 00000000 00000000 00011011

print(num1 & num2,  bin(num1 & num2))   # 10 0b1010
print(num1 | num2,  bin(num1 | num2))   # 31 0b11111
print(num1 ^ num2,  bin(num1 ^ num2))   # 21 0b10101
print(~num2,        bin(~num2))         # -28 -0b11100
print(num1 << 2,    bin(num1 << 2))     # 56 0b111000
print(num1 >> 2,    bin(num1 >> 2))     # 3 0b11


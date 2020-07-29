"""
    < 논리 연산자 >
    - 항의 참/거짓 여부에 관여하는 연산기호
    - 결과값의 자료형은 bool형 (True 혹은 False)
    and : a and b (a, b 모두 True 여야 True)
    or  : a or b  (a, b 둘 중 하나가 True 여도 True)
    not : not a   (a 가 True 면 False, False 면 True)

"""
num1 = 10
num2 = 3

print(num1 >= 10 and num2 != 3)  # False
print(num1 >= 10 or num2 != 3)   # True
print(not num2 != 3)             # True

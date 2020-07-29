"""
    < 멤버쉽 연산자 >
    - 원소의 구성 여부를 확인하는 연산자
    - 결과값의 자료형은 bool형 (True 혹은 False)

    in     : a in iterables (iterables 에 a가 있으면 True)
    not in : a not in iterables (iterables 에 a가 없으면 True)

"""
num1 = 3
num2 = 10
lst = [1, 2, 3, 4, 5]

print(num1 in lst)      # True
print(num2 in lst)      # False
print(num1 not in lst)  # False

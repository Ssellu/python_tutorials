"""
    < 형변환(casting) >
    - 데이터의 자료형을 일시적으로 변경
    - 자료형(변환할 값)
"""

a = int(1.234567)   # 1     (1.234567을 int 형으로 일시적으로 변경한 뒤, 그 결과를 a에 대입)
b = float(1)        # 1.0   (1을 float 형으로 일시적으로 변경한 뒤, 그 결과를 b에 대입)
c = str(b)          # '1.0' (b의 값을 str 형으로 일시적으로 변경한 뒤, 그 결과를 c에 대입)
d = bool(1)         # True
e = bool(0)         # False
f = int('10')       # 10
# f = int('abc')    # 에러
g = int(15 / 2)     # 7

print(a, type(a))  # 1 <class 'int'>
print(b, type(b))  # 1.0 <class 'float'>
print(c, type(c))  # 1.0 <class 'str'>
print(d, type(d))  # True <class 'bool'>
print(e, type(e))  # False <class 'bool'>
print(f, type(f))  # 10 <class 'int'>
print(g, type(g))  # 7 <class 'int'>


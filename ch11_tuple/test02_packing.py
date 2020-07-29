# packing 과 unpacking
a = 10, 20, 30  # 이때 10, 20, 30은 (10, 20, 30)으로 packing 된다.
print(a)        # (10, 20, 30)
print(type(a))  # <class 'tuple'>

a, b = (10, 20)  # 이때 (10, 20)이 unpacking 되어 a, b에 각각 담긴다.
print(a, b)      # 10 20

a, b = 10, 20    # 데이터를 ','로 나열하는 경우 자동으로 이들은 tuple 이 된다. a,b=(10,20) 과 동일하다.
print(a, b)      # 10 20 ==> 10, 20 이 (10,20)으로 packing ==> 다시 unpacking 되며 a, b에 저장

a, *b = 10, 20, 30, 40  # * : packing 연산자
print(a, b)      # 10 [20, 30, 40]
print(type(a))   # <class 'int'>
print(type(b))   # <class 'list'>

*a, b = 10, 20, 30, 40
print(a, b)      # [10, 20, 30] 40
print(type(a))   # <class 'list'>
print(type(b))   # <class 'int'>

# *a, *b = 10, 20, 30, 40  # 에러 (SyntaxError: two starred expressions in assignment)

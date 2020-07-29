"""
    < set >
    - 집합 자료형
    - 형식 :
        1. {원소1, 원소2, 원소3, ..}
        2. set(iterable)
            ** iterable 은 list, tuple, set, str 등의 나열되는 형태를 말한다. (dictionary 는 아님)
    - 중복 원소를 거른다. (중복 저장 X)
    - 순서가 없다. (인덱스, 슬라이싱 불가)
    - 중복 제거 필터용으로 사용된다.

"""
s = {10, 10, 20, 30, 40, 50, 60, 60}
print(s)  # {40, 10, 50, 20, 60, 30}

s = set("hello, python!")
print(s)  # {'p', 'y', 'h', 'e', ' ', 't', 'n', '!', ',', 'l', 'o'}

print(type(s))  # <class 'set'>

# print(s[0])  # TypeError: 'set' object is not subscriptable
# 인덱싱, 슬라이싱 등으로 접근하려면 set 을 tuple 로 바꿔서 사용한다.
t = tuple(s)
print(t[0])  # p

"""
1. 교집합 : &
"""
s1 = {2, 4, 6, 8, 10}
s2 = {1, 2, 3, 4, 5}
res = s1 & s2  # s1.intersection(s2) 으로 대체 가능 (s1, s2의 순서는 상관 없다.)
print(res)  # {2, 4}

"""
2. 합집합 : |
"""
res = s1 | s2  # s1.union(s2) 으로 대체 가능 (s1, s2의 순서는 상관 없다.)
print(res)  # {1, 2, 3, 4, 5, 6, 8, 10}

"""
3. 차집합 : - 
"""
res = s1 - s2  # s1.difference(s2) 으로 대체 가능
print(res)  # {8, 10, 6}

res = s2 - s1  # s2.difference(s1) 으로 대체 가능
print(res)  # {1, 3, 5}

"""
원소 추가 : 셋.add(새원소)
"""
s1.add(100)
print(s1)  # {2, 4, 100, 6, 8, 10}

s1.add(10)  # 중복 원소는 추가되지 않는다.
print(s1)  # {2, 4, 100, 6, 8, 10}

"""
원소 삭제 : 셋.remove(원소)
"""
s1.remove(100)
print(s1)  # {2, 4, 100, 6, 8, 10}

# s1.remove(-10)  # 없는 원소는 에러 (KeyError: -10)
# print(s1)

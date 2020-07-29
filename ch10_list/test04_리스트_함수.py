"""
    < 리스트 관련 함수 >
"""

# 1. 새 리스트 생성 : list()
a = list()  # a = [] 와 동일

# 2. 원소 추가 : 리스트.append(element)
print(a)  # []
a.append(10)
a.append(20)
a.append(30)
a.append(40)
a.append(50)
print(a)  # [10, 20, 30, 40, 50]

# 3. 원소 삽입 : 리스트.insert(index, element)
a.insert(3, 45)  # a[3]에 45 추가
print(a)  # [10, 20, 30, 45, 40, 50]

# 4. 리스트 복사 : 변수 = 리스트.copy()
b = a
c = a.copy()
a[0] = 40
print(a)  # [40, 20, 30, 45, 40, 50]
print(b)  # [40, 20, 30, 45, 40, 50]
print(c)  # [10, 20, 30, 45, 40, 50]

# 5. 특정 원소 개수 : 리스트.count(원소)
b = a.count(40)
print(b)  # 2

b = a.count(400)
print(b)  # 0

# 6. 다른 리스트와 병합 : 리스트.extend(다른 리스트)
b = [1, 2, 3, 4]
a.extend(b)  # a += b 와 동일
print(a)  # [40, 20, 30, 45, 40, 50, 1, 2, 3, 4]

# 7. 원소의 인덱스 찾기 :
#  변수 = 리스트.index(원소)
#  변수 = 리스트.index(원소, 시작인덱스)
#  변수 = 리스트.index(원소, 시작인덱스, 끝인덱스)
#  원소가 없는 경우 에러.
#  원소가 여러 개인 경우 가장 앞 원소 삭제

b = a.index(3)
print(b)  # 8

# b = a.index(-100)
# print(b)  # 에러 (ValueError: -100 is not in list)

# 8. 원소 삭제
# 1) 리스트.pop()  : 가장 마지막 원소를 삭제한 후, 삭제된 원소를 반환
# 2) 리스트.pop(인덱스) : 특정 인덱스의 원소를 삭제한 후, 삭제된 원소를 반환
# 3) 리스트.remove(원소) : 특정 원소를 삭제 (원소가 없는 경우 에러, 원소가 여러 개인 경우 가장 앞 원소 삭제)
b = a.pop()
print(a)  # [40, 20, 30, 45, 40, 50, 1, 2, 3]
print(b)  # 4

b = a.pop(3)  # [3]번 원소 삭제
print(a)  # [40, 20, 30, 40, 50, 1, 2, 3]
print(b)  # 45

a.remove(40)  # 원소 40 을 삭제
print(a)  # [20, 30, 40, 50, 1, 2, 3]

# 9. 오름차순 정렬 : 리스트명.sort()
a.sort()
print(a)  # [1, 2, 3, 20, 30, 40, 50]

# 10. 내림차순 정렬 : 리스트명.reverse()
a.reverse()
print(a)  # [50, 40, 30, 20, 3, 2, 1]

# 11. 모두 삭제 : 리스트명.clear()
a.clear()
print(a)  # []

# 참고) 메모리 해제 : del 대상
# (리스트, 변수 상관 없음)
del a
# print(a) # 에러 (NameError: name 'a' is not defined)

# 참고) 정렬 또 다른 방법
a = [1, 4, 5, 2, 6, 3, 1, 3, 1]
b = sorted(a)
print(a)  # [1, 4, 5, 2, 6, 3, 1, 3, 1] 변하지 않는다.
print(b)  # [1, 1, 1, 2, 3, 3, 4, 5, 6]

c = sorted(a, reverse=True)
print(c)  # [6, 5, 4, 3, 3, 2, 1, 1, 1]

# 참고) 리스트의 최댓값, 최솟값 구하기 (list 말고도 tuple, set 등의 iterable 자료형에 사용가능하다.)
m1 = max(a)
m2 = min(a)
print(m1)  # 6
print(m2)  # 1


a = [10, 20, 30, 40, 50]

# 방법1. while 문 사용
i = 0
while i < len(a):  # 혹은 i < 5
    print(a[i])
    i += 1


# 방법2. for 문 사용
for e in a:  # e : 10, 20, 30, 40, 50
    print(e)

# 방법3. for 문 사용 (인덱스를 증가)
for i in range(len(a)):  # i : 0, 1, 2, 3, 4
    print(a[i])  # a[0], a[1], a[2], a[3], a[4]


# for 문 변수에 원소를 대입하느냐, 인덱스를 대입하느냐의 차이
# ==> 각각 원소 수정 불가능, 수정 가능
b = [10, 20, 30, 40, 50]
for i in range(len(b)):
    b[i] += 1
print(b)  # [11, 21, 31, 41, 51]

b = [10, 20, 30, 40, 50]
for e in b:
    e += 1
print(b)  # [10, 20, 30, 40, 50]

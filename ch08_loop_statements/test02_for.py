"""
    < for 문 >
    형식:
        for 변수 in Iterable:
            Iterable 의 모든 원소를 순차적으로 변수에 담으면서 반복을 수행

    ** Iterable 형 데이터
        : 반복처리가 가능한 데이터의 집합 (데이터를 나열한 형태의 구조)

"""

for n in range(10):  # start:0 / end:9 / step:1
    print(n)
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9


for n in range(2, 10):  # start:2 / end:9 / step:1
    print(n)
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

for n in range(2, 10, 3):  # start:2 / end:9 / step:3
    print(n)
# 2
# 5
# 8


for n in [10, 20, 30, 40, 50]:
    print(n)
# 10
# 20
# 30
# 40
# 50

for n in (10, 20, 30, 40, 50):
    print(n)
# 10
# 20
# 30
# 40
# 50


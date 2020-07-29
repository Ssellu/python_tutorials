"""
    < tuple >
    - 수정 불가능한 리스트
    - 형식 : (원소1, 원소2, 원소3, ..)
    - 수정(원소 추가, 수정, 삭제, 삽입) 등을 제외하고는 리스트와 사용방법이 동일하다.
        -> 함수 사용 가능, for 문 사용 가능, 슬라이싱 가능

"""
t1 = (10, 20, 30, 40, 50)
print(t1)
print(t1[0])
print(t1[1])
print(t1[2])
print(t1[3])
print(t1[4])

# t1[2] = 10  # 에러 (TypeError: 'tuple' object does not support item assignment)


# 빈 튜플 만들기
t2 = ()
print(type(t2))  # <class 'tuple'>

t3 = tuple()
print(type(t3))  # <class 'tuple'>


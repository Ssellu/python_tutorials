"""
    < dictionary >
    - key-value 쌍으로 원소를 저장한다.
    - 형식 : {키1:값1, 키2:값2, 키3:값3, ...}
    - 인덱스 대신 key 를 사용하여 value 에 접근한다.
    - key 는 중복 X / value 는 중복 O
    - key 는 보통 정수나 문자열을 사용한다.

"""
d1 = dict()  # 혹은 d = {}
print(d1)  # {}
print(type(d1))  # <class 'dict'>

info1 = {'name': '홍길동', 'age': 19, 'tel': '010-1111-2222', 'vip': False}
info2 = {'name': '고길동', 'age': 29, 'tel': '010-3333-4444', 'vip': True}
print(info1)  # {'name': '홍길동', 'age': 19, 'tel': '010-1111-2222', 'vip': False}
print(info2)  # {'name': '고길동', 'age': 29, 'tel': '010-3333-4444', 'vip': True}

# 원소 변경
info1['name'] = '김길동'
info1['vip'] = True
print(info1)  # {'name': '김길동', 'age': 19, 'tel': '010-1111-2222', 'vip': True}


# 원소 추가
info1['addr'] = '서울시 강남구 역삼동'
print(info1)  # {'name': '김길동', 'age': 19, 'tel': '010-1111-2222', 'vip': True, 'addr': '서울시 강남구 역삼동'}




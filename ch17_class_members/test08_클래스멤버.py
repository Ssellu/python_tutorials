"""

    < 클래스멤버와 인스턴스멤버  >

    인스턴스 멤버 : 인스턴스 생성 시 생성되는 멤버
                    '객체주소.멤버명'으로 접근

    클래스 멤버 : 클래스 로드 시 생성되는 멤버
                    '클래스.멤버명'으로 접근

"""
class Tourist:
    destination = ''     # 클래스변수
    guide = ''           # 클래스변수

    def __init__(self):
        self.name = ''   # 인스턴스변수
        self.budget = 0  # 인트턴스변수


# 클래스멤버는 객체 생성 없이 바로 사용 가능
Tourist.destination = '제주도'
Tourist.guide = '김아무개'

# 인스턴스멤버는 객체 생성 후 사용 가능
t1 = Tourist()
t2 = Tourist()

t1.name = '홍길동'
t1.budget = 1000000

t2.name = '고길동'
t2.budget = 2000000

print(f'Tourist.destination : {Tourist.destination}')  # 제주도
print(f't1.destination : {t1.destination}')            # 제주도
print(f't2.destination : {t2.destination}')            # 제주도

print(f'Tourist.guide : {Tourist.guide}')  # 김아무개
print(f't1.guide : {t1.guide}')            # 김아무개
print(f't2.guide : {t2.guide}')            # 김아무개


print(f'{t1.name}, 예산 {t1.budget}원')    # 홍길동, 예산 1000000원
print(f'{t2.name}, 예산 {t2.budget}원')    # 고길동, 예산 2000000원

# 인스턴스변수는 객체 생성을 할 때마다 추가로 만들어진다.
# 클래스변수는 객체들 통틀어 단 1개씩만 만들어진다.
# 단, 다음과 같은 예외가 있다.

# 클래스명.변수명으로 값 변경 ==> 모두 동일하게 적용
Tourist.guide = '김라이츄'
print(f'Tourist.guide : {Tourist.guide}')  # 김라이츄
print(f't1.guide : {t1.guide}')            # 김라이츄
print(f't2.guide : {t2.guide}')            # 김라이츄


# 객체.변수명으로 값 변경 ==> 해당 변수는 더이상 t1에 대해서는 클래스변수가 아니다.
t1.guide = '이푸린'  # t1 객체의 클래스변수의 값 변경
print(f'Tourist.guide : {Tourist.guide}')  # 김라이츄
print(f't1.guide : {t1.guide}')            # 이푸린
print(f't2.guide : {t2.guide}')            # 김라이츄







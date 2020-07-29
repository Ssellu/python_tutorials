"""
    < 여러가지 문자열 포맷 방법 >
"""

name = '홍길동'
age = 10
height = 110.4

# 잘못된 표현
f_s0 = '제 이름은 name 이고, 나이는 age, 키는  height 입니다.'
print(f_s0)  # 제 이름은 name 이고, 나이는 age, 키는  height 입니다.

# 방법1. f-strings
f_s1 = f'제 이름은 {name} 이고, 나이는 {age}, 키는  {height} 입니다.'
print(f_s1)  # 제 이름은 홍길동 이고, 나이는 10, 키는  110.4 입니다.

f_s1 = f'제 이름은 {name:10} 이고, 나이는 {age:10}, 키는  {height:10.3f} 입니다.'
print(f_s1)  # 제 이름은 홍길동        이고, 나이는         10, 키는     110.400 입니다.


# 방법2. % operators
f_s2 = "제 이름은 %s이고, 나이는 %d, 키는 %f입니다." % (name, age, height)
print(f_s2)  # 제 이름은 홍길동이고, 나이는 10, 키는 110.400000입니다.

f_s2 = "제 이름은 %10s이고, 나이는 %10d, 키는 %10.3f입니다." % (name, age, height)
print(f_s2)  # 제 이름은        홍길동이고, 나이는         10, 키는    110.400입니다.

f_s2 = "제 이름은 %-10s이고, 나이는 %-10d, 키는 %-10.3f입니다." % (name, age, height)
print(f_s2)  # 제 이름은 홍길동       이고, 나이는 10        , 키는 110.400   입니다.


# 방법3. format()
f_s3 = '제 이름은 {0} 이고, 나이는 {1}, 키는  {2} 입니다.'.format(name, age, height)
print(f_s3)  # 제 이름은 홍길동 이고, 나이는 10, 키는  110.4 입니다.

f_s3 = '제 이름은 {0:10} 이고, 나이는 {1:10}, 키는  {2:10.3f} 입니다.'.format(name, age, height)
print(f_s3)  # 제 이름은 홍길동        이고, 나이는         10, 키는     110.400 입니다.


# 더보기 : https://docs.python.org/ko/3/tutorial/inputoutput.html


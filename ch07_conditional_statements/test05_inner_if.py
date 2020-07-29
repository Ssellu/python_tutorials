"""
    elif 는 else 와 if의 합성 키워드이다.
    test04의 실행 구조는 다음과 같다.
"""
age = int(input('나이 : '))

if age <= 7:
    print('미취학 아동입니다.')
else:
    if age <= 13:
        print('초등학생입니다.')
    else:
        if age <= 16:
            print('중학생입니다.')
        else:
            if age <= 16:
                print('고등학생입니다.')
            else:
                print('일반성인 혹은 대학생입니다.')

print(f'당신은 {age}살입니다.')

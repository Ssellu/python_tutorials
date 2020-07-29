"""
    < 분기문 >
    break : 반복을 종료한다.
    continue : 반복문 내의 남아있던 종속문장을 1회 생략한다.
    return : 함수를 종료한다.
    pass : 종속문장을 생략한다.

""" 
print('--- break test ---')
for num in range(10, 0, -1):
    if num % 4 == 0:
        break
    print(num)
# --- break test ---
# 10
# 9


print('--- continue test ---')
for num in range(10, 0, -1):
    if num % 4 == 0:
        continue
    print(num)
# --- continue test ---
# 10
# 9
# 7
# 6
# 5
# 3
# 2
# 1


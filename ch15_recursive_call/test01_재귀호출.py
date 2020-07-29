"""
    재귀 : 빙글빙글 돌기
    재귀호출 (recursive call)
        : 함수가 함수 내부에서 자기 자신을 호출하는 것
"""

# n! 구하기
def factorial(n:int)->int:
    if n == 1:
        return 1
    return n * factorial(n-1)
               ############## 재귀호출이 일어나는 부분

print(factorial(5))  # 120

"""
< 재귀호출의 동작 과정 >
def factorial(n:int)->int:   #  n : 5
    if n == 1:
        return 1
    return 5 * factorial(4) # 이전 호출된 자리로 값을 return 한다. (factorial(5) 의 자리로)
---------------============---------------------------------
                def factorial(n:int)->int:   #  n : 4
                    if n == 1:
                        return 1
                    return 4 * factorial(3) # 이전 호출된 자리로 값을 return 한다. (factorial(4) 의 자리로)
-------------------------------============---------------------------------
                               def factorial(n:int)->int:   #  n : 3
                                   if n == 1:
                                       return 1
                                   return 3 * factorial(2) # 이전 호출된 자리로 값을 return 한다. (factorial(3) 의 자리로)
----------------------------------------------============---------------------------------    
                                               def factorial(n:int)->int:   #  n : 2
                                                   if n == 1:
                                                       return 1
                                                   return 2 * factorial(1) # 이전 호출된 자리로 값을 return 한다. (factorial(2) 의 자리로)
--------------------------------------------------------------============---------------------------------
                                                               def factorial(n:int)->int:   #  n : 1
                                                                   if n == 1:
                                                                       return 1  # 이전 호출된 자리로 값을 return 한다. (factorial(1) 의 자리로)
                 
"""

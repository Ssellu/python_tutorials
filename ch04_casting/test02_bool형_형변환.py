"""
    Python3 에서는
     0, [], (), {}, None, '' 등의 데이터가 없는, 혹은 비어있는 형태를 False 로 인식한다.
     그 외는 모두 True 다.
"""
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
print(bool(None))
print(bool(0))
# 모두 False

# 따라서 다음을 주의하자
print(bool("False"))  # True


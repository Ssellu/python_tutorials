# 파일 읽기 - read 모드
#   * 한번 read 된 텍스트는 파일을 다시 열지 않는 이상 다시 read 되지 않는다.
#   * 파일 읽기/쓰기 모두 파일 내 커서를 기준으로 진행된다.
f = open('test.txt', 'r')

# 방법1. readline() : 한 줄 읽기, 커서는 다음 줄 맨 앞으로 넘어간다.
# s1 = f.readline()  # 한 줄 읽기
# s2 = f.readline()  # 한 줄 읽기
# s3 = f.readline()  # 한 줄 읽기
# print(s1)
# print(s2)
# print(s3)
# ==> 총 3줄을 읽었다.

# 방법2. readlines() : 한 줄 단위로 끊어서 리스트로 return
lst = f.readlines()
# 결과: ['aaaabbbb\n', 'cccc\n', 'dddd\n', 'aaaabbbb\n', 'cccc\n', 'dddd\n', 'aaaabbbb\n', 'cccc\n', 'dddd\n']
print(lst)

# 방법3. read()
# s = f.read()
# print(s)  # 파일의 모든 내용이 출력 (read() 를 수행하면 파일을 처음부터 끝까지 읽어들이므로 이후에는 read()를 추가로 진행할 수 없다.)


# 작업을 모두 수행하면 꼭 close() 하여 자원 누수를 막는다. (파일 닫기의 개념)
f.close()

"""

    < 파일 입출력 >

    객체명 = open('파일명', '모드')
    * 파일명은 경로를 포함한다.
        디렉토리 구분자는 \\ 혹은 /
    * 경로가 없는 파일인 경우 기본경로는 소스파일( .py)의 디렉토리
    * 파일 열기 모드
        'w' : write     (쓰기모드. 기존 내용을 덮어쓴다.)
        'a' : append    (추가모드. 기존 내용의 끝에 쓴다.)
        'r' : read      (읽기모드)

        - w, a 모드는 없는 파일인 경우 새로 생성
          r 모드는 error 발생
"""
# 파일 쓰기
f = open('test.txt', 'w')


# write(문자열)
f.write('aaaa')

# writelines(문자열 리스트)
s = ['bbbb\n', 'cccc\n', 'dddd\n']
f.writelines(s)


# 작업을 모두 수행하면 꼭 close() 하여 자원 누수를 막는다. (파일 닫기의 개념)
f.close()

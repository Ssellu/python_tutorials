# 파일 쓰기 - append 모드
f = open('test.txt', 'a')


# write(문자열)
f.write('aaaa')

# writelines(문자열 리스트)
s = ['bbbb\n', 'cccc\n', 'dddd\n']
f.writelines(s)

# 작업을 모두 수행하면 꼭 close() 하여 자원 누수를 막는다. (파일 닫기의 개념)
f.close()

"""
    < 제어문자(Escape Sequences) >
    - 컴퓨터와 주변기기의 상태를 제어하는 특수 문자
    - \ + 문자
    - 프로그래밍뿐 아니라 모든 IT 분야에서 상용된다.

    < 주요 제어문자 >
    \n : new line (enter 와 비슷)
    \b : back space
    \t : tab
    \\ : 문자 그대로의 \
    \' : 문자 그대로의 '
    \" : 문자 그대로의 "
    \r : carriage return (현재 줄의 맨 앞으로 커서 이동, home 과 비슷)
    \o8진수 : 8진수 정수로 문자 출력
    \x16진수 : 16진수 정수로 문자 출력


"""

print('hello\nworld!')
# hello
# world!

print('hello\bworld!')
# hellworld!

print('hello\tworld!')
# hello     world!

print('hello\\world!')
# hello\world!

print('hello\'world!')
# hello'world!

print('hello\"world!')
# hello"world!


print('hello\rworld!')  # /r : carriage return (줄의 맨 앞으로)
# world!

print("\110\145\154\154\157\40\127\157\162\154\144\41")  # \ooo (8진수 정수로 문자 출력)
# Hello World!

print("\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21")  # \xhh (16진수 정수로 문자 출력)
# Hello World!

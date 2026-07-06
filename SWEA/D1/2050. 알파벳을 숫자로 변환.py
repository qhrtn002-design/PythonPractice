data = input()
for i in data:
    print(ord(i) - ord('A') + 1, end=' ')
# ord : 문자를 숫자 유니코드 값으로 바꿔주는 내장함수 
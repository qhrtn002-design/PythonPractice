a = "Baseball"
print(a.count('b')) #해당문자의 개수 출력
print(a.find('b')) #해당문자가 처음 나온 위치. 없으면 -1 출력
#대소문자 동일 취급하지 않음.

b = "Life is too Long"
print(b.index('o')) #이것도 해당 문자가 처음나온 위치. 없으면 오류발생.
# 대소문자를 구별해야함. 동일 취급하지 않는다.

print(",".join('abcd'))
#abcd 문자열 사이에 쉼표를 삽입.

s = "  hi  "
print(s.strip()) #공백제거. lstrip: 왼쪽 공백만 제거, rstrip: 오른쪽 공백만 제거
print(s.rstrip().upper()) #공백제거 후, 대문자로 변환

print(b.replace("Long", "bad")) 
#문자열 바꾸기. 바꿀 단어를 찾지못하면 그대로 출력. 대소문자 구별 필요
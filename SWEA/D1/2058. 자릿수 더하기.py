a = int(input())

arr = list(str(a)) # 숫자를 문자열리스트로 만들기
sum = 0
for i in range(len(arr)):
    sum += int(arr[i]) # 문자열 하나씩 더하기
print(sum)
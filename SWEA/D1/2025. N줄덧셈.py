n = int(input())
total = 0 #합계 초기값은 무조건 반복문 밖에 있어야함
for i in range(n+1): # 1을 더해서 원래 숫자만큼 반복되게.
    total += i
print(total)
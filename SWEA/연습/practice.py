a = 'a:b:c:d'
b = a.split(':')
ans = '#'.join(b)
print(ans)

sum =0
A = [20,55,67,82,45,33,90,87,100,25]
for i in A:
    if i>=50:
        sum += i
print(sum)

def fibo(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibo(n-1) + fibo(n-2)

for i in range(10):
    print(fibo(i), end = ' ')


total = 0
num = map(int,input().split(','))
for i in num:
    total += i
print(total)


user_input = int(input('구구단을 출력할 숫자를 입력하세요 (2~9) : '))
for i in range(1,10):
    print(i*user_input, end=' ')
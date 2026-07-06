# 1번
def is_odd(num):
    if num % 2 == 1:
        return True
    else:
        return False

print(is_odd(3))
print(is_odd(4))

# 2번
def avg(*args):
    result = 0
    for i in args:
        result +=i
    return result / len(args)
print(avg(1,2))
print(avg(1,2,3,4,5))

# 3번
input1 = int(input("첫 번째 숫자를 입력하세요: "))
input2 = int(input("두 번째 숫자를 입력하세요: "))

total = input1 + input2
print("두 수의 합은 %d 입니다." % total)
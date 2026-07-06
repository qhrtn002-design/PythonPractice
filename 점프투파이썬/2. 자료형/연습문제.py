# 1번
kor = 80
eng = 75
math = 55
print((kor+eng+math)/3)

# 2번
if 13 % 2 == 0:
    print("짝수")
else:
    print("홀수")

# 3번
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)

# 4번
if pin[7] == "1":
    print("남자")
else:
    print("여자")

# 5번
a = "a,b,c,d"
b = a.replace(",","#")
print(b)

# 6번
a = [1,3,5,4,2]
a.sort()
a.reverse()
print(a)

# 7번
a = ['Life', 'is', 'too', 'short']
result = " ".join(a) # 공백마다 문자열을 넣겠다는 의미. ""이 아니라 " ".
print(result)

# 8번
a= (1,2,3)
print(a+(4,))

# 9번
a = dict()
# a[[1]] = 'python'은 오류발생. Key값은 변경이 불가능해야한다.
# 지금 Key은 리스트이므로 변경가능하기 때문에 오류가 발생.

# 10번
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a)
print(result)

# 11번
a = [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a)
b = list(aSet)
print(b)

# 12번
a = b = [1,2,3]
a[1] = 4
print(b)
s1 = set([1,2,3])
print(s1)
s2 = "baseball"
print(set(s2)) #중복 제거 후 출력, 순서없음

l1 = list(s1)#리스트로 반환
print(l1)
print(l1[2])

t1 = tuple(s1) #튜플로 반환
print(t1)

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print(s1 & s2) #교집합
print(s1 | s2) #합집합


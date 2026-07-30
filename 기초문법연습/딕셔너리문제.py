inventory={}
inventory['메로나'] = 300, 20 # 튜플 형식으로 저장됨.
inventory['비비빅'] = [400, 3] # 수정되기 위해선 리스트로 저장 필요
inventory['죠스바'] = [250, 100]
print(inventory)
print(f'{inventory["메로나"][0]} 원') #밸류에 대한 주소를 0으로 지정
print(f'{inventory["메로나"][1]} 개')

inventory['월드콘'] = [500,7] #새로운 내용 추가
print(inventory)

icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
print(list(icecream.keys())) #키만 리스트형태로 출력
print(list(icecream.values())) # 밸류만 리스트형태로 출력
print(sum(icecream.values())) # 밸류의 합계 출력
icecream.update({'팥빙수':2700, '아맛나':1000}) #여러개의 내용 한번에 추가
print(icecream)

keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys,vals)) # result라는 새로운 딕셔너리 추가.
# zip = 키와 밸류의 집합들을 하나의 딕셔너리로 묶어서 새로운 딕셔너리 생성
print(result)

date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date,close_price))
print(close_table)

from collections import defaultdict

arr = [1, 2, 1, 3, 2, 1]

cnt = defaultdict(int)

for x in arr:
    cnt[x] += 1

print(dict(cnt))
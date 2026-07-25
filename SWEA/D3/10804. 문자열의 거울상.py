t = int(input())
ans = {'p':'q','d':'b','q':'p','b':'d'} #딕셔너리 생성
for s in range(1,t+1):
    n = input()
    lst = []
    for i in n: 
        #리스트 돌면서 딕셔너리에서 해당 키값의 밸류를 리스트에 넣기
        lst.append(ans.get(i))
    answer = lst[::-1] # 거울에 비추니까 거꾸로 뒤집기
    print(f'#{s} ',end='')
    print(''.join(answer))

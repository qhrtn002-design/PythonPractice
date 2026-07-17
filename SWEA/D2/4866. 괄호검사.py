a = int(input())

for i in range(1,a+1):
    lst = [] #괄호를 받을 스택 생성
    flag = 1 #초기 출력 값을 1로 설정
    ans = input() # 문자열 입력 받기
    for x in ans: 
        if x == '{' or x == '(': 
            lst.append(x) #문자열마다 반복하면서 열린 괄호면 더하기
        else:
            if x == '}' or x == ')': #열린 괄호가 아닌경우, 닫힌 괄호 발견시
                if len(lst) == 0: 
                    flag = 0 #이전 스택 길이가 0이라면 0출력
                elif lst[-1] == '(' and x == ')':
                    lst.pop() #괄호의 짝이 맞다면 여는 괄호 없애기
                elif lst[-1] == '{' and x == '}':
                    lst.pop() #괄호의 짝이 맞다면 여는 괄호 없애기
                else: #이 외의 경우에는 모두 0 출력
                    flag = 0
                
            else: #괄호가 아닌 문자인 경우 그냥 넘기기
                continue
            
    if len(lst) != 0: #최종 스택 길이가 0이 아니라면 0 출력
        flag = 0 # 남아 있는 괄호가 있다는 뜻이기 때문
    print(f'#{i} {flag}')
          
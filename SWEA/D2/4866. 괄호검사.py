a = int(input())

for i in range(1,a+1):
    lst = []
    flag = 1
    ans = input()
    for x in ans:
        if x == '{' or x == '(':
            lst.append(x)
        else:
            if x == '}' or x == ')':
                if len(lst) == 0:
                    flag = 0
                elif lst[-1] == '(' and x == ')':
                    lst.pop()
                elif lst[-1] == '{' and x == '}':
                    lst.pop()
                else:
                    flag = 0
                
            else:
                continue
            
    if len(lst) != 0:
        flag = 0
    print(f'#{i} {flag}')
          
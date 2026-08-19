t = int(input())
for s in range(t):
    stack = []
    lst = list(input().split())
    ans = 'error'
    for i in lst:
        if i.isdigit():
            stack.append(int(i))
        elif i in '+-*/':
            if len(stack) >= 2:
                if i == '+':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a+b)
                elif i == '-':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b-a)
                elif i == '*':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a*b)
                elif i == '/':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b//a)
            else:
                ans = 'error'
                break
        elif i == '.':
            if len(stack) == 1:
                ans = stack.pop()
            else:
                ans = 'error'
                break
            
    print(f'#{s+1} {ans}')
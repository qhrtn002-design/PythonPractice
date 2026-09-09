for s in range(10):
    n=int(input())
    text=input()
    stack=[]
    ans=1
    for i in text:
        if i == '[' or i=='{' or i=='<' or i=='(':
            stack.append(i)
        else:
            if stack[-1] == '(' and i == ')':
                stack.pop()
            elif stack[-1] == '[' and i == ']':
                stack.pop()
            elif stack[-1] == '<' and i=='>':
                stack.pop()
            elif stack[-1] == '{' and i =='}':
                stack.pop()
            else:
                ans = 0
    if len(stack) != 0:
        ans = 0
    print(f'#{s+1} {ans}')
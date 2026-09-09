for s in range(10):
    n=int(input())
    text=input()
    flag=1
    stack=[]
    for t in text:
        if t=='(' or t=='{' or t=='[' or t=='<':
            stack.append(t)
        else:
            if len(stack)==0:
                flag=0
            elif stack[-1] == '(' and t == ')':
                stack.pop()
            elif stack[-1] == '[' and t == ']':
                stack.pop()
            elif stack[-1] == '{' and t == '}':
                stack.pop()
            elif stack[-1] == '<' and t == '>':
                stack.pop()
            else:
                flag=0
    if len(stack)!=0:
        flag=0
    print(f'#{s+1} {flag}')
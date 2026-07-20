t = int(input())

for s in range(1,t+1):
    n, m = map(int, input().split())

    num = list(map(int, input().split()))
    ans = num[m % len(num)]
    # 규칙 : m번만큼 맨앞을 맨뒤로 보내면, 결국 맨앞에 오는건 전체길이의 나머지다

    print(f'#{s} {ans}')
def dfs(i):
    if len(stack) == m:
        print(*stack)
        return
    else:
        for j in range(i, n+1):
            stack.append(j)
            dfs(j)
            stack.pop()


n, m = map(int, input().split())
stack = list()

dfs(1)
def dfs():
    if len(stack) == m:
        print(*stack)
        return
    else:
        for j in range(1, n+1):
            if j not in stack:
                stack.append(j)
                dfs()
                stack.pop()


n, m = map(int, input().split())
stack = list()
dfs()

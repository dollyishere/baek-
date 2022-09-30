def dfs(i):
    if len(stack) == m:
        for s in stack:
            print(num[s], end=' ')
        print()
        return
    else:
        for j in range(i, n):
            if j not in stack:
                stack.append(j)
                dfs(j)
                stack.pop()


n, m = map(int, input().split())
num = list(map(int, input().split()))
stack = list()

num.sort()
dfs(0)
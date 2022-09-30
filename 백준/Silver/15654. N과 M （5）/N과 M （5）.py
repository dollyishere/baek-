def dfs(i):
    if len(stack) == m:
        print(*stack)
        return
    else:
        for j in range(n):
            if num[j] not in stack:
                stack.append(num[j])
                dfs(num[j])
                stack.pop()


n, m = map(int, input().split())
num = list(map(int, input().split()))
stack = list()

num.sort()
dfs(0)
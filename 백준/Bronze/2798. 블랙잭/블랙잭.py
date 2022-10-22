from inspect import stack


n, m = map(int, input().split())
cards = list(map(int, input().split()))

def dfs(v):
    global maxv
    if len(stack) == 3:
        if sum(stack) > maxv and sum(stack) <= m:
            maxv = sum(stack)
    else:
        for i in range(v, n):
            if cards[i] not in stack:
                stack.append(cards[i])
                dfs(i)
                stack.pop()

stack = []
maxv = 0

dfs(0)
print(maxv)
import sys

N = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for n in range(N)]

stack = []

for n in range(N):
  order = data[n]
  if order == 'top':
    if len(stack):
      print(stack[-1])
    else:
      print(-1)
  elif order == 'size':
    print(len(stack))
  elif order == 'empty':
    if len(stack):
      print(0)
    else:
      print(1)
  elif order == 'pop':
    if len(stack):
      print(stack.pop(-1))
    else:
      print(-1)
  else:
    stack.append(order[5:])

n = int(input())
answer = 0

for _ in range(n):
    words = input()
    stack = []
    # 만약 A와 B가 번갈아서 있게 되면, 좋지 않음(선이 겹치므로)
    # 따라서 A끼리 떨어져 있어도, 중간에 B가 둘이 겹쳐서 빠져나온다면 좋은 수가 되는 것임(ABBA)
    # 고로, STACK에 값을 넣고 맨 윗값과 현재 값을 비교해 맞아 떨어지면 묶어서 끌고 나오는 식으로 해줌
    # 만약 끝까지 연산을 진행했어도 STACK 안에 단어가 남아 있다면, 좋은 단어가 아니게 됨
    for word in words:
        if stack:
            if stack[-1] == word:
                stack.pop()
            else:
                stack.append(word)
        else:
            stack.append(word)
    if stack == []:
        answer += 1

print(answer)

n, m = map(int, input().split())

pocketmons = {}
pocketmon_num = {}
for i in range(1, n+1):
    input_po = input()
    pocketmons[i] = input_po
    pocketmon_num[input_po] = i

for _ in range(m):
    now_input = input()
    if now_input.isdigit():
        print(pocketmons[int(now_input)])
    else:
        print(pocketmon_num[now_input])
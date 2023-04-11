import sys

N, M = map(int, sys.stdin.readline().split())
not_here_yet = set(sys.stdin.readline().rstrip() for _ in range(N))
not_see_yet = set(sys.stdin.readline().rstrip() for _ in range(N))

answer_list = not_here_yet & not_see_yet
new_answer_list = list(answer_list)
new_answer_list.sort()

print(len(new_answer_list))
for here_name in new_answer_list:
    print(here_name)
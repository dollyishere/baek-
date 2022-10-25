num_list = [int(input()) for _ in range(8)]

num_copy = num_list[:]
num_list.sort(reverse=True)

index_list = []
for i in range(5):
    index_list.append(num_copy.index((num_list[i])) + 1)

index_list.sort()

print(sum(num_list[:5]))

for j in range(5):
    if j == 4:
        print(index_list[j])
    else:
        print(index_list[j] , end=' ')
# 중위순회 함수 inorder 제작
def inorder(n):
    global cnt
    if n:
        # 한번 정점 조회할 때마다 cnt에 1씩 더해줌
        cnt += 1
        inorder(ch1[n])
        # 만약 정점에 도달할 시, 해당 정점 번호를 조회하는 대신 word_list를 조회하여 해당 정점 번호에 해당하는 인덱스에 담겨 있는 단어를 print함
        # 이때 end=를 사용하여 붙여서 출력해줌(하나의 단어를 완성해야 하기 때문)
        # 만약 cnt의 값이 N과 같다면(모든 정점을 조회했다면), end를 붙이지 않고 출력함
        if cnt == N:
            print(word_list[n-1])
        else:
            print(word_list[n - 1], end='')
        inorder(ch2[n])


# 테스트 케이스는 총 10번
# for문으로 해당 횟수만큼 반복함
for tc in range(1, 11):

    # 트리가 가지는 총 정점의 수 N을 받아줌
    N = int(input())
    # N의 크기 만큼 반복하며 해당 정점, 해당 정점의 문자, 해당 정점의 왼쪽 자식, 오른쪽 자식 입력 값을 node_list에 리스트 형태로 담아줌(왜냐하면 길이가 얼마일지 입력 값에 따라 달라지기 때문)
    node_list = [input().split() for _ in range(N)]
    # 정점 연결 상태를 담아줄 num_list와 해당 정점이 가지고 있는 문자를 담아줄 word_list를 빈 리스트 형태로 각각 생성
    num_list = list()
    word_list = list()

    # 현재 몇 번 정점까지 조회했는지를 파악하기 위한 변수 cnt 생성
    cnt = 0

    # node_list 안에 들어있는 구성 요소를 for문을 통해 순회
    for i in node_list:
    
    # 첫 값은 현 정점을 나타내는 숫자이므로 따로 num 변수에 담아줌
        num = int(i[0])
    # 두번째 값은 무조건 해당 정점이 가지고 있는 문자이므로 word_list에 담아줌
        word_list.append(i[1])
    # 만약 i의 길이가 2를 초과한다면, 자식인 정점을 지니고 있는 정점이라는 것을 뜻함
    # for문을 이용하여 이후 인덱스를 조회하며 현 정점 -> 자식 정점 순으로 담아줌
        if len(i) > 2:
            for j in range(2, len(i)):
                num_list.append(num)
                num_list.append(int(i[j]))

    # 이후 조회는 N - 1만큼 반복됨
    # E 변수에 해당 값 담아줌  
    E = N - 1

    # 왼쪽/오른쪽 자식 상태 받아줄 리스트 ch1, ch2 각각 생성
    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)

    # for문 이용해 E만큼 반복
    for i in range(E):
        # 부모 정점 번호 p, 자식 정점 번호 c 각각 num_list에서 조회해 받아와줌
        p, c = num_list[i*2], num_list[i*2+1]
        # 만약 왼쪽 정점이 채워져 있지 않다면, 왼쪽 정점부터 채워줌
        if ch1[p] == 0:
            ch1[p] = c
        # 채워져 있다면, 오른쪽 정점을 채워줌
        else:
            ch2[p] = c

    # 해당 트리의 시작점이라고 할 수 있는 root는 1로 지정
    root = 1

    # 먼저 테스트 케이스부터 출력
    print('#{}'.format(tc), end=' ')
    # 중위 순회를 실행시켜줌
    inorder(root)


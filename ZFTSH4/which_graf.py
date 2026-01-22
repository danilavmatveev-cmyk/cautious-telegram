N = int(input())
G = [[0] * N for i in range(N)]
for i in range(N):
    G[i] = list(map(int, input().split()))


def exam_graph(G):
    N = len(G)
    mask_orien = True
    for i in range(N):
        for j in range(N):
            if G[i][j] != G[j][i]:
                mask_orien = False
                break
    return mask_orien


def count__degree(G):
    N = len(G)
    count = 0

    for i in range(N):

        degree = sum(G[i]) + G[i][i]

        if degree % 2 == 0:
            count += 1

    return count
result = exam_graph(G)
print(result)

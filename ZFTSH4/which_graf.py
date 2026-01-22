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
result = exam_graph(G)
print(result)
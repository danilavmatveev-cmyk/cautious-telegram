 def input_graf():
    N = int(input())
    G = [[0]*N for i in range(N)]
    vertex_index = {V_list[i]: i for i in range(N)}
    for i in range(N):
        stok = input().split()
        for v in stok:
            G[i][vertex_index[v]]=1
            G[vertex_index[v]][i]=1
    return N,G

V_list = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
N,G = input_graf()
for i in range(N):
    print(*G[i])


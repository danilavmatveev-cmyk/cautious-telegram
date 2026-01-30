import sys

def input_graph(N):
    W = [[0]*N for i in range(N)]
    for i in range(N):
        line = input().split()
        j = 0
        for l in line:
            W[i][j] = int(l)
            j += 1
    return W

def floyd(dist):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

def graph_maxsize():
    for i in range(N):
        for j in range(N):
            if i != j and G[i][j] == 0:
                G[i][j] = sys.maxsize

def find_mountain(G):
  arr = max(G, key=max)
  return G.index(arr), arr.index(max(arr)), max(map(max, G))

N = int(input())
V_list = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
G = input_graph(N)

graph_maxsize()
G = floyd(G)
row_idx, col_idx, max_value = find_mountain(G)
print(V_list[row_idx], V_list[col_idx], max_value)

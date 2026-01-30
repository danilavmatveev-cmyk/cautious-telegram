def input_graph(N):
    W = [[0]*N for i in range(N)]
    for i in range(N):
        line = input().split()
        j = 0
        for l in line:
            W[i][j] = int(l)
            j += 1
    return W

def find_mountain(G):
  arr = max(G, key=max)
  return G.index(arr), arr.index(max(arr)), max(map(max, G))


N = int(input())
V_list = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


G = input_graph(N)
row_idx, col_idx, max_value = find_mountain(G)

print(V_list[row_idx], V_list[col_idx], max_value)


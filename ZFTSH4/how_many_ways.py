def input_graph(N):
    G = [[0] * N for i in range(N)]
    for i in range(N):
        G[i] = list(map(int, input().split()))
    return G


def matrix_to_edges(G, vertices):
    n = len(G)
    edges = []

    for i in range(n):
        for j in range(n):
            if G[i][j] != 0:
                edges.append(vertices[i] + vertices[j])

    return edges

def count_paths(NV, KV, edges):
    neighbours = [a for a, b in edges if b == KV]
    if KV == NV:
        return 1
    else:
        return sum(count_paths(NV,n, edges) for n in neighbours)

N = int(input())
input_data = input().split()
NV = input_data[0]
NP = input_data[1]
KV = input_data[2]

V_list = list("АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЭЮЯ")[:N]

G = input_graph(N)

E = matrix_to_edges(G,V_list)

print(count_paths(NV, KV, E))
print(count_paths(NV, NP, E) * count_paths(NP,KV,E))
print(count_paths(NV,KV,E)-count_paths(NV,NP,E)*count_paths(NP,KV,E))

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

def rec_p(nv, np, nk, st, dlm):
    global mindlm
    global minp
    if nv == nk:
        if np in st:
            if dlm < mindlm:
                mindlm = dlm
                minp = st.copy()
        return
    for i in range(N):
        if G[nv][i] != 0 and not (i in st):
            st.append(i)
            dlm += G[nv][i]
            rec_p(i, np, nk, st, dlm)
            st.pop()
            dlm -= G[nv][i]




N,nv,np,nk = map(int,input().split())
G = input_graph(N)
minp = []  # для хранения минимального пути
mindlm = sys.maxsize  # максимально возможное число в Python
rec_p(nv, np, nk, [nv], 0)
print(mindlm)
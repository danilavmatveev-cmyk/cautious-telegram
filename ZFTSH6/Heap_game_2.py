k1 = int(input())
k2 = int(input())
k3 = int(input())

def Peter(s,n):
    if s <= 1000:
        return True
    elif n==0:
        return False
    else:
        h=[]
        h.append(Ivan(s-k1,n-1))
        if s % k2 == 0: h.append(Ivan(s//k2,n-1))
        else: h.append(Ivan(s - 2, n - 1))
        if s % k3 == 0: h.append(Ivan(s//k3, n-1))
        else: h.append(Ivan(s - 3, n - 1))
        return any(h)

def Ivan(s, n):
    if s <= 1000:
        return True
    elif n == 0:
        return False
    else:
        h = []
        h.append(Peter(s-k1,n-1))
        if s % k2 == 0: h.append(Peter(s // k2, n - 1))
        else: h.append(Peter(s - 2, n - 1))
        if s % k3 == 0: h.append(Peter(s // k3, n - 1))
        else: h.append(Peter(s - 3, n - 1))
        return all(h)

for s in range(1000,10000):
    if not Peter(s,1) and Ivan (s,2):
        print (s)
        break





def count_paths(NV, KV, E):
    neighbours = [a for a, b in E if b == KV]
    if KV == NV:
        return 1
    else:
        return sum(count_paths(NV,n, E) for n in neighbours)


E = "АБ АВ АГ АД БВ ВЖ ВЗ ГВ ГЗ ДГ ДЗ ЖИ ЗЖ ЗИ ИК ИЛ ЛМ КМ".split()
NV = E[0][0]
KV = E[-1][-1]
NP = 'Л'


print(count_paths(NV,NP,E)*(count_paths(NP,KV,E)))
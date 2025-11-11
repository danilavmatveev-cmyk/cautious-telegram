def ring_dist(n, x, y):
    d = abs(x - y)
    return min(d, n - d)


def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    a = int(data[1])
    b = int(data[2])
    q = int(data[3])

    queries = []
    index = 4
    for _ in range(q):
        u = int(data[index])
        v = int(data[index + 1])
        index += 2
        queries.append((u, v))

    results = []
    for u, v in queries:
        d1 = ring_dist(n, u, v)
        d2 = ring_dist(n, u, a) + 1 + ring_dist(n, b, v)
        d3 = ring_dist(n, u, b) + 1 + ring_dist(n, a, v)
        results.append(str(min(d1, d2, d3)))

    print("\n".join(results))


if __name__ == "__main__":
    main()

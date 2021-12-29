def main():
    n = 0
    m = 0
    #G = [[2,3,4],[2,3],[],[0,1,4],[0,3]]
    G = [[2, 3], [2], [4, 5], [], [], [6], []]
    T = [[2, 3], [3], [0], [0, 1, 4], [3]]

    List = []
    Q = []
    parents = []
    count = []

    for v in range(len(G)):  # |V|
        parents.append([])  # |V|

    for v in range(len(G)):  # |V|
        count.append(len(G[v]))  # |V|
        for e in G[v]:
            parents[e].append(v)
        if len(G[v]) == 0:
            Q.append(v)

    while len(Q) != 0:
        List.append(Q[0])

        m = m + 1
        for e in parents[Q[0]]:
            n = n + 1
            count[e] = count[e] - 1
            if (count[e] == 0):
                Q.append(e)
        Q.pop(0)

    print(List)
    print(n)
    print(m)


if __name__ == '__main__':
    main()

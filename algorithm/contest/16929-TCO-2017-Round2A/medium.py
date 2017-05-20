class DistanceZeroAndOne:
    def construct(self, dist0, dist1):
        if not dist0[0] == dist1[1] == 0 or not dist0[1] == dist1[0] > 0:
            return tuple()
        n = len(dist0)
        es = [[10**18]*n for i in xrange(n)]
        for i in xrange(n):
            es[i][i] = 0
            for j in xrange(i+1, n):
                d0 = abs(dist0[i] - dist0[j])
                d1 = abs(dist1[i] - dist1[j])
                if d0 + d1 == 1 or d0 == d1 == 1:
                    es[i][j] = es[j][i] = 1
        for k in xrange(n):
            for i in xrange(n):
                for j in xrange(n):
                    es[i][j] = min(es[i][j], es[i][k] + es[k][j])
        for i in xrange(n):
            if es[0][i] != dist0[i]:
                return tuple()
            if es[1][i] != dist1[i]:
                return tuple()
            for j in xrange(n):
                if es[i][j] >= n:
                    return tuple()
        return tuple("".join(map(lambda x: "NY"[x==1], e)) for e in es)

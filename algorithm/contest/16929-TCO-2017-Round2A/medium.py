# encoding: utf-8
# あるn個の頂点集合があり、各辺の長さを1とした時の、
# 頂点0と1からの各頂点iまでの最短距離dist0[i], dist1[i]が与えられる。
# この条件を満たすグラフGが存在するかを判定し、存在するのであればその一つを出力せよ。
# 出力: tuple(string)の隣接行列 ('Y': iとjの間に(長さ1の)辺が存在, 'N': otherwise)
#     : 存在しない場合は空のtuple
class DistanceZeroAndOne:
    def construct(self, dist0, dist1):
        if not dist0[0] == dist1[1] == 0 or not dist0[1] == dist1[0] > 0:
            return tuple()
        n = len(dist0)
        es = [[10**18]*n for i in xrange(n)]
        for i in xrange(n):
            es[i][i] = 0
            for j in xrange(i+1, n):
                # 頂点iと頂点jが隣接しているか計算
                d0 = abs(dist0[i] - dist0[j])
                d1 = abs(dist1[i] - dist1[j])
                # (d0, d1) in [(0, 1), (1, 0), (1, 1)] => 頂点が隣接していると考えられる
                if d0 + d1 == 1 or d0 == d1 == 1:
                    es[i][j] = es[j][i] = 1
        # Warshall-Floyd Algorithm
        for k in xrange(n):
            for i in xrange(n):
                for j in xrange(n):
                    es[i][j] = min(es[i][j], es[i][k] + es[k][j])
        # 頂点0, 1から各頂点の距離までがdist0[i], dist1[i]と一致するかチェックする
        for i in xrange(n):
            if es[0][i] != dist0[i]:
                return tuple()
            if es[1][i] != dist1[i]:
                return tuple()
            for j in xrange(n):
                if es[i][j] >= n:
                    return tuple()
        return tuple("".join(map(lambda x: "NY"[x==1], e)) for e in es)

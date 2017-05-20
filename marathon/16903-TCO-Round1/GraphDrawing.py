# score: 190756.09
import random, math, time
import sys, operator

class GraphDrawing:

    def plot(self, NV, edges):
        tm = time.time
        start = tm()

        random.seed()
        randint = random.randint
        rand = random.random
        sqrt = math.sqrt

        es = [[] for i in xrange(NV)]
        NE = len(edges)/3
        nxt = iter(edges).next
        for i in xrange(0, NE):
            a = nxt(); b = nxt(); c = nxt()
            es[a].append((b, c))
            es[b].append((a, c))

        #sys.stderr.write("%s %s\n" % (ma, pair))
        LX = 700; LY = 700
        used = {}
        def gen():
            for i in xrange(NV):
                x = randint(0, LX)
                y = randint(0, LY)
                while (x, y) in used:
                    x = randint(0, LX)
                    y = randint(0, LY)
                used[x, y] = i
                yield (x, y)
        P = list(gen())

        V = [None]*NV
        m_score = 0
        result = P[:]
        inf = ()
        count = 0
        while 1:
            count += 1
            c_tm = tm()
            mi = (); ma = 0
            #sys.stderr.write("="*10 + str(t) + "\n")
            #sys.stderr.write("\n".join(",".join(map(str, p)) for p in P))
            e_nxt = iter(es).next
            p_nxt = iter(P).next

            for i in xrange(NV):
                vx = vy = 0.
                ix, iy = p_nxt()
                for j, c in e_nxt():
                    jx, jy = P[j]
                    dx = jx - ix; dy = jy - iy
                    ee = sqrt(dx**2 + dy**2)
                    r = abs(ee) / c

                    if ee > c:
                        sc = max(r, 1./r)**3 / ee
                    else:
                        sc = -max(r, 1./r)**3 / ee
                    vx += sc * dx
                    vy += sc * dy
                    mi = min(mi, r)
                    ma = max(ma, r)
                V[i] = (vx, vy)

            if m_score * ma < mi:
                m_score = mi / ma
                result = P[:]
                #sys.stderr.write("-> %.10f (%d, %f, %f)\n" % (m_score, count, mi, ma))

            p_nxt = iter(P).next
            v_nxt = iter(V).next
            for i in xrange(NV):
                vx, vy = v_nxt()
                px, py = ix, iy = p_nxt()
                if abs(vx)+abs(vy) > 1:
                    vv = vx**2 + vy**2
                    if 10 < vv:
                        r = randint(1, 10) / sqrt(vv)
                    else:
                        vv = sqrt(vv)
                        r = randint(1, int(vv+1)) / vv
                    #r = randint(1, min(10, int(vv))) / vv
                    ix = min(max(ix + int(vx * r) + randint(-2, 2), 0), LX)
                    iy = min(max(iy + int(vy * r) + randint(-2, 2), 0), LY)
                    if (ix, iy) not in used:
                        del used[px, py]
                        P[i] = (ix, iy)
                        used[ix, iy] = i
                    else:
                        j = used[ix, iy]
                        P[i], P[j] = P[j], P[i]
                        used[ix, iy] = i
                        used[px, py] = j

            #sys.stderr.write("\n".join(",".join(map(str, p)) for p in V))
            #sys.stderr.write("\n")

            n_tm = tm()
            #sys.stderr.write("%f %f\n" % (n_tm-start, n_tm-start+n_tm-c_tm))
            if n_tm - start + (n_tm - c_tm) > 9.5:
                break
        #sys.stderr.write("count: %d\n" % count)

        ret = reduce(operator.add, result)
        #sys.stderr.write("time: %f\n" % (tm() - start))

        return ret

class FoxAndCake2:
    def isPossible(self, c, s):
        p = "Possible"; q = "Impossible"
        def gcd(m, n):
            if m < n: return gcd(n, m)
            r = m % n
            return n if r == 0 else gcd(n, r)
        if gcd(c, s) > 1:
            return p
        if c % 2 == 1 and s % 2 == 1:
            if c >= 5 and s >= 5:
                return p
        if c % 2 == 1 and s % 2 == 0:
            if c >= 5 and s >= 8:
                return p
        if c % 2 == 0 and s % 2 == 1:
            if c >= 8 and s >= 5:
                return p
        return q

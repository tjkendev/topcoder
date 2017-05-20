# encoding: utf-8
# cherry🍒とstrawberry🍓がそれぞれc, s個ある。
# Cielは以下の条件を満たすようにcake🎂を焼きたい。
# - 全てのcherryとstrawberryを使い切る
# - 焼くcakeの数は任意の正の整数
# - 異なるcakeは異なる量のcherryとstrawberryを使う
# - 各cakeは少なくとも一つのcherryとstrawberryを使う
# - 各cakeに使うcherryとstrawberryの数は互いに素にならないようにする
# 以上の条件を満たすcherryとstrawberryの分け方が存在する場合は"Possible"、
# それ以外の場合は"Impossible"を出力せよ。
class FoxAndCake2:
    def isPossible(self, c, s):
        p = "Possible"; q = "Impossible"
        def gcd(m, n):
            if m < n: return gcd(n, m)
            r = m % n
            return n if r == 0 else gcd(n, r)
        if gcd(c, s) > 1:
            # (c, s)が互いに素でない => cake一個で満たせる
            return p
        if c % 2 == 1 and s % 2 == 1:
            # (odd, odd) => (5, 5)以上であれば(3, 3) + (even, even)という分け方が存在
            if c >= 5 and s >= 5:
                return p
        if c % 2 == 1 and s % 2 == 0:
            # (odd, even) => (5, 8)以上であれば(3, 6) + (event, event)という分け方が存在
            if c >= 5 and s >= 8:
                return p
        if c % 2 == 0 and s % 2 == 1:
            if c >= 8 and s >= 5:
                return p
        return q

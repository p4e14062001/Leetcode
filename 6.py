class Solution:
    def convert(self, s: str, n: int) -> str:
        if n == 1:
            return s
        word = [['' for i in range(len(s))] for j in range(n)]
        r = 0
        c = 0
        down = True
        for i in s:
            if down:
                d = 1
            else:
                d = -1
            word[r][c] = i
            c = c + 1
            r = r + d
            if r == 0:
                down = True
            if r == n - 1:
                down = False
        s = ''
        for i in word:
            s = s + ''.join(i)
        return s

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        sign = abs(x) // x
        x = sign * int(str(abs(x))[::-1])
        if x > 2 ** 31 - 1 or x < -2 ** 31:
            return 0
        return x

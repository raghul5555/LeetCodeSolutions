class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        l0 = 0
        l1 = 1
        t = l0+l1
        for i in range(2, n+1):
            t = l0+l1
            l0 = l1
            l1 = t
        return t
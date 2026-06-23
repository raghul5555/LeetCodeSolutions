class Solution:
    def reverse(self, x: int) -> int:
        if -10<x<10:
            x = x
        elif x>0:
            x = str(x)
            x = int(x[::-1])
        else:
            x = str(x)[1::]
            x = int(x[::-1])
            x = -1*x
        if -2**31<=x<2**31:
            return x
        else:
            return 0

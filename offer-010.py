class Solution:
    def fib(self, n: int) -> int:
        fib_dict = {0: 0, 1: 1}

        for i in range(2, 101):
            fib_dict[i] = (fib_dict[i-1] + fib_dict[i-2])%1000000007

        return fib_dict[n]
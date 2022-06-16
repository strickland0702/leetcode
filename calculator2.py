class Solution:
    def calculate(self, s: str) -> int:

        num = 0
        stack = []
        presign = '+'

        for i in range(len(s)):

            if '0' <= s[i] <= '9':
                num = 10 * num + int(s[i])

            if i == len(s) - 1 or s[i] in '+-*/':
                if presign == '+':
                    stack.append(num)
                elif presign == '-':
                    stack.append(-num)
                elif presign == '*':
                    stack.append(stack.pop() * num)
                elif presign == '/':
                    stack.append(int(stack.pop() / num))

                presign = s[i]
                num = 0

        return sum(stack)
        

sol = Solution()
print(sol.calculate(s = "14-3/2"))
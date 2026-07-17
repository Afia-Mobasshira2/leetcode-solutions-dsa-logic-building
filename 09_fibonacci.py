class Solution(object):
    def fib(self, n):
        # 1. BASE CASES (The Emergency Brakes)
        if n == 0:
            return 0
        if n == 1:
            return 1
            
        # 2. RECURSIVE CASE
        # We tell the function to call ITSELF with smaller inputs!
        return self.fib(n - 1) + self.fib(n - 2)
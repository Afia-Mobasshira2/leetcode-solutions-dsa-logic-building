class Solution(object):
    def climbStairs(self, n):
        # Base cases handled cleanly
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Starting values for Step 1 and Step 2
        first = 1
        second = 2
        
        # Step through from 3 all the way up to n
        for i in range(3, n + 1):
            # The current step is the sum of the previous two steps
            current = first + second
            
            # Shift our variables forward for the next step loop
            first = second
            second = current
            
        return second
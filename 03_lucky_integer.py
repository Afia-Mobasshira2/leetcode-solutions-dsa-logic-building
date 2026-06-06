class Solution(object):
    def findLucky(self, arr):
        counts = {}
        
        # Step 1: Count the frequency of each number
        for num in arr:
            if num in counts:
                counts[num] = counts[num] + 1
            else:
                counts[num] = 1
        
        lucky_version = -1
        
        # Step 2: Look for the lucky number
        for num in counts:
            if counts[num] == num:
                # If we find a higher lucky number, update our answer
                if num > lucky_version:
                    lucky_version = num
                
        return lucky_version
    
    # --- Test Case for VS Code ---
sol = Solution()
print(sol.findLucky([2, 2, 3, 4]))
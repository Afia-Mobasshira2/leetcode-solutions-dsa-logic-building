from typing import List

class Solution:
    def reverseString(self, s):
        # 1. Initialize your pointers
        left = 0
        right = len(s) - 1
        
        # 2. Keep looping as long as left is less than right
        while left < right:
            # 3. Swap the letters
            s[left], s[right] = s[right], s[left]
            
            # 4. Move the pointers inward
            left = left + 1    # Pushes left pointer to the right
            right = right - 1  # Pushes right pointer to the left

# --- This section runs your code locally in VS Code ---
if __name__ == "__main__":
    sol = Solution()               # Create the solution machine
    test_word = ["h", "e", "l", "l", "o"]
    
    sol.reverseString(test_word)   # Run your function
    print(test_word)               # Print the result
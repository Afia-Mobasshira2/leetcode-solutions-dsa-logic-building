class Solution(object):
    def getDecimalValue(self, head):
        total = 0
        current = head
        
        while current is not None:
            # RULE: Double the total, then add the chalkboard value
            total = (total * 2) + current.val
            
            # Walk to the next car
            current = current.next
            
        return total
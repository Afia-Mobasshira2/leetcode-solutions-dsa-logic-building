def largestAltitude(gain):
    current_altitude = 0
    max_altitude = 0
    
    for g in gain:
        # 1. Update your current_altitude (Right-to-Left assignment)
        current_altitude = current_altitude + g
        
        # 2. If the new altitude is higher than our maximum, update the maximum!
        if current_altitude > max_altitude:
            max_altitude = current_altitude
        
    return max_altitude

# Test case to check your logic
print(largestAltitude([-5, 1, 5, 0, -7])) # Should output 1
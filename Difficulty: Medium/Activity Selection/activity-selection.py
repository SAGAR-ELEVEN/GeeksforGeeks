class Solution:
    def activitySelection(self, start: list[int], finish: list[int]) -> int:
        #code here
        
        #1. create an empty tuple
        activities = []
        
        #2. To add start, finish elements in tuple
        for i in range(len(start)):
            activities.append((start[i], finish[i]))
            
        
        #3. Sort the activities tuple
        activities.sort(key=lambda x:x[1])
        
        
        #4. Assign some stuff
        count = 0
        last_element = -1
        
        #5. Main part
        for start_element, end_element in activities:
            
            if start_element > last_element:
                count += 1
                
                last_element = end_element
                
        
        return count
        
        
        
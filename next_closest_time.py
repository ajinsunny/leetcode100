'''
        input: "HH:MM"
        output: string 
        
        
        1, 9 , 3, 4 
        
        - iterate through the string 
            - avoid ":"
            - addition of minutes. 
            
       1, 9 , 3, 4      
            
       closest can be done by changing the last digit. 
       
       change using 1 -- 1, 9, 3, 1 --- this is also back
       change using 9 ---1, 9, 3, 9 --- this is going forward , so ok 
       change using 3 ---1, 9, 3, 3  -- this is going back 
       
       
       
       iterate through the time and replace the minute with lowest value 
       
       - replace last digit with every digit in the time. 
       
                - check delta between original time and new time. 
                
            
        
        '''

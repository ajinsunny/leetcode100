import math 
class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        
        
        '''
        
        iterate from left to right 
        
            for each number. 
                - check if number is a palindrome. 
                - check if the sqaureroot of the number is a palindrome. 
    
        '''
        
        count = 0
        sqrt_left = math.sqrt(int(left))
        sqrt_right = math.sqrt(int(right))
            
            
        for num in range(int(sqrt_left),int(sqrt_left)):
            print(num)
            if str(num) == str(num)[::-1]:
                print(num)
                
            
            
            
            
            
            
            
            
            
                    
        # print(count)
        
        
                
        

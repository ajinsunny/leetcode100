class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        '''
        
        f
        s
        ADOBECODEBANC
        
        counts = {A:0 , B:0, C:0}
        
        missing char = 3 
        result = [0, inf]
      
        fast = 0 
        slow = 0 
        missing_characters = len(t)
        
        counts = {}
        
        for fast in range(len(s)):
            if s[fast] not in counts:
                
                if counts[s[fast]]==0:
                    missing_characters -=1
                    
                counts[s[fast]] +=1
        
            if missing_characters ==0:
                if (fast - slow) < result[1]-result[0]:
                    result[0]=slow
                    result[1]=fast
                if s[slow] in counts:
                    if counts[s[slow] == 0:
                        missing_char +=1 
                        
                slow +=1 
                
        if result[1]==inf: return ""
        return S[result[0]:result[1]]
        
                    
        '''
        
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        

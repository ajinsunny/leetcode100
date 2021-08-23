class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        hashmap = {}
        
        for i in range(len(nums)):
            hashmap[nums[i]]=i
            
        for i in range(len(nums)):
            if target-nums[i] in hashmap:
                if hashmap[target-nums[i]] != i:
                    return [i, hashmap[target-nums[i]]]

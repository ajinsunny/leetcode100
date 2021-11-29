#include <vector>
#include <map>


class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        
        //make an unordered map 
        unordered_map<int, int> hash;
        
        //decalre a vector for th result
        vector<int> result;
        
        //number to find 
        
        
        //iterate through the given vector of nums and use the target to find the other pair 
        
        for (int i=0;i<nums.size();i++){
            
            int numberToFind = target - nums[i];
            
            if(hash.find(numberToFind) != hash.end()){
                
                result.push_back(hash[numberToFind]);
                result.push_back(i);
                return result;
                
            }
            
            hash[nums[i]]=i;
            
        }
        return result;
    }
};

class Solution2 {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        
        map<int,int> map;
        vector<int> pairs;
        
        for(int i = 0; i<nums.size(); i++){
            int complement = target - nums[i];
            if (map.find(complement)!=map.end()){
                pairs.push_back(map.find(complement)->second);
                pairs.push_back(i);
                break;
                
            }
            map.insert(pair<int, int>(nums[i],i));
                
        }
        return pairs;
        
    }
};

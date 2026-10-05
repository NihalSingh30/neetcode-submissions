class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sets = {} 

        for i in range(len(nums)):

            difference = target - nums[i] #target - value
           
            if difference in sets: #kalo difference ada di set
                return [sets[difference],i]
            sets[nums[i]] = i
    
                    
 

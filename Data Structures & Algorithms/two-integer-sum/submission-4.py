class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for index, n in enumerate(nums):
            hashmap[n] = index

        for index, n in enumerate(nums):
            diff = target - n
            if diff in hashmap and hashmap[diff] != index:
                return [index, hashmap[diff]]
        return []
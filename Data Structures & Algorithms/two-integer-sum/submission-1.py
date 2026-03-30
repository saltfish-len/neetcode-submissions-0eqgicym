class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash to speed up
        indice = {v:i for i,v in enumerate(nums)}
        for i,x in enumerate(nums):
            if target-x in indice and indice[target-x]!=i:
                return [i,indice[target-x]]
        
        
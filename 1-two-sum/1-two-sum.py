class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, v in enumerate(nums):
            ii=i+1
            for ind, vv in enumerate(nums[ii:]):
                if v+vv == target:
                    return(i, ii+ind) 
            
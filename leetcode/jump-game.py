class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        # iterate over arr len
        for i in range(len(nums)):
            if i > max_reach: # if at any point the length of the arr > max_reach, failed bc end cannot be reached
                return False
            
            max_reach = max(max_reach, i + nums[i]) # else, update and loop

        return True
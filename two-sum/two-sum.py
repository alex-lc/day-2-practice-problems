class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## UNDERSTAND
        # Given a list of numbers, find the indices of the two numbers
        # that add up to our passed in target number

        ## PLAN
        # Use two loops
        # Compare first num to rest of nums in list, repeat

        ## EXECUTE
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [nums.index(nums[i]), nums.index(nums[j], i + 1)]
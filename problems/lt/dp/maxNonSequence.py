


from typing import List










class Solution:
    def rob(self, nums: List[int]) -> int:
        if (len(nums) == 0):
            return 0
        if (len(nums) == 1):
            return nums[0]

        if (len(nums) == 2):
            return nums[1] if nums[1] > nums[0] else nums[0]

        max1 = nums[0]
        maxS = nums[1] if nums[1] > nums[0] else nums[0]

        for i in range(2, len(nums)):
            nums[i] = nums[i] + max(nums[i - 2], max1)

            max1 = maxS

            if nums[i] > maxS:
                maxS = nums[i]
        return maxS

s = Solution()
item= [2,4,0,3,5]
max2 = s.rob(item)
print(max2)
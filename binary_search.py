class Solution:
    def searchRange(self, nums, target: int):

        start, end = None, None

        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                right = mid - 1

            elif nums[mid] > target:
                right = mid - 1

            else:
                left = mid + 1
 
        if left >= len(nums) or nums[left] != target:
            start = -1

        else:
            start = left

        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                left = mid + 1

            elif nums[mid] > target:
                right = mid - 1

            else:
                left = mid + 1

        if right < 0 or nums[right] != target:
            end = -1

        else:
            end = right

        return [start, end]

solution = Solution()
print(solution.searchRange(nums=[5,7,7,8,8,10], target=8))

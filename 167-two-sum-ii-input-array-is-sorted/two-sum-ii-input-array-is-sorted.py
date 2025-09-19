class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l <= r:
            x = numbers[l] + numbers[r]
            if x == target:
                return [l+1, r+1]
            elif x > target:
                r -= 1
            else:
                l += 1
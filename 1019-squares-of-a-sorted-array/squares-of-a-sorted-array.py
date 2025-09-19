class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        s = 0
        e = n-1
        for i in range(n-1, -1, -1):
            if abs(nums[s]) >= abs(nums[e]):
                ans[i] = nums[s]*nums[s]
                s += 1
            else:
                ans[i] = nums[e]*nums[e]
                e -= 1
        return ans
        #   ^^^
        # # O(n), O(n)

        # ans = [num*num for num in nums]
        # ans.sort()
        # return ans
        #   ^^^
        # O(nlogn), O(n)  But somehow, this gets a faster runtime ;-; !

        # TimeComplexit, SpaceComplexity
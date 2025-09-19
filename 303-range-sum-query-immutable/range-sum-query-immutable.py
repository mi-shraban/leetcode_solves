class NumArray:

    def __init__(self, nums: List[int]):
        self.prefNums = nums
        for i in range(1, len(nums)):
            self.prefNums[i] += self.prefNums[i-1]        

    def sumRange(self, left: int, right: int) -> int:
        if left != 0:
            sum = self.prefNums[right] - self.prefNums[left-1]
        else:
            sum = self.prefNums[right]
        return sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
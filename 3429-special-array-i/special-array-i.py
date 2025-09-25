class Solution:
    def isArraySpecial(self, arr: List[int]) -> bool:
        n = len(arr)
        for i in range(1, n):
            if arr[i-1] & 1 == arr[i] & 1:
                return False
        return True
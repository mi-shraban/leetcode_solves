class Solution:
    def isArraySpecial(self, arr: List[int]) -> bool:
        for i in range(1, len(arr)):
            if arr[i-1] & 1 == arr[i] & 1:
                return False
        return True
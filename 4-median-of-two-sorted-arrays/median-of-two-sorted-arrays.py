class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = []
        n = len(nums1)
        m = len(nums2)
        x = n + m
        i = j = 0
        while i < n and j < m:
            if nums1[i] <= nums2[j]:
                arr.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                arr.append(nums2[j])
                j += 1
        while i < n:
            arr.append(nums1[i])
            i += 1
        while j < m:
            arr.append(nums2[j])
            j += 1
        if x % 2 == 0:
            ans = float(arr[x//2 - 1] + arr[x//2])/2
        else:
            ans = arr[x//2]
        return ans

        # O(n) time complexity
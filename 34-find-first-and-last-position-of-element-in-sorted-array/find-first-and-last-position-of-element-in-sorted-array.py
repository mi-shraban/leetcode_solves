class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # def binSrc():
        #     l, r = 0, len(nums)-1
        #     while l <= r:
        #         mid = l + (r-l)//2
        #         if nums[mid] == target:
        #             return mid
        #         elif nums[mid] > target:
        #             r = mid - 1
        #         else:
        #             l = mid + 1
        #     return -1
        # idx = binSrc()
        # print(idx)
        # if idx == -1 or len(nums) == 0:
        #     return [-1, -1]
        # l = r = idx
        # while l >= 0 and  nums[l] == target:
        #     l -= 1
        # while r < len(nums) and nums[r] == target:
        #     r += 1
        # return [l+1, r-1]
        # O(n) in worst case. Where all of the elements are equal to the target.
        def binSrc(left):
            l, r = 0, len(nums) - 1
            idx = -1
            while l <= r:
                mid = l + (r-l)//2
                if nums[mid] == target:
                    idx = mid
                    if left:
                        r = mid - 1
                    else:
                        l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return idx
        l = binSrc(True)
        r = binSrc(False)
        return [l, r]
        # O(logn)
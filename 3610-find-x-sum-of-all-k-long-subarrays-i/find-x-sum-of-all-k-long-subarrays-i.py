class Solution:
    def findXSum(self, nums: List[int], k: int, thresh: int) -> List[int]:
        l = 0
        r = l + k
        ans = []
        for i in range(0, len(nums)-k+1):
            freq = {}
            for x in nums[l:r]:
                freq[x] = freq.get(x, 0) + 1
            l += 1
            r += 1
            freq = sorted(freq.items(), key=lambda item: (item[1], item[0]), reverse=True)
            val = 0
            for i, kv in enumerate(freq):
                k, v = kv
                if i == thresh:
                    break
                val += k * v
            ans.append(val)
        return ans
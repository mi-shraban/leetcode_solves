class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        for x in nums:
            if x not in cnt:
                cnt[x] = 0
            cnt[x] += 1
        bkt = sorted(cnt.items(), reverse=True, key=lambda x:x[1]) # O(nlogn) ;-;
        ans = [x for x, y in bkt[:k]]
        return ans
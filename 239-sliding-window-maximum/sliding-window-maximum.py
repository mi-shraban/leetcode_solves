class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # ans = []
        # for i in range(len(nums)-(k-1)):
        #     ans.append(max(nums[i:k+i]))
        # return ans
        # O(n*k) too slow
        ans = []
        q = deque()
        for i, x in enumerate(nums):
            while q and q[-1] < x:
                q.pop()
            q.append(x)
            if i >= k and nums[i-k] == q[0]:
                q.popleft()
            if i >= k-1:
                ans.append(q[0])
        return ans
        # O(n)
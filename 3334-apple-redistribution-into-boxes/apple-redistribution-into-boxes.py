class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apples = sum(apple)
        capacity.sort(reverse=True)
        ans = 0
        for x in capacity:
            if apples <= 0:
                return ans
            apples -= x
            ans += 1
        return ans
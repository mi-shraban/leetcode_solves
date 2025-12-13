class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        n = len(code)
        ans = []
        priority = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }
        def isValid(s):
            if len(s) == 0:
                return False
            for x in s:
                if x.isalnum() or x == '_':
                    continue
                else:
                    return False
            return True
        for i, x in enumerate(code):
            if isValid(x) and isActive[i] and businessLine[i] in priority:
                ans.append((priority[businessLine[i]], x))
        ans.sort()
        return [y for x, y in ans]
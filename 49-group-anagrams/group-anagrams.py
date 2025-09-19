class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ds = {}
        for x in strs:
            key = self.isAnagram(x)
            if key not in ds:
                ds[key] = [x]
            else:
                ds[key].append(x)
        return [y for x, y in ds.items()]
    def isAnagram(self, s: str) -> int:
        return ''.join(sorted(s))
        # a, b = 0, 0
        # for x in s:
        #     a += ord(x)
        #     b += ord(x)**2
        # return a+b
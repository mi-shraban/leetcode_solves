class Solution:
    def isValid(self, s: str) -> bool:
        stacc = []
        pairs = ['()', '{}', '[]']
        cl = [')', '}', ']']
        for x in s:
            if x in cl:
                if stacc:
                    op = stacc.pop()
                    if op + x not in pairs:
                        return False
                    else:
                        continue
                else:
                    return False
            else:
                stacc.append(x)
        if not stacc:
            return True
        return False
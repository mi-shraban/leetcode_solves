class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        vowels = 'aeiouAEIOU'
        consonants = "qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM"
        digits = '0123456789'
        allowed = vowels + consonants + digits
        has_vowels = False
        has_consonants = False
        for c in word:
            if c in vowels:
                has_vowels = True
            if c in consonants:
                has_consonants = True
            if c not in allowed:
                return False
        return has_vowels & has_consonants
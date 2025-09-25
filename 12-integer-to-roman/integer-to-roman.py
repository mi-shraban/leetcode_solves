class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ''
        n_map = {
            1000 : 'M', 
            900: 'CM',
            500 : 'D',
            400 : 'CD',
            100 : 'C',
            90 : 'XC',
            50 : 'L',
            40 : 'XL',
            10 : 'X',
            9 : 'IX',
            5 : 'V',
            4 : 'IV',
            1 : 'I'         
        }   # reverse sorted by keys
        for k, v in n_map.items():
            if num == 0:
                return ans
            cnt = num // k
            ans += cnt * v
            num -= cnt * k
        return ans
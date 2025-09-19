class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd = n ** 2
        sumEven = n * (n + 1)
        print(sumOdd, sumEven)
        while sumEven:
            sumOdd, sumEven = sumEven, sumOdd % sumEven
        return sumOdd
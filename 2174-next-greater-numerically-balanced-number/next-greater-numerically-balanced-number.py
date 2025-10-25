# class Solution:
#     def nextBeautifulNumber(self, n: int) -> int:
#         balanced, size = self.generateBalanced()
#         print(balanced, size)
#         # balanced = [1, 22, 122, 212, 221, 333, 1333, 3133, 3313, 3331, 4444, 14444, 22333, 23233, 23323, 23332, 32233, 32323, 32332, 33223, 33232, 33322, 41444, 44144, 44414, 44441, 55555, 122333, 123233, 123323, 123332, 132233, 132323, 132332, 133223, 133232, 133322, 155555, 212333, 213233, 213323, 213332, 221333, 223133, 223313, 223331, 224444, 231233, 231323, 231332, 232133, 232313, 232331, 233123, 233132, 233213, 233231, 233312, 233321, 242444, 244244, 244424, 244442, 312233, 312323, 312332, 313223, 313232, 313322, 321233, 321323, 321332, 322133, 322313, 322331, 323123, 323132, 323213, 323231, 323312, 323321, 331223, 331232, 331322, 332123, 332132, 332213, 332231, 332312, 332321, 333122, 333212, 333221, 422444, 424244, 424424, 424442, 442244, 442424, 442442, 444224, 444242, 444422, 515555, 551555, 555155, 555515, 555551, 666666]
#         # size = 109
#         # l, r = 0, size-1
#         # while l < r:
#         #     mid = (l + r)//2
#         #     if balanced[mid] <= n:
#         #         l = mid + 1
#         #     else:
#         #         r = mid
#         # return balanced[l]
#     # code used to generate all the balanced number within the given range :3
#     def isBalanced(self, dct):
#         for k, v in dct.items():
#             if k != v:
#                 return False
#         return True
#     def generateBalanced(self):
#         N = 10**8
#         balanced = []
#         size = 0
#         for i in range(1, N):
#             temp = {}
#             curr = i
#             while curr:
#                 x = curr % 10
#                 temp[x] = 1 + temp.get(x, 0)
#                 curr //= 10
#             if self.isBalanced(temp):
#                 balanced.append(i)
#                 size += 1
#         return balanced, size
def generate(n, cnt, balanced):
    if n > 0 and isBalanced(cnt):
        balanced.append(n)
    if n > 1224444:
        return
    for i in range(1, 8):
        if cnt[i] < i:
            cnt[i] += 1
            generate(n * 10 + i, cnt, balanced)
            cnt[i] -= 1
def isBalanced(cnt: list[int]) -> bool:
    for i in range(1, 8):
        if cnt[i] != 0 and cnt[i] != i:
            return False
    return True
balanced = []
generate(0, [0]*10, balanced)
balanced.sort()
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        l, r = 0, len(balanced)-1
        while l < r:
            mid = (l + r)//2
            if balanced[mid] <= n:
                l = mid + 1
            else:
                r = mid
        return balanced[l]
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        group = [i for i in range(n)]
        group[firstPerson] = 0
        meetings.sort(key=lambda x:x[2])
        size = len(meetings)
        i = 0
        while i < size:
            curr_t = meetings[i][2]
            temp = []
            while i < size and meetings[i][2] == curr_t:
                g1 = self.find(group, meetings[i][0])
                g2 = self.find(group, meetings[i][1])
                group[max(g1, g2)] = min(g1, g2)
                temp.extend(meetings[i][0:2])
                i += 1
            for j in temp:
                if self.find(group, j) != 0:
                    group[j] = j
        ans = []
        for i in range(n):
            if self.find(group, i) == 0:
                ans.append(i)
        return ans
    def find(self, group, idx):
        while idx != group[idx]:
            idx = group[idx]
        return idx
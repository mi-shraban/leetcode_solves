class DSU:
    def __init__(self, n):
        self.size = n
        self.parent = [i for i in range(self.size)]
        self.rank = [0 for i in range(self.size)]
        self.cycles = 0
    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]
    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        if x == y:
            self.cycles += 1
        else:
            if self.rank[x] < self.rank[y]:
                self.parent[x] = y
            elif self.rank[x] > self.rank[y]:
                self.parent[y] = x
            else:
                self.parent[x] = y
                self.rank[y] += 1
    def components(self):
        count = 0
        for i in range(self.size):
            if self.parent[i] == i:
                count += 1
        return count

class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        vertices = []
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    vertices.append((i, j))
        dsu = DSU(n)
        for u, v in vertices:
            dsu.union(u, v)
        ans = dsu.components()
        return ans
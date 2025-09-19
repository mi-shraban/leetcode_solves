class Solution:
    def findOrder(self, numCourses, prerequisites):
        self.digraph = {i: [] for i in range(numCourses)}
        for u, v in prerequisites:
            self.digraph[v].append(u)
        self.order = []
        self.visited = {i: 0 for i in range(numCourses)}
        self.parents = {i: -1 for i in range(numCourses)}
        for node in self.digraph:
            if self.visited[node] == 0:
                if self.dfs(node):
                    return []
        return self.order[::-1]
    def dfs(self, node):
        self.visited[node] = 1
        for adj in self.digraph[node]:
            if self.visited[adj] == 1:
                return True
            if self.visited[adj] == 0:
                self.parents[adj] = node
                if self.dfs(adj):
                    return True
        self.visited[node] = 2
        self.order.append(node)
        return False
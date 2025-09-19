class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for u, v in prerequisites:
            graph[u].append(v)
        visited = {i: 0 for i in range(numCourses)}
        for node in graph:
            if visited[node] == 0:
                if self.dfs(node, graph, visited):
                    return False
        return True
    def dfs(self, node, graph, visited):
        visited[node] = 1
        for adj in graph[node]:
            if visited[adj] == 1:
                return True
            if visited[adj] == 0:
                if self.dfs(adj, graph, visited):
                    return True
        visited[node] = 2
        return False
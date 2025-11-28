class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        if n < 2:
            return 1
        graph = {i:[] for i in range(n)}
        degree = [0] * n
        for a, b in edges:
            graph[a].append(b)
            degree[a] += 1
            graph[b].append(a)
            degree[b] += 1
        leaves = deque([i for i in range(n) if degree[i] == 1])
        cnt = 0
        while leaves:
            curr = leaves.popleft()
            degree[curr] -= 1
            carry = 0
            if values[curr] % k == 0:
                cnt += 1
            else:
                carry = values[curr]
            for adj in graph[curr]:
                if degree[adj] == 0:
                    continue
                degree[adj] -= 1
                values[adj] += carry
                if degree[adj] == 1:
                    leaves.append(adj)
        return cnt
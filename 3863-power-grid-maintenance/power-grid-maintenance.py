class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        parent = [i for i in range(c+1)]
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        for a, b in connections:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[rb] = ra
        next_node = [0] * (c + 1)
        comp_min = [0] * (c + 1)
        last = {}
        for i in range(1, c+1):
            r = find(i)
            if comp_min[r] == 0:
                comp_min[r] = i
            else:
                next_node[last[r]] = i
            last[r] = i
        offline = [False] * (c + 1)
        ans = []
        for t, x in queries:
            if t == 1:
                if not offline[x]:
                    ans.append(x)
                else:
                    r = find(x)
                    ans.append(comp_min[r] if comp_min[r] else -1)
            else:
                if not offline[x]:
                    offline[x] = True
                    r = find(x)
                    if comp_min[r] == x:
                        y = next_node[x]
                        while y and offline[y]:
                            y = next_node[y]
                        comp_min[r] = y if y else 0
        return ans

        # ah yes. DSU...after a long time
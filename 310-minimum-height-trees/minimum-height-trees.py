class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        tree = {i: [] for i in range(n)}
        min_height = 10**9
        mht = []
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)
        leaves = [node for node in range(n) if len(tree[node]) == 1]
        rem = n
        while rem > 2:
            rem -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                adj = tree[leaf].pop()
                tree[adj].remove(leaf)
                if len(tree[adj]) == 1:
                    new_leaves.append(adj)
            leaves = new_leaves
        return leaves
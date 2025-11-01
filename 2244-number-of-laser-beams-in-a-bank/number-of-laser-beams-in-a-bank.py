class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        layers = []
        for row in bank:
            x = row.count('1')
            if x:
                layers.append(x)
        beams = 0
        for i in range(1, len(layers)):
            beams += layers[i-1]*layers[i]
        return beams
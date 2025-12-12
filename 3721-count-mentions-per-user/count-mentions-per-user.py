class Solution:
    def countMentions(self, n: int, events: List[List[str]]) -> List[int]:
        mentions = [0] * n
        online = [0] * n
        events.sort(key=lambda x: (int(x[1]), x[0] == "MESSAGE"))
        all_mentioned = 0
        for e, t, a in events:
            t = int(t)
            if  e == "MESSAGE":
                if a == "ALL":
                    all_mentioned += 1
                elif a == "HERE":
                    for i in range(n):
                        if online[i] <= t:
                            mentions[i] += 1
                else:
                    a = [int(x[2:]) for x in a.split(' ')]
                    for x in a:
                        mentions[x] += 1
            else:
                a = int(a)
                online[a] = t + 60
        for i in range(n):
            mentions[i] += all_mentioned
        return mentions
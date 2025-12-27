class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms, counter = [0] * n, [0] * n
        meetings.sort()
        for s, e in meetings:
            found = False
            for idx, busy in enumerate(rooms):
                if busy <= s:
                    rooms[idx] = e
                    counter[idx] += 1
                    found = True
                    break
            if not found:
                q = rooms.index(min(rooms))
                rooms[q] += e - s
                counter[q] += 1
        return counter.index(max(counter))
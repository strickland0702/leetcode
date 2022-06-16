from dis import dis
from queue import PriorityQueue
class Solution:
    def networkDelayTime(self, times, n: int, k: int) -> int:

        def dijkstra(start, graph):
            distto = [float("inf") for _ in range(n+1)]

            distto[start] = 0

            queue = PriorityQueue()
            
            queue.put((0, start))

            while not queue.empty():

                cur_dist, cur_id = queue.get()
                print(cur_dist, cur_id)
                if cur_dist > distto[cur_id]:
                    continue

                for neighbor in adjacency[cur_id]:
                    next_id = neighbor[0]
                    next_dist = distto[cur_id] + neighbor[1]

                    if distto[next_id] > next_dist:
                        distto[next_id] = next_dist
                        queue.put((next_dist, next_id))

                print(distto)
                # print(queue)

            
            return distto

        adjacency = [[] for _ in range(n+1)]
        for (source, target, weight) in times:
            adjacency[source].append((target, weight))

        print(adjacency)
        distto = dijkstra(k, adjacency)
        res = 0

        for i in range(1, n+1):
            if distto[i] == float("inf"):
                return -1

            res = max(res, distto[i])

        return res


times = [[2,1,1],[2,3,1],[3,4,1]]
sol = Solution()
res = sol.networkDelayTime(times, 4, 2)
print("ans:", res)
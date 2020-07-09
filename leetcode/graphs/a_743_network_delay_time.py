import collections


# heap

# class Solution:
#     def networkDelayTime(self, times, N, K):
#         q, t, adj = [(0, K)], {}, collections.defaultdict(list)
#         for u, v, w in times:
#             adj[u].append((v, w))
#         while q:
#             time, node = heapq.heappop(q)
#             if node not in t:
#                 t[node] = time
#                 for v, w in adj[node]:
#                     heapq.heappush(q, (time + w, v))
#         return max(t.values()) if len(t) == N else -1


# queue

class Solution:
    def networkDelayTime(self, times: [[int]], N: int, K: int) -> int:

        track = [0] + [2 ** 31] * N
        graph = collections.defaultdict(list)
        q = collections.deque()
        q.append((0, K))

        for sn, tn, t in times:
            graph[sn].append([tn, t])

        while q:
            time, node = q.popleft()
            if time < track[node]:
                track[node] = time
                for tr, tm in graph[node]:
                    q.append((tm + time, tr))

        mx = max(track)
        return mx if mx < 2 ** 31 else -1


if __name__ == '__main__':
    print(Solution().networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))

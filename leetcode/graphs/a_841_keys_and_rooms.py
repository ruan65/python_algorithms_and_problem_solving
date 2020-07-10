# class Solution:
#     def canVisitAllRooms(self, rooms: [[int]]) -> bool:
#         visited = [not r for r in rooms]
#         q = deque([0])
#         while q:
#             r = q.popleft()
#             visited[r] = True
#             for k in rooms[r]:
#                 if not visited[k]:
#                     q.append(k)
#         return all(visited)


class Solution:
    def canVisitAllRooms(self, rooms: [[int]]) -> bool:
        visited = set()

        def dfs(rm: int):
            if rm not in visited:
                visited.add(rm)
                for r in rooms[rm]:
                    dfs(r)

        dfs(0)
        return len(visited) == len(rooms)


if __name__ == '__main__':
    print(Solution().canVisitAllRooms([[1], [2], [3], []]))

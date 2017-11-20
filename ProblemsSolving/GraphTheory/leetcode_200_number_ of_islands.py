# https://leetcode.com/problems/number-of-islands

from collections import defaultdict


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        if not grid:
            return 0

        # build graph
        n, m = len(grid), len(grid[0])
        graph = defaultdict(list)
        for row in range(n):
            for col in range(m):
                if grid[row][col] == '0':
                    continue

                graph[(row, col)].append((row, col))
                if row > 0 and grid[row - 1][col] == '1':
                    graph[(row, col)].append((row - 1, col))

                if row < (n - 1) and grid[row + 1][col] == '1':
                    graph[(row, col)].append((row + 1, col))

                if col > 0 and grid[row][col - 1] == '1':
                    graph[(row, col)].append((row, col - 1))

                if col < (m - 1) and grid[row][col + 1] == '1':
                    graph[(row, col)].append((row, col + 1))

        seen = set()
        res = 0
        for vertex in graph:
            if vertex not in seen:
                seen.add(vertex)
                stack = [vertex]
                island = []
                while stack:
                    cur_vertex = stack.pop()
                    island.append(cur_vertex)
                    for nei in graph[cur_vertex]:
                        if nei not in seen:
                            seen.add(nei)
                            stack.append(nei)

                if island:
                    res += 1
        return res


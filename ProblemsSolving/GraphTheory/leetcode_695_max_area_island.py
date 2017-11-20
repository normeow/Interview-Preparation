'''
https://leetcode.com/problems/max-area-of-island
'''


from collections import defaultdict


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0

        n, m = len(grid), len(grid[0])
        graph = defaultdict(list)

        for row in range(n):
            for col in range(m):
                if grid[row][col] != 1:
                    continue
                graph[(row, col)].append((row, col))
                if row > 0 and grid[row-1][col] == 1:
                    graph[(row, col)].append((row-1, col))

                if row < (n-1) and grid[row+1][col] == 1:
                    graph[(row, col)].append((row+1, col))

                if col > 0 and grid[row][col-1] == 1:
                    graph[(row, col)].append((row, col-1))

                if col < (m-1) and grid[row][col+1] == 1:
                    graph[(row, col)].append((row, col+1))

        seen = set()
        for vertex in graph:
            if vertex not in seen:
                seen.add(vertex)
                stack = [vertex]
                component = []
                while stack:
                    cur_vertex = stack.pop()
                    component.append(cur_vertex)
                    for node in graph[cur_vertex]:
                        if node not in seen:
                            stack.append(node)
                            seen.add(node)
                res = max(res, len(component))

        return res



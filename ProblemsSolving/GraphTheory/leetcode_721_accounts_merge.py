'''
https://leetcode.com/problems/accounts-merge/

For every pair of emails in the same account, draw an edge between those emails.
The problem is about enumerating the connected components of this graph.
'''

from collections import defaultdict


class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        email_to_name = dict()

        # Adjacency list for nodes-emails
        graph = defaultdict(list)
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                graph[email].append(acc[1])
                graph[acc[1]].append(email)
                email_to_name[email] = name

        # dfs, find all connected components
        visited = set()
        res = []
        for email in graph:
            if email not in visited:
                visited.add(email)
                component = []
                stack = [email]
                while stack:
                    node = stack.pop()
                    component.append(node)
                    for nei in graph[node]:
                        if nei not in visited:
                            stack.append(nei)
                            visited.add(nei)

                res.append([email_to_name[email]] + sorted(component))
        return res

s = Solution()
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"],
            ["John", "johnnybravo@mail.com"],
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["Mary", "mary@mail.com"]]
print(s.accountsMerge(accounts))






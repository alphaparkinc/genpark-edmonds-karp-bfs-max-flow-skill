"""Edmonds-Karp BFS Max Flow Algorithm.
100% Python Standard Library.
"""

import collections

class EdmondsKarpMaxFlow:
    """Edmonds-Karp BFS shortest augmenting path maximum flow algorithm."""
    def __init__(self, num_nodes):
        self.n = num_nodes
        self.capacity = collections.defaultdict(int)
        self.adj = collections.defaultdict(list)

    def add_edge(self, u, v, cap):
        self.capacity[(u, v)] += cap
        self.adj[u].append(v)
        self.adj[v].append(u)

    def compute_max_flow(self, s, t):
        flow = 0
        while True:
            parent = {s: None}
            queue = collections.deque([s])
            while queue and t not in parent:
                u = queue.popleft()
                for v in self.adj[u]:
                    if self.capacity[(u, v)] > 0 and v not in parent:
                        parent[v] = u
                        queue.append(v)

            if t not in parent:
                break

            push = float("inf")
            curr = t
            while curr != s:
                p = parent[curr]
                push = min(push, self.capacity[(p, curr)])
                curr = p

            curr = t
            while curr != s:
                p = parent[curr]
                self.capacity[(p, curr)] -= push
                self.capacity[(curr, p)] += push
                curr = p

            flow += push

        return flow

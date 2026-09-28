from client import EdmondsKarpMaxFlow

ek = EdmondsKarpMaxFlow(4)
ek.add_edge(0, 1, 10)
ek.add_edge(0, 2, 10)
ek.add_edge(1, 2, 2)
ek.add_edge(1, 3, 4)
ek.add_edge(2, 3, 9)

print("Edmonds-Karp Max Flow:", ek.compute_max_flow(0, 3))

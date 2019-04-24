import networkx as nx
import queue


g = nx.Graph()

g.add_nodes_from([1,2,3,4,5])
g.add_weighted_edges_from([(1,2,1),(1,3,3),(2,3,1),(2,4,4),
                           (3,4,2),(3,5,3),(4,5,3)])

NEW = 0
OPEN = 1
CLOSED = 2

for n in g.nodes():
    g.nodes[n]["state"] = NEW

list(g.nodes())[0]
print(g.node[1])
q = queue.Queue()
print(q.empty())
q.put(1)
q.put(2)
print(q.get())
print(q.get())
print(list(g.neighbors(1)))

def bfs(g):
    first = list(g.nodes())[0]
    q = queue.Queue()
    q.put(first)
    g.nodes[first]["state"] = OPEN
    while not q.empty():
        n = q.get()
        print(n)
        for neigh in g.neighbors(n):
            if g.nodes[neigh]["state"] == NEW:
                q.put(neigh)
                g.nodes[neigh]["state"] = OPEN
        g.nodes[n]["state"] = CLOSED

bfs(g)
print(list(map(lambda x: x[1],nx.bfs_edges(g,1))))
print("Graf ma {} vrcholu a {} hran".format(g.number_of_nodes(),
                                            g.number_of_edges()))

print(list(nx.all_shortest_paths(g,1,5,'weight')))
print(nx.shortest_path(g,1,None,'weight'))
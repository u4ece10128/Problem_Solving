import numpy as np
import math


# caluclates the euclidean distance between two stations
def distance(x, y):
    return math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))

if __name__ == '__main__':

    # earth is located at origin
    earth = [0.00, 0.00, 0.00]
    zearth = [float(i) for i in (raw_input()).split()]

    n = int(raw_input())

    adj = np.zeros((n + 2, n + 2), dtype=np.float64)

    vertices = [earth, zearth]

    # vertices is the list of all the coordinates of the teleport stations
    for _ in range(n):
        station = [float(i) for i in (raw_input()).split()]
        vertices.append(station)

    edges = []

    # build an weighted adjacency matrix
    for i in range(0, n+2):
        for j in range(i+1, n+2):
            dist = np.around(distance(vertices[i], vertices[j]), decimals=2)
            edges.append((dist, i, j))
            if i != j:
                adj[i][j] = distance(vertices[i], vertices[j])
                adj[j][i] = adj[i][j]

    # sort the edges, ASC order
    edges.sort()

    nodes = [i for i in range(0, n+2)]
    parent = [-1] * (n+2)

    # Initialize the spanning tree adjacecny matrix, with default = False
    spt_adj = np.zeros((n + 2, n + 2), dtype=np.bool)

    def union(a, b):
        xset = find(a)
        yset = find(b)
        parent[xset] = yset

    def find(a):
        if parent[a] == -1:
            return a
        return find(parent[a])

    for edge in edges:
        vertex_a = edge[1]
        vertex_b = edge[2]

        print(edge)
        if not find(vertex_a) == find(vertex_b):
            union(vertex_a, vertex_b)
            spt_adj[vertex_a][vertex_b] = True
            spt_adj[vertex_b][vertex_a] = True

    print(spt_adj)
    # Re-Initialize visited to verify the path between earth to zearth
    vis = np.zeros((1, n + 2), dtype=np.bool)


    def dfs2(a, vis):

        vis[0][a] = True  # update the node as visited

        for i in range(0, n + 2):
            if spt_adj[a][i] and ~vis[0][i]:
                if i == 1:  # If location zearth reached
                    return adj[a][i], True
                w, found = dfs2(i, vis)
                if found:
                    return max(w, adj[a][i]), True
        return 0, False


    max_teleport = (dfs2(0, vis))

    print("Maximum Distance of the Safest Path:", np.around(max_teleport[0], decimals=2))

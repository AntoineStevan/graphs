from pprint import pprint


def dfs_rec(g: list, v: int, seen=[]) -> list:
    """
        Performs a recursive Depth First Search (DFS)
        traversal of graph g, starting from node v.

        Args
        ----
        g: list of lists of ints
            the adjacency lists of the graph
            representation.
        v: int, 0 <= v < |g|
            the starting node of DFS.
        seen: list of ints, optional
            the list of seen nodes, used for
            recursion.

        Return
        ------
        seen: list of ints
            the list of nodes explored, in order.
    """
    ## treat v.

    seen = seen + [v]  # add current node.

    # explore every neighbour nor already seen.
    for c in g[v]:
        if c not in seen:
            seen = dfs_rec(g, c, seen)
    return seen


def dfs(g: list, v: int) -> list:
    """
        Performs an iterative Depth First Search (DFS)
        traversal of graph g, starting from node v.

        Args
        ----
        g: list of lists of ints
            the adjacency lists of the graph
            representation.
        v: int, 0 <= v < |g|
            the starting node of DFS.

        Return
        ------
        seen: list of ints
            the list of nodes explored, in order.
    """
    seen = []     # list of explored nodes.
    to_see = [v]  # stack of remaining nodes.
    while len(to_see) != 0:
        x = to_see.pop()        # get node in FIFO.
        if x not in seen:       # skip if explored.
            seen.append(x)      #  \-> avoids duplicates.

            ## treat x.

            for c in g[x]:
                if c not in seen:
                    to_see.append(c)
    return seen


def bfs(g: list, v: int) -> list:
    """
        Performs an iterative Breadth First Search (BFS)
        traversal of graph g, starting from node v.

        Args
        ----
        g: list of lists of ints
            the adjacency lists of the graph
            representation.
        v: int, 0 <= v < |g|
            the starting node of DFS.

        Return
        ------
        seen: list of ints
            the list of nodes explored, in order.
    """
    seen = []     # list of explored nodes.
    to_see = [v]  # stack of remaining nodes.
    while len(to_see) != 0:
        x = to_see.pop(0)       # get node in FIFO.
        if x not in seen:       # skip if explored.
            seen.append(x)      #  \-> avoids duplicates.

            ## treat x.

            for c in g[x]:
                if c not in seen:
                    to_see.append(c)
    return seen


def argmin_dists(N: list, dists: list) -> int:
    """
        Computes the index stored in N corresponding
        with the minimal distance stored in dists.

        Args
        ----
        N: list of ints
            the list of integer indices.
        dists: list of numbers
            the list of distances used to sort the
            indices in N.

        Return
        ------
        i: integer
            the index of N which minimizes dists[j] for j in N.
    """
    i = N[0]
    m = dists[i]
    for j in N:
        if dists[j] < m:
            i = j
            m = dists[j]
    return i

def dijkstra(g: list, w: list, s: int) -> tuple:
    """
        Computes all shortest path starting from s, in graph
        g weighted by w.
        This shortest path computation uses Dijkstra's algorithm.

        Args
        ----
        g: list of lists of ints
            the adjacency lists of the graph
            representation.
        w: |g|x|g| matrix of positive numbers
            the matrix of all weights between pairs of vertices.
        s: int, 0 <= s < |g|
            the starting node of dijkstra's algorithm.

        Return
        ------
        dists: list of numbers
            the list of distances from s to any other vertex in g.
            s always has distance 0.
            dists[v] is the distance from s to v.
        preds: list of ints
            the list of predecessors along the shortest paths.
            s always has no predecessor, i.e. preds[s] = None.
            to build shortest path from s to v=c_n in g, start from
            preds[c_n] = c_n-1, then c_n-2 = preds[c_n-1], and so on until
            None is found. The path is s=c_1 -> c_2 -> ... -> c_n=v.
    """
    dists = [float("inf") for _ in g]  # node infinitely far away.
    preds = [None for _ in g]          # no predecessor.
    N = [k for k, _ in enumerate(g)]   # all nodes to be explored.

    dists[s] = 0  # s is as close as can be from s.
    while len(N) != 0:
        v = argmin_dists(N, dists)  # get "minimal-distance" node.
        N.remove(v)                 # and mark it explored.
        for n in g[v]:
            if n in N:
                d = dists[v] + w[v][n]  # update distance and predecessor
                if d < dists[n]:        # of n with new distance and node
                    dists[n] = d        # v.
                    preds[n] = v

    return dists, preds


# TODO
# binary heap.


# TODO
def a_star():
    ...


# TODO
def prim():
    ...


# TODO
# union-find


# TODO
def kruskal():
    ...


# TODO
def bellman_ford():
    ...


# TODO
def held_karp_bu():
    ...


# TODO
def held_karp_td():
    ...


def main():
    # graph on page 16 of Supaero's "FSD301 Optimization in graphs" lesson.
    g_p16 = [
               [1,3],
               [0,2],
               [3],
               [0,1,2]
            ]
    print("g_p16:")
    for i, li in enumerate(g_p16): print('\t', i, li)
    print("recursive DFS:", dfs_rec(g_p16,0))
    print("iterative DFS:", dfs(g_p16,0))
    print("iterative BFS:", bfs(g_p16,0))
    print()

    # graph on page 19 of Supaero's "FSD301 Optimization in graphs" lesson.
    g_p19 = [
               [1],
               [2,5],
               [3,6],
               [0],
               [],
               [3],
               [7],
               [],
               [0,7]
            ]
    print("g_p19:")
    for i, li in enumerate(g_p19): print('\t', i, li)
    print("recursive DFS:", dfs_rec(g_p19,0))
    print("iterative DFS:", dfs(g_p19,0))
    print("iterative BFS:", bfs(g_p19,0))
    print()

    # graph on page 35 of Supaero's "FSD301 Optimization in graphs" lesson.
    g_p35 = [
               [1,2],   # A
               [2,3,4], # B
               [1,3,4], # C
               [],      # D
               [3],     # E
            ]
    w_p35 = [
               [0,4,2,0,0], # A
               [0,0,3,2,3], # B
               [0,1,0,4,5], # C
               [0,0,0,0,0], # D
               [0,0,0,1,0], # E
            ]
    print("g_p35:")
    for i, (li, wi) in enumerate(zip(g_p35, w_p35)): print('\t', i, li, wi)
    print(dijkstra(g_p35, w_p35, 0))


if __name__ == "__main__":
    main()

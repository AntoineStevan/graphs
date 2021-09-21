from pprint import pprint


def dfs_rec(g: list[list[int]], v: int, seen=[]) -> list[int]:
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


def dfs(g: list[list[int]], v: int) -> list[int]:
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


def bfs(g: list[list[int]], v: int) -> list[int]:
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


def argmin_dists(N: list[int], dists: list[float]) -> int:
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

def dijkstra(
        g: list[list[int]],
        w: list[list[int]],
        s: int) -> tuple[list[float], list[int]]:
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


def argmin_dists_h(N: list[int], dists: list[float], h: lambda n,v: 0) -> int:
    """
        Computes the index stored in N corresponding
        with the minimal distance stored in dists.
        Uses a heuristic h.

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
        if dists[j] + h(j) < m:
            i = j
            m = dists[j] + h(j)
    return i

def a_star(
        g: list[list[int]],
        w: list[list[int]],
        s: int,
        h: lambda n,v: 0) -> tuple[list[float], list[int]]:
    """
        Computes all shortest path starting from s, in graph
        g weighted by w.
        This shortest path computation uses the A* algorithm.

        Args
        ----
        g: list of lists of ints
            the adjacency lists of the graph
            representation.
        w: |g|x|g| matrix of positive numbers
            the matrix of all weights between pairs of vertices.
        s: int, 0 <= s < |g|
            the starting node of the A* algorithm.
        h: function from [0, |g|-1]x[0, |g|-1] to R
            the heuristic used to guide the baseline Dijkstra's
            algorithm toward the goal.
            Allows to explore less nodes if h is well chosen.
            If h is expensive to compute, no guarantees are given
            by the following algorithm concerning speed.

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
        v = argmin_dists_h(N, dists, h)  # get "minimal-distance" node.
        N.remove(v)                      # and mark it explored.
        for n in g[v]:
            if n in N:
                d = dists[v] + w[v][n]  # update distance and predecessor
                if d < dists[n]:        # of n with new distance and node
                    dists[n] = d        # v.
                    preds[n] = v

    return dists, preds


def prim(
        g: list[list[int]],
        w: list[list[int]]) -> tuple[list[float], list[int]]:
    """
        Computes the Minimum Spanning Tree (MST) of graph g weighted by w.
        This MST implementation uses Prim's algorithm.
        Prim's algorithm is a greedy tree growth, from any node, with
        respect to the nodes of the graph.

        Args
        ----
        g: list of lists of ints
            the adjacency lists of the graph
            representation.
        w: |g|x|g| matrix of positive numbers
            the matrix of all weights between pairs of vertices.

        Return
        ------
        cheapest: list of numbers
            the list of cheapest weights inside the MST of g.
            s always has the cheapest, i.e. 0, weight.
            cheapest[v] is the cheapest weight inside MST for v.
        preds: list of ints
            the list of predecessors inside the Spanning Tree.
            s always has no predecessor, i.e. preds[s] = None.
            to build the resulting tree, read the preds list in reverse,
            from any node.
    """
    cheapest = [float("inf") for _ in g]  # node infinitely far away.
    preds = [None for _ in g]             # no predecessor.
    N = [v for v in range(len(g))]        # all nodes to be explored.

    cheapest[0] = 0
    while len(N) != 0:
        v = argmin_dists(N, cheapest)  # get "cheapest-weight" node.
        N.remove(v)                    # and mark it explored.
        for n in g[v]:
            if n in N:
                c = w[v][n]          # update cheapest weight and
                if c < cheapest[n]:  # predecessor of n with new 
                    cheapest[n] = c  # cheapest weight and node v.
                    preds[n] = v

    return cheapest, preds


def make_union_find(s: int) -> list[int]:
    """
        Creates a union-find structure, namely an array containing indices
        to go from any node in the tree.
        Starts with every node pointing to itself.

        Args
        ----
        s: int, positive
            the size of the union-find structure.

        Return
        ------
        uf: list of ints
            the initialized union-find structure.
    """
    return [k for k in range(s)]

def find(uf: list[int], u: int) -> int:
    """
        Finds the representative of element u in the union-find uf.
        No optimization is performed to reduce the size of the
        union-find whilst findind the representative.

        Args
        ----
        uf: list of ints
            a union-find structure.
        u: int
            the element of uf one wants the representative of.

        Return
        ------
        v: int
            the representative of u in the union-find uf.
    """
    if u == uf[u]:  # representative found.
        return u
    return find(uf, uf[u])

def union(uf: list[int], u: int, v: int) -> list[int]:
    """
        Performs the union of u and v, i.e. setting u's and v's
        representatives to the same value.
        No optimization is performed to reduce the size of the
        union-find whilst merging u and v.

        Args
        ----
        uf: list of ints
            a union-find structure.
        u: int
            one element of uf one wants to merge with v.
        v: int
            one element of uf one wants to merge with u.

        Return
        ------
        uf: list of ints
            a new union-find structure where u and v have the
            same representative.
    """
    uf[u] = find(uf, v)
    return uf

def kruskal(g: list[list[int]], w: list[list[int]]) -> list[(int, int)]:
    """
        Computes the Minimum Spanning Tree (MST) of graph g weighted by w.
        This MST implementation uses Kruskal's algorithm.
        Kruskal's algorithm is a greedy tree growth with respect to the
        edges of the graph.

        Args
        ----
        g: list of lists of ints
            the adjacency lists of the graph
            representation.
        w: |g|x|g| matrix of positive numbers
            the matrix of all weights between pairs of vertices.

        Return
        ------
        selected: list of tuple of 2 ints
            the list of edges used to build the MST.
    """
    edges = [(w[u][v],u,v) for u in range(len(w)) for v in range(len(w[u])) if u!=v]
    edges = sorted(edges)  # sort all the edges by weight.

    selected = []                  # no edge selected.
    uf = make_union_find(len(g))   # empty union-find.
    for wuv, u, v in edges:
        if find(uf, u) != find(uf, v):  # union and select edge
            uf = union(uf, u, v)        # if nodes do not have the
            selected.append((u,v))      # same representative.
    return selected


# TODO
def bellman_ford():
    ...


def held_karp_bu(g: list[list[int]], w: list[list[int]]) -> tuple[int, tuple[int, int]]:
    """
        Solves the Travelling SalesPerson (TSP) problem wy using Held-Karp's algorithm
        in its bottum-up version.

        Args
        ----
        g: list of lists of ints
            the adjacency lists of the graph
            representation.
        w: |g|x|g| matrix of positive numbers
            the matrix of all weights between pairs of vertices.

        Return
        ------
        solution: tuple with 1 int and a tuple of 2 ints
            the solution is composed of the total cost of the path and a tuple
            containing the hot-encoding of the nodes and the final node in the
            path.
    """
    L = {}  # L[{S},j] is the cost of the path ending in j and going through the nodes in S.
    for i in range(1, len(g)):
        L[(1<<i, i)] = w[0][i]

    # compute L from the bottom-up.
    for m in range(2, len(g)):
        # S is the hot-encoding of the nodes used in each subset, i.e.
        # if nodes 1 and 3 are used in a set of 4 nodes -> S = b1010
        for S in [S << 1 for S in range(2**(len(g)-1)) if sum(map(int, bin(S)[2:])) == m]:
            # conversion to the actual node numbers.
            S_ = [j for j in range(1, len(g)) if S>>j & 1]
            # dynamic programming part to go from m-1 to m.
            for j in S_:
                L[(S,j)] = min([L[(S & ~(1<<j), k)] + w[k][j] for k in S_ if k != j])

    # do not forget the cost for the way back to the starting node.
    return min([(L[(S, j)] + w[j][0], (S,j)) for j in range(1, len(g))])


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
    print("dijkstra:", dijkstra(g_p35, w_p35, 0))
    print()

    # graph on page 53 of Supaero's "FSD301 Optimization in graphs" lesson.
    g_p53 = [
               [1,2,3,4], # w
               [0,2,3,4], # 1
               [0,1,3,4], # 2
               [0,1,2,4], # 3
               [0,1,2,3]  # 4
            ]
    w_p53 = [
               [0,1,5,4,3], # w
               [1,0,5,2,5], # 1
               [5,5,0,3,4], # 2
               [4,2,3,0,2], # 3
               [3,5,4,2,0], # 4
            ]
    print("g_p53:")
    for i, (li, wi) in enumerate(zip(g_p53, w_p53)): print('\t', i, li, wi)
    print("prim:", prim(g_p53, w_p53))
    print("kruskal:", kruskal(g_p53, w_p53))
    print()
    
    # graph on page 86 of Supaero's "FSD301 Optimization in graphs" lesson.
    g_p86 = [
               [1,2,3], # A
               [0,2,3], # B
               [0,1,3], # C
               [0,1,2], # D
            ]
    w_p86 = [
               [0,2,1,4], # A
               [2,0,3,5], # B
               [1,3,0,6], # C
               [4,5,6,0], # D
            ]
    print("g_p86:")
    for i, (li, wi) in enumerate(zip(g_p86, w_p86)): print('\t', i, li, wi)
    print("held karp bu:", held_karp_bu(g_p86, w_p86))


if __name__ == "__main__":
    main()

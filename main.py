from pprint import pprint


def dfs_rec(g, v, seen=[]):
    ## treat v.
    seen = seen + [v]
    for c in g[v]:
        if c not in seen:
            seen = dfs_rec(g, c, seen)
    return seen


def dfs(g,v):
    seen = []
    to_see = [v]
    while len(to_see) != 0:
        x = to_see.pop()
        if x not in seen:
            seen.append(x)
            # treat x.
            for c in g[x]:
                if c not in seen:
                    to_see.append(c)
    return seen


def bfs(g,v):
    seen = []
    to_see = [v]
    while len(to_see) != 0:
        x = to_see.pop(0)
        if x not in seen:
            seen.append(x)
            # treat x.
            for c in g[x]:
                if c not in seen:
                    to_see.append(c)
    return seen


def argmin_dists(N, dists):
    i = N[0]
    m = dists[i]
    for j in N:
        if dists[j] < m:
            i = j
            m = dists[j]
    return i

def dijkstra(g,w,s):
    dists = [float("inf") for _ in g]
    preds = [None for _ in g]
    N = [k for k, _ in enumerate(g)]

    dists[s] = 0
    while len(N) != 0:
        v = argmin_dists(N, dists)
        N.remove(v)
        for n in g[v]:
            if n in N:
                d = dists[v] + w[v][n]
                if d < dists[n]:
                    dists[n] = d
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

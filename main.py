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
        seen.append(x)
        # treat x.
        for c in g[x]:
            if c not in seen and c not in to_see:
                to_see.append(c)
    return seen


def bfs(g,v):
    seen = []
    to_see = [v]
    while len(to_see) != 0:
        x = to_see.pop(0)
        seen.append(x)
        # treat x.
        for c in g[x]:
            if c not in seen and c not in to_see:
                to_see.append(c)
    return seen


# TODO
def dijkstra():
    ...


# TODO
# binary tree.


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

    print("graph on page 16:")
    for i, li in enumerate(g_p16): print(i, li)
    print("recursive DFS:", dfs_rec(g_p16,0))
    print("iterative DFS:", dfs(g_p16,0))
    print("iterative BFS:", bfs(g_p16,0))
    print()
    print("graph on page 19:")
    for i, li in enumerate(g_p19): print(i, li)
    print("recursive DFS:", dfs_rec(g_p19,0))
    print("iterative DFS:", dfs(g_p19,0))
    print("iterative BFS:", bfs(g_p19,0))


if __name__ == "__main__":
    main()

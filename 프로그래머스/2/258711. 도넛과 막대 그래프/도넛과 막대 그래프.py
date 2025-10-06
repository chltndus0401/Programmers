from collections import defaultdict, deque

def solution(edges):
    indeg = defaultdict(int)
    outdeg = defaultdict(int)
    graph = defaultdict(list)
    
    for a, b in edges:
        outdeg[a] += 1
        indeg[b] += 1
        graph[a].append(b)
    
    generated = -1
    for node in graph.keys():
        if outdeg[node] >= 2 and indeg[node] == 0:
            generated = node
            break
    
    donut = bar = eight = 0
    visited = set()
    
    for nxt in graph[generated]:
        if nxt in visited:
            continue
        q = deque([nxt])
        v_nodes = set()
        edge_count = 0
        while q:
            cur = q.popleft()
            if cur in v_nodes:
                continue
            v_nodes.add(cur)
            for nx in graph[cur]:
                edge_count += 1
                if nx not in v_nodes:
                    q.append(nx)
        visited |= v_nodes
        node_count = len(v_nodes)
        if node_count == edge_count:
            donut += 1
        elif node_count == edge_count + 1:
            bar += 1
        elif node_count + 1 == edge_count:
            eight += 1
    
    return [generated, donut, bar, eight]

# function to check if the given graph is DAG
def is_graph_dag(edges):
    from collections import defaultdict, deque
    
    # creating the adj list of graph
    adj_list = defaultdict(list)
    in_degree = defaultdict(int)
    
    # compute the indegree for each node and append the nodes in adj list
    for edge in edges:
        adj_list[edge.source].append(edge.target)
        in_degree[edge.target] += 1
        if edge.source not in in_degree:
            in_degree[edge.source] = 0
    
    queue = deque([node for node, degree in in_degree.items() if degree == 0])
    visited_nodes = 0
    
    while queue:
        node = queue.popleft()
        visited_nodes += 1
        
        for neighbor in adj_list[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return visited_nodes == len(in_degree)
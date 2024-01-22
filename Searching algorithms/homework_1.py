from collections import deque
# from prettytable import PrettyTable

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    print("Node     Frontier     Reached")
    str_result = ""

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            print(node, end="       ")
            str_result += node
           
            for neighbor in graph[node]:
                print(neighbor, end="")

            print("             ", end="")
            print(str_result)

            # Enqueue neighboring nodes that haven't been visited
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)



def dfs(graph, start, visited=None):
    # print("Node     Frontier     Reached")
    str_result = ""
    if visited is None:
        visited = set()

    
    # print(start, end="     ")
    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)










# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}



# Start BFS from node 'A'
# bfs(graph, 'A')

# Bắt đầu DFS từ đỉnh 'A'
dfs(graph, 'A')

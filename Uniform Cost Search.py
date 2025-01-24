from collections import deque

romania_map = {
    'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Arad':140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Bucharest': 101},
    'Craiova': {'Rimnicu Vilcea': 146, 'Dobreta': 120, 'Pitesti': 138},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Dobreta': 75},
    'Dobreta': {'Mehadia': 75, 'Craiova': 120},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101}
    }

def ucs(graph, start, goal):
    queue = deque([(start, [start], 0)])
    while queue:
        node, path, maliyet = queue.popleft()
        if node == goal:
            return path, maliyet
        for komsu, komsu_maliyet in graph[node].items():
            if komsu not in path:
                queue.append((komsu, path + [komsu], maliyet + komsu_maliyet))
    return None, None

path, maliyet = ucs(romania_map, 'Zerind', 'Dobreta')
print("Gidilen yol:", path)
print("Toplam maliyet:", maliyet)
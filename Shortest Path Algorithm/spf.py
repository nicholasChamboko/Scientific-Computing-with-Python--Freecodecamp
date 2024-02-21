nick = {
    'name' : 'Nicholas',
    'surname' : 'Chamboko',
    'age' : 30,
    'occupation' : 'IT Technician'
}

#A Graph declaration
#Node A is connected to B and C is connected to B
#B is a list because its has many connections
my_graph = {
    'A' : [('B', 'C',), ('D',1)],
    'B' : [('A', 3), ('C', 4)],
    'C' : [('B', 4), ('D', 7)],
    'D' : [('A', 1), ('C', 7)]
}

def shortest_path(graph, start):
    unvisited = list(graph)
    distances = {key: 0 if key == start else float('inf') for key in graph}
    paths = {key: [] for key in graph}
    paths[start].append(start)

    while not unvisited:
        pass
        print(f'Unvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}')

shortest_path(my_graph, 'A')
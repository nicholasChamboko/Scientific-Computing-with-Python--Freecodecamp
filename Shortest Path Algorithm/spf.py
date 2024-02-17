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
    'A' : [('B', 'C',),
           ('D',1)],
    'B' : ['A', 'C'],
    'C' : ['B', 'D'],
    'D' : ['A', 'C']
}
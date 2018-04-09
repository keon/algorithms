"""
Given a list of system packages,
some packages cannot be installed until the other packages are installed.
Provide a valid sequence to install all of the packages.

e.g.
a relies on b
b relies on c

then a valid sequence is [c, b, a]
"""

depGraph = {

    "a" : [ "b" ],
    "b" : [ "c" ],
    "c" :  [ 'e'],
    'e' : [ ],
    "d" : [ ],
    "f" : ["e" , "d"]
}


given = [ "b", "c", "a", "d", "e", "f" ]

given = [ "b", "c", "a", "d", "e", "f" ]
def retDeps(G, out, visited, start):
    if start in visited:
      return
    visited.add(start)
    for child in G[start]:
      retDeps(G, out, visited, child)
    out.append(start)


def retDepGraph(G):
    visited = set()
    out = []
    for pac in given:
      retDeps(G, out, visited, pac)
    print(out)
  
retDepGraph(depGraph)

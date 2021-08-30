colors = ['Red', 'Blue', 'Green', 'Yellow', 'Black', 'Brown', 'Purple']
nodes = ['0', '1', '2', '3', '4']
neighbors = {}

neighbors['0'] = ['1', '2']
neighbors['1'] = ['0', '2', '3']
neighbors['2'] = ['0', '1', '3']
neighbors['3'] = ['1', '2', '4']
neighbors['4'] = ['3']

colors_of_nodes = {}


def promising(node, color):
    for neighbor in neighbors.get(node):
        color_of_neighbor = colors_of_nodes.get(neighbor)
        if color_of_neighbor == color:
            return False
    return True


def get_color_for_node(node):
    for color in colors:
        if promising(node, color):
            return color


def main():
    for node in nodes:
        colors_of_nodes[node] = get_color_for_node(node)

    print(colors_of_nodes)


main()
listOfValues = colors_of_nodes.values()
listOfValues = list(set(listOfValues))
print("Chromatic Number is : " + str(len(listOfValues)))

def rotate_clockwise(matrix):
    new = []
    for row in reversed(matrix):
        for i, elem in enumerate(row):
            try:
                new[i].append(elem)
            except IndexError:
                new.insert(i, [])
                new[i].append(elem)
    return new


def rotate_counterclockwise(matrix):
    new = []
    for row in matrix:
        for i, elem in enumerate(reversed(row)):
            try:
                new[i].append(elem)
            except IndexError:
                new.insert(i, [])
                new[i].append(elem)
    return new


def top_left_invert(matrix):
    new = []
    for row in matrix:
        for i, elem in enumerate(row):
            try:
                new[i].append(elem)
            except IndexError:
                new.insert(i, [])
                new[i].append(elem)
    return new


def bottom_left_invert(matrix):
    new = []
    for row in reversed(matrix):
        for i, elem in enumerate(reversed(row)):
            try:
                new[i].append(elem)
            except IndexError:
                new.insert(i, [])
                new[i].append(elem)
    return new


if __name__ == '__main__':
    def print_matrix(matrix, name):
        print('{}:\n['.format(name))
        for row in matrix:
            print('  {}'.format(row))
        print(']\n')

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    print_matrix(matrix, 'initial')
    print_matrix(rotate_clockwise(matrix), 'clockwise')
    print_matrix(rotate_counterclockwise(matrix), 'counterclockwise')
    print_matrix(top_left_invert(matrix), 'top left invert')
    print_matrix(bottom_left_invert(matrix), 'bottom left invert')

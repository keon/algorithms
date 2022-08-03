"""
Manhattan Distance in Machine Learning

Also refered as city block distance or taxi cab distance.

The sum of absolute difference between coordinates of two points.

distance = |x2 - x1| + |y2 - y1|

"""
def manhattan_distance(coords1, coords2):
    
    distance = 0
    for x1, x2 in zip(coords1, coords2):
            distance += abs(x1-x2)

    return distance

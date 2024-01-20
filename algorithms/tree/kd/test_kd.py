# This is provided to you so that you can test your bst.py file with a particular tracefile.

import argparse
import csv
import kd

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-tf', '--tracefile')
    args = parser.parse_args()
    tracefile = args.tracefile

    t = None
    with open(tracefile, "r") as f:
        reader = csv.reader(f)
        lines = [l for l in reader]
        for l in lines:
            if l[0] == 'initialize':
                t = kd.KDtree(int(l[1]),int(l[2]))
            if l[0] == 'insert':
                t.insert(tuple([int(i) for i in l[2:]]),l[1])
            if l[0] == 'delete':
                t.delete(tuple([int(i) for i in l[1:]]))
            if l[0] == 'knn':
                print(t.knn(int(l[1]),tuple([int(i) for i in l[2:]])))
            if l[0] == 'dump':
                print(t.dump())
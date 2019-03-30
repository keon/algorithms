mouvement = 0


def TowerOfHanoi(n, source, dest, by):
    global mouvement
    mouvement += 1
    if n == 1:
        print('Move the plate from ', source, ' to ', dest)
    else:
        TowerOfHanoi(n-1, source, by, dest)
        print('Move the plate from ', source, ' to ', dest)
        TowerOfHanoi(n-1, by, dest, source)


# Driver Code
n = int(input("Enter the number of plates : "))
TowerOfHanoi(n, 'source', 'by', 'dest')
print('Total moves :' + str(mouvement))

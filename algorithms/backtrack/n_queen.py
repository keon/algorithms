def place(k, i):
    for l in range(1, k):
        if (x[l] == i) or (abs(x[l] - i) == abs(l - k)):
            return False
    return True


def nqueens(k):
    global x, n, flag

    for j in range(1, n + 1):  # iterate over all columns
        if place(k, j):
            x[k] = j
            if k == n:
                print(x[1 : n + 1])
                flag = 1
            else:
                nqueens(k + 1)


def main():
    global n, x, flag
    flag = 0
    n = input("Enter n for n-queen problem solution:")
    x = [i for i in range(n + 1)]
    for m in range(1, n + 1):
        print("\nFirst queen is placed in column:", m, "\n")
        x[1] = m
        nqueens(2)
        if flag == 0:
            print("No solution exists for queen placed in column:", m)
        print("\n")


if __name__ == "__main__":
    main()
    
 #By cosmos

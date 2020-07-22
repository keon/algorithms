def subsetsum(cs, k, r, x, w, d):
    x[k] = 1
    if cs + w[k] == d:
        for i in range(0, k + 1):

            if x[i] == 1:
                print(w[i], end=" ")
        print()

    elif cs + w[k] + w[k + 1] <= d:
        subsetsum(cs + w[k], k + 1, r - w[k], x, w, d)

    if (cs + r - w[k] >= d) and (cs + w[k] <= d):
        x[k] = 0
        subsetsum(cs, k + 1, r - w[k], x, w, d)


# driver for the above code
# Main array w
w = [2, 3, 4, 5, 0]
x = [0 for i in range(len(w))]
print("Enter the no u want to get the subsets sum for")
num = int(input())
if num <= sum(w):
    print("The subsets are:-\n")

    subsetsum(0, 0, sum(w), x, w, num)
else:
    print(
        "Not possible The no is greater than the sum of all the elements in the array"
    )

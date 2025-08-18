def remove_dups(string):
    res = string[0]
    for ch in string:
        if res[-1] != ch:
            res += ch
    return res


input_string = input("Enter string: ")
res_str = remove_dups(input_string)
print("Resultant string: ", res_str)

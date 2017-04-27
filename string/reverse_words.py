
def reverse_words(str):
	res = " "
	for a in str.split(" "):
		res = a + " " + res
	return res

if __name__ == "__main__":
    test = "I am keon kim and I like pizza"
    print(test)
    print(reverse_words(test))

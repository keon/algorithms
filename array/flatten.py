"""
Implement Flatten Arrays.
Given an array that may contain nested arrays,
give a single resultant array.

function flatten(input){
}

Example:

Input: var input = [2, 1, [3, [4, 5], 6], 7, [8]];
flatten(input);
Output: [2, 1, 3, 4, 5, 6, 7, 8]
"""


def list_flatten(l, a=None):
    a = list(a) if isinstance(a, (list, tuple)) else []
    for i in l:
        if isinstance(i, (list, tuple)):
            a = list_flatten(i, a)
        else:
            a.append(i)
    return a


# stack version
# public static List<Integer> flatten(List<NestedList> l) {
# List<Integer> main = new ArrayList<Integer>();
		# Stack<List<NestedList>> stack = new Stack<List<NestedList>>();
		# Stack<Integer> indexes = new Stack<Integer>();
		# stack.add(l);
		# indexes.add(0);
		# while (true) {
			# if (stack.isEmpty())
				# break;
			# int index1 = indexes.pop();
			# l = stack.pop();
			# for (int i = index1; i < l.size(); i++) {
				# NestedList n = l.get(i);
				# if (n.isInteger()) {
					# main.add(n.value);
				# } else {
					# stack.add(l);
					# indexes.add(i+1);
					# l = n.list;
					# stack.add(l);
					# indexes.add(0);
					# break;

				# }
			# }
		# }

		# return main;
# }

# Report for assignment 3

This is a template for your report. You are free to modify it as needed.
It is not required to use markdown for your report either, but the report
has to be delivered in a standard, cross-platform format.

## Project

Name: Algorithms
URL: https://github.com/keon/algorithms
Description: A python library containing minimal examples of algorithm and datastructure implementations.

## Onboarding experience

### 1. How easily can you build the project? Briefly describe if everything worked as documented or not:

#### (a) Did you have to install a lot of additional tools to build the software?

No additional tools were required to build the project. As it is a python project it did not need to be built, either.

#### (b) Were those tools well documented?

As there were no tools, no documentation was necessary.

#### (c) Were other components installed automatically by the build script?

The testing components were added in a requirements.txt file, and thus installed automatically.

#### (d) Did the build conclude automatically without errors?

Yes. The project built without any errors.

#### (e) How well do examples and tests run on your system(s)?

The tests ran without errors.

#### Summary

The project was easy to get started and running. No extra components or tools were necessary to run the program, and the components necessary for the tests were listed in a requirements.txt file. While the versions of each tool was not added to the requirements.txt file, it was not necessary in this case either as no errors were encountered. Had errors been encountered, however, it would be preferable to have the version numbers in case.

# Glossary:

*NLOC* : Number of Lines of Code
*CC* : Cyclomatic Complexity

## Complexity

1. What are your results for ten complex functions?
   * Did all methods (tools vs. manual count) get the same result?

   The results for each function is presented as follows:

   ### Cyclomatic Complexities:

   #### Strip_URL_Params:

   algorithms/algorithms/strings/strip_url_params.py
   strip_url_params1@14-68@

   CC = 20
   NLOC = 50

   #### Intersection:

   algorithms/algorithms/linkedlist/intersection.py
   intersection@21-64@

   CC = 14
   NLOC = 31
   **CC_Manual = 14**

   #### maximum_flow_bfs

   algorithms/graph/maximum_flow_bfs.py
   maximum_flow_bfs@28-84@

   CC = 10
   NLOC = 55
   #### maximum_flow_dfs

   algorithms/graph/maximum_flow_dfs.py
   maximum_flow_dfs@27-83@

   CC = 10
   NLOC = 55
   **CC_Manual = 10**

   #### three_sum

   ./algorithms/array/three_sum.py
   three_sum@18-48@

   CC = 11
   NLOC = 30
   #### Text_justification

   ./algorithms/strings/text_justification.py
   text_justification@34-89@ Count by hand = 13

   CC = 13
   NLOC = 55
   **CC_Manual = 13**

   #### multiply:

   algorithms/algorithms/matrix/sparse_mul.py:
   multiply@71-99@

   CC = 18
   NLOC = 24
   **CC_manual = 16**

   #### delete_fixup:

   algorithms/algorithms/tree/red_black_tree/red_black_tree.py:
   delete_fixup@209-267@

   CC = 14
   NLOC = 31

   ### count_islands:

   ./algorithms/bfs/count_islands.py
   count_islands@40-65@

   CC = 14
   NLOC = 25
   **CC_Manual = 14**

   ### pacific_atlantic:

   ./algorithms/dfs/pacific_atlantic.py
   pacific_atlantic@32-54@

   CC = 14
   NLOC = 22

   * Are the results clear?

   The results are mostly clear, bar one function which did not return the same cyclomatic complexity as the *Lizard* tool. Every other function returned the same result during the manual count as well as the automatic count. While we are not entirely certain as to why, we did perform certain experiments to assess how Lizard calculates the cyclomatic complexity of the functions, but as the tool is not open we could not come to any conclusive results. We do speculate however, as the Lizard tool itself states in its documentation: "This tool actually calculates how complex the code ‘looks’ rather than how complex the code really ‘is’", there might be some discrepancies regarding functions of a higher complexity as those become more complex.

2. Are the functions just complex, or also long?

While the sample size of this assignment is small, there seems to be no correlation between the NLOC and the CC, which seems to be a popular trend within Python in general. It appears to have more to do with the overall function of the code rather than its complexity, as it almost appears to be an inverse relation for the functions that we have picked. While the most complex function also has the most NLOC, this appears to just be a coincidense.

3. What is the purpose of the functions?

   #### Strip_URL_Params:

   The function takes a URL with a parameter string as an input, it then looks for duplicate parameters and removes them. One can also provide an array of parameters one would like to strip, and the functions removes any instance of those parameters within the URL.

   #### Intersection:

   The function takes two linked lists and checks if they share a node. If the nodes are shared (not node values) the function returns the first shared node in question.

   #### maximum_flow_bfs

   The function takes an m x n matrix of non-negative integers representing the height of each unit cell in a continent and return the position with parameters.

   #### maximum_flow_dfs

   Calculates the maximum flow through a graph given an adjencency list using depth for search.
   #### three_sum

   In a list of integers, find a set of three distinct integers that adds up to 0.
   #### Text_justification

   Formats a string to have a specified amount of characters on each line and evenly distributes the spaces without cutting words in two.

   #### multiply:

   Calculates the maximum flow through a graph given an adjencency list using depth for search.

   #### delete_fixup:

   This function takes a node from a red black tree. The purpose of this function is handling the rotation of a red black tree after deleting some node in the tree.

   ### count_islands:

   The function takes a 2D-array and counts the number of islands. If 1 (lands) are surrounded by 0 (water), it will be counted as an island.

   ### pacific_atlantic:

   The function takes an m x n matrix of non-negative integers representing the height of each unit cell in a continent and return the position with parameters.


4. Are exceptions taken into account in the given measurements?

During the manual count we took exceptions into account, however, most of the functions did not make use of exceptions. We did some experimenting with regards to exceptions for the Lizard tool, and we arrived at the conclusion that it seems that the Lizard tool regards exceptions as return statements, that is they were disregarded.

5. Is the documentation clear w.r.t. all the possible outcomes?

The documentation is very bare-bones, barely describing the functionality of each function, and when the functions are described barely one of the cases (always a working case) are described. We thus found the documentation to be extremely lacking in general. The documentation does not appear to follow any conventions or standards for documentations either, except using the Python Docstring denominator.

## Refactoring

Plan for refactoring complex code:
Estimated impact of refactoring (lower CC, but other drawbacks?).
Carried out refactoring (optional, P+):
git diff ...

## Coverage

### Tools

Document your experience in using a "new"/different coverage tool.
How well was the tool documented? Was it possible/easy/difficult to
integrate it with your build environment?

### Your own coverage tool

Show a patch (or link to a branch) that shows the instrumented code to
gather coverage measurements.
The patch is probably too long to be copied here, so please add
the git command that is used to obtain the patch instead:
git diff ...
What kinds of constructs does your tool support, and how accurate is
its output?

### Evaluation

1. How detailed is your coverage measurement?
2. What are the limitations of your own tool?
3. Are the results of your tool consistent with existing coverage tools?

## Coverage improvement

Show the comments that describe the requirements for the coverage.
Report of old coverage: [link]
Report of new coverage: [link]
Test cases added:
git diff ...
Number of test cases added: two per team member (P) or at least four (P+).

## Self-assessment: Way of working

Current state according to the Essence standard: ...
Was the self-assessment unanimous? Any doubts about certain items?
How have you improved so far?
Where is potential for improvement?
## Overall experience

What are your main take-aways from this project? What did you learn?
Is there something special you want to mention here?
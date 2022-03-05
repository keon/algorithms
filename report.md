# Report for assignment 4

This is a template for your report. You are free to modify it as needed.
It is not required to use markdown for your report either, but the report
has to be delivered in a standard, cross-platform format.

## Project

Name: keon/algorithms

URL: The forked repo can be found in [this link](https://github.com/AmandaStromdahl/algorithms).

The chosen project is a Python repository that implements various algorithms and data structures.

## Onboarding experience

For this task our group chose a new project to work with. The onboarding experience between the two projects are distinctly different. The last repository we worked with was quite minimalistic in terms of basic usage instructions. For example did the last repository not explain how to run the tests. This repository on the other hand clearly states how to run the tests, install dependencies and so on. Eeach implemented algorithm is also conveniently listed in the readme. Overall the onboarding experience is a lot smoother compared to the last project.

## Effort spent

For each team member, how much time was spent in

1. plenary discussions/meetings;

2. discussions within parts of the group;

3. reading documentation;

4. configuration and setup;

5. analyzing code/output;

6. writing documentation;

7. writing code;

8. running code?

For setting up tools and libraries (step 4), enumerate all dependencies
you took care of and where you spent your time, if that time exceeds
30 minutes.

## Overview of issue(s) and work done.

Title: "Add Bitmasking in DP #480"

URL: The issue can be found in [this link](https://github.com/keon/algorithms/issues/480).

The task is to implement the bitmasking-and-dp-algorithm. This algorithm solves the problem of determining how many ways there are to assign unique caps to every person in a set of people, where each person has their own set of caps.

The issue will require a new file to be added to the dp-folder. Since the implementation doesn't already exist in the repo, no existing code will be affected. The algorithm will most likely require one or more helper functions. The scope of the issue is small enough to be able to finish the issue within a few days.

## Requirements for the new feature or requirements affected by functionality being refactored

Each of the following requirements will be linked to new tests, since no tests related to the issue exist previously. The requirements named R1.x are related to the cap assignment problem, whereas the remaining requirments named R2.x concern the TSP implementation.

| ID   |                     Title                     |                                                                                                                                                    Description |
| :--- | :-------------------------------------------: | -------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| R1.1 | Nr of cap sets less than 1 or greater than 10 |                                                                                             If the nr of cap sets is <1 or >10, a ValueError should be raised. |
| R1.2 |              Person without caps              |                                                         If there is at least one person that doesn't have any caps, there should be 0 ways to assign the caps. |
| R1.3 |           No unique cap assignment            |                                  Assume there are >0 people and at least one cap per person. If there is no unique assignment of caps, the output should be 0. |
| R1.4 |      One or more unique cap assignments       |                       Assume there are >0 people and at least one cap per person. If there is at least one unique assignment of caps, the output should be >0. |
| R2.1 |                   No nodes                    |                                                                                                        If the nr of nodes is 0, a ValueError should be raised. |
| R2.2 |                   One node                    |                                                                                                               If the nr of nodes is 1, the output should be 0. |
| R2.3 |             Positive path length              | If there are at least two nodes that are >0 length units apart, the output should be a number >0 that corresponds to the length of the shortest Euler circuit. |
| R2.4 |                  No solution                  |                                  If the nr of nodes is >1 and there is at least one node that cannot be reached from any other node, the output should be inf. |
| R2.5 |               Faulty dimensions               |                                              If the dimensions of the given graph don't correspond to the dimension parameters, a ValueError should be raised. |

## Algorithm description

To solve this problem, we will use bitmasking and dynamic programming. Bitmasking is used to represent subsets of a collection of elements as bits sequences called _masks_. In these sequences, a bit set to 1 means that the associated element is part of the subset. More specifically, if the _i-th_ bit is set to 1, then the _i-th_ element is part of the subset defined by this sequence. For example, if we have a collection of 10 elements, the bits sequence 0111010000 means that the associated subset contains element 2, 3, 4 and 6.

In our case, bitmasking will be used to represent whether a person is wearing a hat. In other words, a _i-th_ bit set to 1 means that the _i-th_ person is wearing a hat. Therefore the final cases we're interested into are the ones when the mask is completely full, i.e. all bits are set to 1.

Let's have a look on the dynamic programming formula. The table storing the intermediate results is a $M\times N$ matrix where:

- $M$ is the total number of masks, which is equal to $2^n$ where $n$ is the number of people
- $N$ is the total number of hats

And so the formula goes as follow:

`countWaysUntil(mask, k_hat) = countWaysUntil(mask, k_hat + 1) + `$\sum_{i=0}^{n}$` countWaysUntil(mask | (1 << i), k_hat + 1)`

More specifically, this formula says that the number of ways satisfying the problem for a specific mask (i.e. hat wearing status of the people) and taking into account all hats from the _k-th_ one until hat $N$ is defined by the sum of

1. the number of ways satisfying the problem without taking the _k-th_ hat into account
2. the sum of the number of ways satisfying the problem when each person, that have the _k-th_ hat in their collection and are not currently wearing a hat, wears it.

Note that before the computation of the formula, we have to check three cases:

1. if the mask is full, then it means that we found a way of satisfying the problem, hence we return 1
2. if the hat index is bigger than the total number of hats, it means that there are no more hats left and we could not find a satisfying ways to the problem. Therefore we return 0
3. if the number of ways of the mask and the _k-th_ hat has already been computed, then we just return the result from the dynamic programming table/matrix

Finally the result will be stored is the matrix cell `[0][1]`.

## Code changes

### Patch

(copy your changes or the add git command to show them)

git diff ...

Optional (point 4): the patch is clean.

Optional (point 5): considered for acceptance (passes all automated checks).

## Test results

The repository has initially a [complete folder](tests/) dedicated to the tests, after running the command `python3 -m pytest tests` given in the [README](README.md), we can see that there are already 394 tests implemented. Note that all the tests succeed. To have a bit more information about the initial coverage of the tests, we ran the `coverage.py` tool that we already used for the last assignment. It turns out that the initial coverage is quite good: 89% (961 misses for 8762 statements). These two results have been logged in [this file](initial_tests_log.txt).

Concerning our issue, since it is related to a new algorithm, there are obviously not tests about it. However, we can still have a look on the [tests folder](tests/). We notice that the tests are divided into files, each of which represents a specific algorithms field where the algorithms are separated in the [algorithms folder](algorithms/). For instance, all algorithms related to [graph](algorithms/graph/) are tested in the file [test_graph.py](tests/test_graph.py). Inside one of these test files, the tests are divided into classes, each representing the test class for a specific algorithm. For example, in the test file [test_graph.py](tests/test_graph.py), one of the class is `class TestTarjan` that contains multiple tests for the [_Tarjan's algorithm_](https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm).

Hence we create the class that will allow us to test the new algorithm of our issue: 'class `TestBitmasking` in the file [test_dp.py](tests/test_dp.py). Each [requirement](TODO) will have its own method that test it inside this class.

## UML class diagram and its description

### Key changes/classes affected

Optional (point 1): Architectural overview.

Optional (point 2): relation to design pattern(s).

## Overall experience

What are your main take-aways from this project? What did you learn?

How did you grow as a team, using the Essence standard to evaluate yourself?

Optional (point 6): How would you put your work in context with best software engineering practice?

Optional (point 7): Is there something special you want to mention here?

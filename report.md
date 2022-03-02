# Report for assignment 4

This is a template for your report. You are free to modify it as needed.
It is not required to use markdown for your report either, but the report
has to be delivered in a standard, cross-platform format.

## Project

Name:

URL:

One or two sentences describing it

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

Title:

URL:

Summary in one or two sentences

Scope (functionality and code affected).

## Requirements for the new feature or requirements affected by functionality being refactored

Optional (point 3): trace tests to requirements.

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

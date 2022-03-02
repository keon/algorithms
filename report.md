# Report for assignment 4

This is a template for your report. You are free to modify it as needed.
It is not required to use markdown for your report either, but the report
has to be delivered in a standard, cross-platform format.

## Project

Name: keon/algorithms

URL: The forked repo can be found in [this link](https://github.com/AmandaStromdahl/algorithms).

The chosen project is a Python repository that implements various algorithms and data structures.

## Onboarding experience

Did you choose a new project or continue on the previous one?

If you changed the project, how did your experience differ from before?

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

Each of the following requirements will be linked to new tests, since no tests related to the issue exist previously.

| ID  |               Title                |                                                                                                                                                     Description |
| :-- | :--------------------------------: | --------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| R1  |        Empty set of people         |                                                                                           If the set of people is empty, there should be 0 ways to assign caps. |
| R2  |        Person without caps         |                                                          If there is at least one person that doesn't have any caps, there should be 0 ways to assign the caps. |
| R3  |     More cap sets than people      | People and cap sets should have a 1-1 mapping. If there are more cap sets than people, there should be an `IllegialArgumentException()` to signal faulty input. |
| R4  |     Less cap sets than people      | People and cap sets should have a 1-1 mapping. If there are less cap sets than people, there should be an `IllegialArgumentException()` to signal faulty input. |
| R5  |      No unique cap assignment      |                                   Assume there are >0 people and at least one cap per person. If there is no unique assignment of caps, the output should be 0. |
| R6  | One or more unique cap assignments |                        Assume there are >0 people and at least one cap per person. If there is at least one unique assignment of caps, the output should be >0. |

## Code changes

### Patch

(copy your changes or the add git command to show them)

git diff ...

Optional (point 4): the patch is clean.

Optional (point 5): considered for acceptance (passes all automated checks).

## Test results

Overall results with link to a copy or excerpt of the logs (before/after
refactoring).

## UML class diagram and its description

### Key changes/classes affected

Optional (point 1): Architectural overview.

Optional (point 2): relation to design pattern(s).

## Overall experience

What are your main take-aways from this project? What did you learn?

How did you grow as a team, using the Essence standard to evaluate yourself?

Optional (point 6): How would you put your work in context with best software engineering practice?

Optional (point 7): Is there something special you want to mention here?

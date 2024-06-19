# Report for Assignment 1

## Project chosen

Name: algorithms    

URL: (https://github.com/keon/algorithms)

Number of lines of code and the tool used to count it: 18023(18 KLOC), counted using lizard

Programming language: Python

## Coverage measurement

### Existing tool

We have used coverage.py to measure the cover of our chosen project. After installing all tools and dependencies, we have 
run the tool by typing coverage run --branch -m pytest tests. Afterwards, we use coverage report to generate the report. Later, Ayman has written a scrip to run the commands in a single script, and to also skip the test files, which don't need to be tested.

In order to not put in 8 large images, I will insert the final screenshot, with the total branch coverage:
![image](https://github.com/CatalinAnt/algorithms-SEP-95/assets/113595149/f1cd3fab-b00c-4cd0-89d0-6452e7ed1a63)


### Your own coverage tool

<The following is supposed to be repeated for each group member>

<Group member name>

<Function 1 name>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements>

<Provide a screenshot of the coverage results output by the instrumentation>

<Function 2 name>

<Provide the same kind of information provided for Function 1>

## Coverage improvement

### Individual tests

<The following is supposed to be repeated for each group member>

<Group member name>

<Test 1>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>

<Provide a screenshot of the old coverage results (the same as you already showed above)>

<Provide a screenshot of the new coverage results>

<State the coverage improvement with a number and elaborate on why the coverage is improved>

<Test 2>

<Provide the same kind of information provided for Test 1>

## Ayman Errahmouni

#### <Test "test_simplify_path">

An enhanced existing test

Old coverage:<br>
![old coverage result (24%)](image-2.png)

Diff (LHS = new code, RHS = old code):<br>
![LHS: new code, RHS: old code](image.png)

New coverage:<br>
![new coverage result (100%)](image-1.png)

The coverage was improved because certain cases that could happen in file paths (e.g. the "." directory, empty path) were not tested for.
By added additional tests that use such cases, the coverage improved.

The test was also faulty on windows (i guess linux was assumed), so i added support for that in the test. (It now passes on Windows 10 too)

#### <Test "test_actual_insertion_sort">

An new test. (before, `insertion_sort` was not present in any test)

Diff (LHS: new code, RHS: old code):<br>
(New test)<br>
![LHS: new code, RHS: old code](image-5.png)<br>
(Changes in imports)<br>
![LHS: new code, RHS: old code](image-6.png)

Old coverage:<br>
![Old coverage result (4%)](image-3.png)

New coverage:<br>
![alt text](image-4.png)

<State the coverage improvement with a number and elaborate on why the coverage is improved>


## Catalin Antonescu

#### Function 1: strong_password

Link to final commit:
https://github.com/CatalinAnt/algorithms-SEP-95/commit/eaad6d32ecd73bb8fde876a4d4852cb522aea6f8

Screenshot of branch measurement:
![image](https://github.com/CatalinAnt/algorithms-SEP-95/assets/113595149/e718a47f-5ea0-412c-b250-25a193412164)

#### Function 2: rotate_image

Link to final commit:(same as for the first one)
https://github.com/CatalinAnt/algorithms-SEP-95/commit/eaad6d32ecd73bb8fde876a4d4852cb522aea6f8

Screenshot of branch measurement:
![image](https://github.com/CatalinAnt/algorithms-SEP-95/assets/113595149/94eec9b6-3dd6-46e3-b087-40892eccc10e)

<Provide the same kind of information provided for Function 1>

## Coverage improvement

### Individual tests

<The following is supposed to be repeated for each group member>

<Group member name>

<Test 1>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>

<Provide a screenshot of the old coverage results (the same as you already showed above)>

<Provide a screenshot of the new coverage results>

<State the coverage improvement with a number and elaborate on why the coverage is improved>

<Test 2>

<Provide the same kind of information provided for Test 1>



### Overall

<Provide a screenshot of the old coverage results by running an existing tool (the same as you already showed above)>

<Provide a screenshot of the new coverage results by running the existing tool using all test modifications made by the group>

## Statement of individual contributions

<Write what each group member did>

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


### Abdullah Abdelkhalik


pythagoras

https://github.com/CatalinAnt/algorithms-SEP-95/commit/5651abafebe8ae3a5ea63e74883bb991acf19303

![pythagoras_hits](https://github.com/CatalinAnt/algorithms-SEP-95/assets/114078193/0df1fa2b-2185-4b9f-ae65-5d969edb009b)


first_unique_char

https://github.com/CatalinAnt/algorithms-SEP-95/commit/c16f26e952322b2c1729778a4141a57103ba7658

![first_unique_char_hits](https://github.com/CatalinAnt/algorithms-SEP-95/assets/114078193/10d7c45c-398e-4408-8f11-6771f51fa95c)


## Coverage improvement

### Individual tests

<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>

<Provide a screenshot of the old coverage results (the same as you already showed above)>

<Provide a screenshot of the new coverage results>

<State the coverage improvement with a number and elaborate on why the coverage is improved>

<Test 2>

<Provide the same kind of information provided for Test 1>

Abdullah Abdelkhalik

test_maths

https://github.com/CatalinAnt/algorithms-SEP-95/commit/60832d9c672efd586848077cc41a52630d34371b

![pythagoras_before](https://github.com/CatalinAnt/algorithms-SEP-95/assets/114078193/cf57112b-1aef-4a10-a41f-bd4b797e2012)

![pythagoras_after](https://github.com/CatalinAnt/algorithms-SEP-95/assets/114078193/1aa45c17-46fc-49d3-944a-03c2276d1be6)

the coverage is improved by 28%, the code only hit one of the five branches and cover only one of the three cases of the pythagoras theory. I added the other two cases, i could have a fourth case where none of the cases is present.

test_strings

https://github.com/CatalinAnt/algorithms-SEP-95/commit/5651abafebe8ae3a5ea63e74883bb991acf19303

![first_unique_char_before](https://github.com/CatalinAnt/algorithms-SEP-95/assets/114078193/9910ec69-73b0-4c87-afc8-abc01f65a423)

![first_unique_char_after](https://github.com/CatalinAnt/algorithms-SEP-95/assets/114078193/10859fac-776c-4a48-8a1c-9531afcbfa9b)

the coverage is improved by 13%, the code only hit three out of five branches and only set up two examples. I added a case where there is no unique letter.


### Overall

<Provide a screenshot of the old coverage results by running an existing tool (the same as you already showed above)>

<Provide a screenshot of the new coverage results by running the existing tool using all test modifications made by the group>

## Statement of individual contributions

<Write what each group member did>

Abdullah -> increased the coverage for two functions.

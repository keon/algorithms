# Report for Assignment 1

## Project chosen

Name: algorithms    

URL: (https://github.com/keon/algorithms)

Number of lines of code and the tool used to count it: (TODO), counted using lizard

Programming language: Python

## Coverage measurement

### Existing tool

<Inform the name of the existing tool that was executed and how it was executed>

<Show the coverage results provided by the existing tool with a screenshot>

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

<Ayman Errahmouni>

<Test "test_simplify_path">

Old coverage:<br>
![old coverage result (24%)](image-2.png)

Diff (LHS = new code, RHS = old code):<br>
![LHS: new code, RHS: old code (i had pushed the code before screenshotting it, oops)](image.png)

New coverage:<br>
![new coverage result (100%)](image-1.png)

The coverage was improved because certain cases that could happen in file paths (e.g. the "." directory, empty path) were not tested for.
By added additional tests that use such cases, the coverage improved.

The test was also faulty on windows (i guess linux was assumed), so i added support for that in the test. (It now passes on Windows 10 too)

### Overall

<Provide a screenshot of the old coverage results by running an existing tool (the same as you already showed above)>

<Provide a screenshot of the new coverage results by running the existing tool using all test modifications made by the group>

## Statement of individual contributions

<Write what each group member did>

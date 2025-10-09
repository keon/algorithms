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

#### Ayman Errahmouni

##### Function 1: simplify_path_v2

[Link the commit](https://github.com/CatalinAnt/algorithms-SEP-95/pull/2/commits/22ee6fa1df4785596c603af61a725c558973eb0b)

Screenshot of branch measurement:<br>
![image](image-7.png)

##### Function 2: insertion_sort

[Link to commit](https://github.com/CatalinAnt/algorithms-SEP-95/pull/2/commits/5dae7f28036f89b7f6ff673639a922dd714aff3e)

Screenshot of branch measurement:<br>
![alt text](image-12.png)

#### Catalin Antonescu

##### Function 1: strong_password
 
Link to commit:
[https://github.com/CatalinAnt/algorithms-SEP-95/commit/eaad6d32ecd73bb8fde876a4d4852cb522aea6f8](https://github.com/CatalinAnt/algorithms-SEP-95/commit/2b0b9187c1c040e4476b1ca14f2c2249273566b7)

Screenshot of branch measurement:
![image](https://github.com/CatalinAnt/algorithms-SEP-95/assets/113595149/e718a47f-5ea0-412c-b250-25a193412164)

##### Function 2: rotate_image

Link to commit:(same as for the first one)
[https://github.com/CatalinAnt/algorithms-SEP-95/commit/eaad6d32ecd73bb8fde876a4d4852cb522aea6f8](https://github.com/CatalinAnt/algorithms-SEP-95/commit/2b0b9187c1c040e4476b1ca14f2c2249273566b7)

Screenshot of branch measurement:
![image](https://github.com/CatalinAnt/algorithms-SEP-95/assets/113595149/94eec9b6-3dd6-46e3-b087-40892eccc10e)

#### Almuthana Almustafa

##### Function 1: stoogsort in stoog_sort.py

[Link to the commit in the founction files](https://github.com/CatalinAnt/algorithms-SEP-95/commit/57b66879c6ae0f82712c55528f540dfdb3c3ddd3)

result: 

![alt text](result_image-2.png)

##### Function 2: word_break in word_break.py

link to commit in founction:
[Link to the commit in the founction files](https://github.com/CatalinAnt/algorithms-SEP-95/commit/57b66879c6ae0f82712c55528f540dfdb3c3ddd3 )

result:

![alt text](result_image_2.png)

## Coverage improvement

### Individual tests

## Ayman Errahmouni

#### <Test "test_simplify_path">

An enhanced existing test

Old coverage:<br>
![old coverage result (24%)](image-2.png)

Diff (LHS = new code, RHS = old code):<br>
![LHS: new code, RHS: old code](image.png)
![alt text](image-9.png)

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
(Instrumentation)<br>
![alt text](image-8.png)

Old coverage:<br>
![Old coverage result (4%)](image-3.png)

New coverage:<br>
![alt text](image-4.png)

<State the coverage improvement with a number and elaborate on why the coverage is improved>

## Catalin Antonescu

Test 1:

In test_string:

Link to commit:

[https://github.com/CatalinAnt/algorithms-SEP-95/commit/eaad6d32ecd73bb8fde876a4d4852cb522aea6f8](https://github.com/CatalinAnt/algorithms-SEP-95/commit/2b0b9187c1c040e4476b1ca14f2c2249273566b7)

Old coverage:

![image](https://github.com/CatalinAnt/algorithms-SEP-95/assets/113595149/5ea3487d-f024-45e6-a1e7-e6d9d1d953b7)
![image](https://github.com/CatalinAnt/algorithms-SEP-95/assets/113595149/e718a47f-5ea0-412c-b250-25a193412164)

New coverage:

![image](https://github.com/CatalinAnt/algorithms-SEP-95/assets/113595149/1d179cc4-1179-40e2-b344-5e904e899647)
![image](https://github.com/CatalinAnt/algorithms-SEP-95/assets/113595149/c8173a47-bcc9-4b6a-9a91-c70b5a8b002f)

For strong_password there was a 26% coverage improvement with the existing tool and 40% with manual measurement tool.

Test 2:

In test_matrix:

[https://github.com/CatalinAnt/algorithms-SEP-95/commit/eaad6d32ecd73bb8fde876a4d4852cb522aea6f8](https://github.com/CatalinAnt/algorithms-SEP-95/commit/2b0b9187c1c040e4476b1ca14f2c2249273566b7)

Old coverage:

![image](https://github.com/CatalinAnt/algorithms-SEP-95/assets/113595149/94eec9b6-3dd6-46e3-b087-40892eccc10e)
![image](https://github.com/CatalinAnt/algorithms-SEP-95/assets/113595149/a97a2bd6-c69e-4435-a8e2-bbdefc429bd1)


New coverage:

![image](https://github.com/CatalinAnt/algorithms-SEP-95/assets/113595149/7cc337eb-5684-40b3-aedd-dc2b7180b7f3)
![image](https://github.com/CatalinAnt/algorithms-SEP-95/assets/113595149/2143adff-e0aa-4113-858a-0c92ec288d20)
 For rotate_image, thre was a 33% coverage improvement with the existing tool and 25% with manual tool.

## Almuthana Almustafa

### Test 1: stoogsort



link to commit in test files:
[Link to the commit in the test files](https://github.com/CatalinAnt/algorithms-SEP-95/commit/157de36fd4c373b67cd03e3b3713be9ba5cf0d97)

existing tool result before:

![alt text](stoog_sort_image1.png)

existing tool result after:

![alt text](stoog_sort_image2.png)

The coverage increased by 89%, largely attributable to the implementation of new tests.

### Test 2: word_break

[Link to the commit in the test files](https://github.com/CatalinAnt/algorithms-SEP-95/commit/157de36fd4c373b67cd03e3b3713be9ba5cf0d97)

existing tool result before:

![alt text](word_break_image1.png)

existing tool result after:

![alt text](word_break_image2.png)

The coverage improved by 86% due to the creation of new tests.
























#### Abdullah Abdelkhalik


pythagoras

https://github.com/CatalinAnt/algorithms-SEP-95/commit/5651abafebe8ae3a5ea63e74883bb991acf19303

![pythagoras_hits](https://github.com/CatalinAnt/algorithms-SEP-95/assets/114078193/c61bff67-be7e-4bd2-b892-0a0f2dada1f3)




first_unique_char

https://github.com/CatalinAnt/algorithms-SEP-95/commit/c16f26e952322b2c1729778a4141a57103ba7658

![first_unique_char_hits (2)](https://github.com/CatalinAnt/algorithms-SEP-95/assets/114078193/8c1b704e-cadb-4f54-aea7-795005348538)





##  Improvements

test_maths

https://github.com/CatalinAnt/algorithms-SEP-95/commit/60832d9c672efd586848077cc41a52630d34371b

![pythagoras_before](https://github.com/CatalinAnt/algorithms-SEP-95/assets/114078193/cf57112b-1aef-4a10-a41f-bd4b797e2012)

![pythagoras_after](https://github.com/CatalinAnt/algorithms-SEP-95/assets/114078193/1aa45c17-46fc-49d3-944a-03c2276d1be6)

the coverage is improved by 28%, the code only hit one of the five branches and cover only one of the three cases of the pythagoras theory. I added the other two cases, i could have a fourth case where none of the cases is present.

test_strings

https://github.com/CatalinAnt/algorithms-SEP-95/commit/5651abafebe8ae3a5ea63e74883bb991acf19303

![first_unique_char_before](https://github.com/CatalinAnt/algorithms-SEP-95/assets/114078193/9910ec69-73b0-4c87-afc8-abc01f65a423)

![first_unique_char_after](https://github.com/CatalinAnt/algorithms-SEP-95/assets/114078193/10859fac-776c-4a48-8a1c-9531afcbfa9b)

The coverage is improved by 13%, the code only hit three out of five branches and only set up two examples. I added a case where there is no unique letter.













### Overall

<Provide a screenshot of the old coverage results by running an existing tool (the same as you already showed above)>
Old overall coverage:
![image](https://github.com/CatalinAnt/algorithms-SEP-95/assets/113595149/f1cd3fab-b00c-4cd0-89d0-6452e7ed1a63)

<Provide a screenshot of the new coverage results by running the existing tool using all test modifications made by the group>
New overall coverage:
 
![image](https://github.com/CatalinAnt/algorithms-SEP-95/assets/113595149/a53729ff-a4f1-42ce-9fe9-ff0813952658)

Due to the large size of the project, the percentage only went up by one percent.

## Statement of individual contributions

<Write what each group member did>

Abdullah -> increased the coverage for two functions.

Almuthana Almustafa -> Instrumentation was added to two functions, and test cases were created for them to improve coverage.

Cataline -> Instrumentation was added to two functions, and the tests for these functions were enhanced.






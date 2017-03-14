## Q

Need to implement set and get operations.
Be aware that one cell may depend on other cells,
e.g. cells[1, 2] = cells[1, 1] + cell[1, 3] * 2

## A

Could you give more details in the description and an example?

For example, it is not clear how the inputs are given.
How is the spreadsheet represented? A 2d array of cells? Each cell contains a string?

Input:
```
[
  ["100",   "A2*3"],
  ["B2+A1", "200"]
]

```
Output:
```
[
  ["100", "900"],
  ["300", "200"]
]
```
Is it like the above? And what about circular reference? What should the output be?

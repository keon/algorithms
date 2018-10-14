"""Iterable to get every convolution window per loop iteration.

## Example Usage

```
from algorithms.iterables import convolved
# This would also work: from conv import convolved

some_list = [1, 2, 3]
for kernel_hover in convolved(some_list, kernel_size=2, stride=1, padding=2, default_value=42):
    print(kernel_hover)
```

## Result:

```
[42, 42]
[42, 1]
[1, 2]
[2, 3]
[3, 42]
[42, 42]
```

"""

import conv


def convolved(iterable, kernel_size=1, stride=1, padding=0, default_value=None):
    """Iterable to get every convolution window per loop iteration.

    For example:
        `convolved([1, 2, 3, 4], kernel_size=2)` 
            will produce the following result:
            `[[1, 2], [2, 3], [3, 4]]`.
        `convolved([1, 2, 3], kernel_size=2, stride=1, padding=2, default_value=42)` 
            will produce the following result:
            `[[42, 42], [42, 1], [1, 2], [2, 3], [3, 42], [42, 42]]`

    Arguments:
        iterable: An object to iterate on. It should support slice indexing if `padding == 0`.
        kernel_size: The number of items yielded at every iteration.
        stride: The step size between each iteration.
        padding: Padding must be an integer or a string with value `SAME` or `VALID`. If it is an integer, it represents
            how many values we add with `default_value` on the borders. If it is a string, `SAME` means that the
            convolution will add some padding according to the kernel_size, and `VALID` is the same as
            specifying `padding=0`.
        default_value: Default fill value for padding and values outside iteration range.

    For more information, refer to: 
    - https://github.com/guillaume-chevalier/python-conv-lib/blob/master/conv/conv.py
    - https://github.com/guillaume-chevalier/python-conv-lib
    - MIT License, Copyright (c) 2018 Guillaume Chevalier
    """
    return conv.convolved(
        iterable=iterable, 
        kernel_size=kernel_size, 
        stride=stride, 
        padding=padding, 
        default_value=default_value
    )

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
    # Input validation and error messages
    if not hasattr(iterable, '__iter__'):
        raise ValueError(
            "Can't iterate on object.".format(
                iterable))
    if stride < 1:
        raise ValueError(
            "Stride must be of at least one. Got `stride={}`.".format(
                stride))
    if not (padding in ['SAME', 'VALID'] or type(padding) in [int]):
        raise ValueError(
            "Padding must be an integer or a string with value `SAME` or `VALID`.")
    if not isinstance(padding, str):
        if padding < 0:
            raise ValueError(
                "Padding must be of at least zero. Got `padding={}`.".format(
                    padding))
    else:
        if padding == 'SAME':
            padding = kernel_size // 2
        elif padding == 'VALID':
            padding = 0
    if not type(iterable) == list:
        iterable = list(iterable)

    # Add padding to iterable
    if padding > 0:
        pad = [default_value] * padding
        iterable = pad + list(iterable) + pad

    # Fill missing value to the right
    remainder = (kernel_size - len(iterable)) % stride
    extra_pad = [default_value] * remainder
    iterable = iterable + extra_pad

    i = 0
    while True:
        if i > len(iterable) - kernel_size:
            break
        yield iterable[i:i + kernel_size]
        i += stride

def convolved_1d(iterable, kernel_size=1, stride=1, padding=0, default_value=None):
    """1D Iterable to get every convolution window per loop iteration.

    For more information, refer to:
    - https://github.com/guillaume-chevalier/python-conv-lib/blob/master/conv/conv.py
    - https://github.com/guillaume-chevalier/python-conv-lib
    - MIT License, Copyright (c) 2018 Guillaume Chevalier
    """
    return convolved(iterable, kernel_size, stride, padding, default_value)


def convolved_2d(iterable, kernel_size=1, stride=1, padding=0, default_value=None):
    """2D Iterable to get every convolution window per loop iteration.

    For more information, refer to:
    - https://github.com/guillaume-chevalier/python-conv-lib/blob/master/conv/conv.py
    - https://github.com/guillaume-chevalier/python-conv-lib
    - MIT License, Copyright (c) 2018 Guillaume Chevalier
    """
    kernel_size = dimensionize(kernel_size, nd=2)
    stride = dimensionize(stride, nd=2)
    padding = dimensionize(padding, nd=2)

    for row_packet in convolved(iterable, kernel_size[0], stride[0], padding[0], default_value):
        transposed_inner = []
        for col in tuple(row_packet):
            transposed_inner.append(list(
                convolved(col, kernel_size[1], stride[1], padding[1], default_value)
            ))

        if len(transposed_inner) > 0:
            for col_i in range(len(transposed_inner[0])):
                yield tuple(row_j[col_i] for row_j in transposed_inner)


def dimensionize(maybe_a_list, nd=2):
    """Convert integers to a list of integers to fit the number of dimensions if
    the argument is not already a list.

    For example:
    `dimensionize(3, nd=2)`
        will produce the following result:
        `(3, 3)`.
    `dimensionize([3, 1], nd=2)`
        will produce the following result:
        `[3, 1]`.

    For more information, refer to:
    - https://github.com/guillaume-chevalier/python-conv-lib/blob/master/conv/conv.py
    - https://github.com/guillaume-chevalier/python-conv-lib
    - MIT License, Copyright (c) 2018 Guillaume Chevalier
    """
    if not hasattr(maybe_a_list, '__iter__'):
        # Argument is probably an integer so we map it to a list of size `nd`.
        now_a_list = [maybe_a_list] * nd
        return now_a_list
    else:
        # Argument is probably an `nd`-sized list.
        return maybe_a_list

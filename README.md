[![PyPI version](https://badge.fury.io/py/algorithms.svg)](https://badge.fury.io/py/algorithms)
[![Open Source Helpers](https://www.codetriage.com/keon/algorithms/badges/users.svg)](https://www.codetriage.com/keon/algorithms)
[![Build Status](https://travis-ci.org/keon/algorithms.svg?branch=master)](https://travis-ci.org/keon/algorithms)
[![Coverage Status](https://coveralls.io/repos/github/keon/algorithms/badge.svg?branch=master)](https://coveralls.io/github/keon/algorithms?branch=master)

<p align="center"><img src="https://raw.githubusercontent.com/keon/algorithms/master/docs/source/_static/logo/logotype1blue.png"></p>

Pythonic Data Structures and Algorithms
=========================================

Minimal and clean example implementations of data structures and algorithms in Python 3.

## Contributing
Thanks for your interest in contributing! There are many ways to contribute to this project. [Get started here](CONTRIBUTING.md)

## Tests

### Use unittest
For running all tests write down:

    $ python3 -m unittest discover tests

For running some specific tests you can do this as following (Ex: sort):

    $ python3 -m unittest tests.test_sort

### Use pytest
For running all tests write down:

    $ python3 -m pytest tests

## Install
If you want to use the API algorithms in your code, it is as simple as:

    $ pip3 install algorithms

You can test by creating a python file: (Ex: use `merge_sort` in `sort`)

```python3
from algorithms.sort import merge_sort

if __name__ == "__main__":
    my_list = [1, 8, 3, 5, 6]
    my_list = merge_sort(my_list)
    print(my_list)
```

## Uninstall
If you want to uninstall algorithms, it is as simple as:

    $ pip3 uninstall -y algorithms

## List of Implementations
<!--fnc_list-->
<!--/fnc_list-->
## Contributors

Thanks to [all the contributors](https://github.com/keon/algorithms/graphs/contributors)
who helped in building the repo.

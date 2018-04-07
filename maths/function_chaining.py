"""
Recently, I came across a new technique called function chaining.
I was surprised that there existed such a technique. So, I am just
going to share it with everyone. (See, If you can come up with a
solution.....I counldn't without knowing the basics.)

Create a function add that adds numbers together when
called in succession. So add(1) should return 1,
add(1)(2) should return 1+2, ...
"""


# Some explanation
"""
If you want to define a function to be called
multiple times, first you need to return a callable
object each time (for example a function) otherwise
you have to create your own object by defining
a __call__ attribute, in order for it to be callable.
"""
class Add(int):
    def __call__(self, v):
        return Add(self + v) # return instance with the updated value

def add(num):
    return Add(num)


# A more compact way of solving the above:
class add(int):
    def __call__(self,n):
        return add(self+n)

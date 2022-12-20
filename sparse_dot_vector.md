

# Storing Sparse Vectors and Calculating Dot Product

When dealing with large sparse vectors, which contain a lot of zeros and doubles, it can be helpful to use a data structure to store them. In this example, we will go over a method that can be used to store such vectors and calculate their dot product. 

## Vector to Index/Value List

The first step is to create a list which contains the index and values of the vector. To do this, we can use a list comprehension to loop through the vector and store the index and the value for each non-zero value in the vector:

```python
def vector_to_index_value_list(vector):
    return [(i, v) for i, v in enumerate(vector) if v != 0.0]
```

## Calculating the Dot Product

Once the vector has been converted to an index/value list, we can calculate the dot product between two vectors. To do this, we use a while loop to traverse through both index/value lists and add the product of their corresponding values to the product variable. Once we reach the end of one of the lists, we can return the product. 

```python
def dot_product(iv_list1, iv_list2):

    product = 0
    p1 = len(iv_list1) - 1
    p2 = len(iv_list2) - 1

    while p1 >= 0 and p2 >= 0:
        i1, v1 = iv_list1[p1]
        i2, v2 = iv_list2[p2]

        if i1 < i2:
            p1 -= 1
        elif i2 < i1:
            p2 -= 1
        else:
            product += v1 * v2
            p1 -= 1
            p2 -= 1

    return product
```

## Testing the Code

To test this code, we can create a test to check that the dot product of two simple vectors is correct, and then time how long it takes to calculate the dot product of two large sparse vectors. 

For the first test, we can create two simple vectors and calculate their dot product:

```python
def __test_simple():
    print(dot_product(vector_to_index_value_list([1., 2., 3.]),
                      vector_to_index_value_list([0., 2., 2.])))
    # 10
```

For the second test, we can create two large sparse vectors and time how long it takes for the dot product to be calculated:

```python
def __test_time():
    vector_length = 1024
    vector_count = 1024
    nozero_counut = 10

    def random_vector():
        import random
        vector = [0 for _ in range(vector_length)]
        for i in random.sample(range(vector_length), nozero_counut):
            vector[i] = random.random()
        return vector

    vectors = [random_vector() for _ in range(vector_count)]
    iv_lists = [vector_to_index_value_list(vector) for vector in vectors]

    import time

    time_start = time.time()
    for i in range(vector_count):
        for j in range(i):
            dot_product(iv_lists[i], iv_lists[j])
    time_end = time.time()

    print(time_end - time_start, 'seconds')
```

## Conclusion

In this example, we went over a method for storing sparse vectors and calculating their dot product. We tested our code by creating two simple vectors and timing how long it took to calculate the dot product of two large sparse vectors.
# Dangerous Default Arguments

Found **7** dangerous default arguments.

These use mutable defaults (dict, list, set) that are shared across function calls.

## Issues Found

### `backtrack/array_sum_combinations.py`

#### Line 41: `backtrack` parameter `res`

**Current:**
```python
def backtrack(constructed_sofar, res=[])
```

**Suggested Fix:**
```python
def backtrack(..., res: Optional[list] = None):
    res = res or []
```

#### Line 41: `backtrack` parameter `constructed_sofar`

**Current:**
```python
def backtrack(constructed_sofar=[], res)
```

**Suggested Fix:**
```python
def backtrack(..., constructed_sofar: Optional[list] = None):
    constructed_sofar = constructed_sofar or []
```

### `graph/find_path.py`

#### Line 6: `find_path` parameter `path`

**Current:**
```python
def find_path(graph, start, end, path=[])
```

**Suggested Fix:**
```python
def find_path(..., path: Optional[list] = None):
    path = path or []
```

#### Line 22: `find_all_path` parameter `path`

**Current:**
```python
def find_all_path(graph, start, end, path=[])
```

**Suggested Fix:**
```python
def find_all_path(..., path: Optional[list] = None):
    path = path or []
```

#### Line 39: `find_shortest_path` parameter `path`

**Current:**
```python
def find_shortest_path(graph, start, end, path=[])
```

**Suggested Fix:**
```python
def find_shortest_path(..., path: Optional[list] = None):
    path = path or []
```

### `graph/graph.py`

#### Line 77: `DirectedGraph.__init__` parameter `load_dict`

**Current:**
```python
def __init__(self, load_dict={})
```

**Suggested Fix:**
```python
def __init__(..., load_dict: Optional[dict] = None):
    load_dict = load_dict or {}
```

### `strings/strip_url_params.py`

#### Line 71: `strip_url_params2` parameter `param_to_strip`

**Current:**
```python
def strip_url_params2(url, param_to_strip=[])
```

**Suggested Fix:**
```python
def strip_url_params2(..., param_to_strip: Optional[list] = None):
    param_to_strip = param_to_strip or []
```


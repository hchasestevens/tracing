# tracing

Utilities for tracing program execution line-by-line.

<img src="demo.gif" width="642">

## Usage

Within code:
```python
from tracing import tracing
with tracing():
  ...  # each line executed will be printed to stdout
```

Within an IPython shell:
```python
In [0]: import tracing

In [1]: %trace enable
```

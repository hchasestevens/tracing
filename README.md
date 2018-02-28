# tracing

[![PyPI version](https://badge.fury.io/py/tracing.svg)](https://badge.fury.io/py/tracing)
![Liberapay receiving](https://img.shields.io/liberapay/receives/hchasestevens.svg)

Utilities for tracing program execution line-by-line.

<img src="demo.gif" width="642">

## What is this good for?

Have you ever been in a situation where you weren't quite sure what a program was doing? Where the program seems to hang, or seems to spend too long between two stages, or is behaving in a way you don't expect it to? `tracing` lets you see in real-time exactly what is being run, without some of the overhead of using a debugger - like having to set breakpoints or manually advance the program's execution.

## Installation

`pip install tracing`

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

## Contacts

* Name: [H. Chase Stevens](http://www.chasestevens.com)
* Twitter: [@hchasestevens](https://twitter.com/hchasestevens)

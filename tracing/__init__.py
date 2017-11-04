from __future__ import print_function

import sys
from fnmatch import fnmatch
from contextlib import contextmanager
from functools import partial

try:
    from IPython.core.magic import register_line_magic
except ImportError:
    register_line_magic = None


@contextmanager
def tracing(pattern=None, out=None):
    """Print executed lines to stdout."""
    _trace = partial(trace_line, pattern)

    if out is None:
        out = sys.stdout

    with redirect_stdout(out):
        sys.settrace(_trace)
        try:
            yield
        finally:
            sys.settrace(None)


def trace_line(pattern, frame, event, arg):
    try:
        if pattern and not fnmatch(frame.f_code.co_filename, pattern):
            return
        print("{0.f_code.co_filename}: {0.f_lineno}".format(frame))
    except Exception:
        pass


@contextmanager
def redirect_stdout(out):
    orig_stdout = sys.stdout
    sys.stdout = out
    try:
        yield
    finally:
        sys.stdout = orig_stdout


if callable(register_line_magic):
    _ORIGINAL_STDOUT = sys.stdout

    @register_line_magic
    def trace(line):
        """Usage: %trace (enable|disable) [file pattern] [output path]"""
        args = line.split()
        enable = args[0] in {'enable', 'on'}

        if not enable:
            sys.settrace(None)
            sys.stdout = _ORIGINAL_STDOUT
            return

        pattern = args[1] if len(args) > 1 else None
        sys.stdout = open(args[2], 'a') if len(args) > 2 else sys.stdout
        sys.settrace(partial(trace_line, pattern))

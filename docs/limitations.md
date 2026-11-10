# Python implementation notes and limitations

## The 40-level gate

CPython places a compile-time limit on statically nested blocks in common versions. Use recursive function frames with live handlers; do not nest 40 textual `try` statements in a single code block.

## Exception constructors

In `raise X()`, `X.__init__()` executes before Python raises the `X` instance. A self-catching constructor must use a guard such as `nested=True`, otherwise creating the inner instance recurses until a `RecursionError`.

## Handler propagation

This does **not** work as a chain:

```python
try:
    raise First()
except First:
    raise Second()
except Second:
    pass
```

The sibling `except Second` will not catch the `Second` raised by the first handler. It must be handled by another surrounding `try` or an explicitly nested handler.

## Thread exceptions

Exceptions raised in worker threads stay in those threads. A parent `except` cannot catch them. For production-grade error collection one would use futures, queues, or explicit result/error containers. Here each worker catches its own work exceptions.

## Zero-call purity

A program cannot enter a user-defined Python function without an initial call, and invoking a constructor for `raise SomeException()` is itself a call. We acknowledge unavoidable bootstrap operations in the spec. The demonstration is a convention, not an interpreter that can alter the language's execution semantics.

## Performance

Exceptions and deep recursion are expensive relative to normal arithmetic. The examples are intentionally wasteful. They are unsuitable for real services, safety-critical software, and high-volume production workloads.
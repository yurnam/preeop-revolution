# EOP · PEOP · REOP · PROEP

> **If it works, throw an exception. If it still works, recurse. If it still works, make it parallel.**

A deliberately ridiculous collection of Python programming paradigms designed to confuse developers, stress debuggers, and transform ordinary arithmetic into an architectural incident.

These are **satirical experimental programming styles**, not production recommendations.

## The four paradigms

| Acronym | Full name | Philosophy |
| --- | --- | --- |
| **EOP** | Exception-Oriented Programming | Exceptions are instructions, not errors. |
| **PEOP** | Parallel Exception-Oriented Programming | Raise and handle independent exceptions concurrently. |
| **REOP** | Recursion-Oriented Programming | Every business operation must recurse before doing useful work. |
| **PROEP** | Parallel Recursion-Oriented Exceptionist Programming | Combine all of the above, and require 40 live exception-handler levels before conventional Python work. |

## Quick start

Requires **Python 3.10+**. No third-party dependencies.

```bash
python examples/eop.py
python examples/peop.py
python examples/reop.py
python examples/proep.py
python -m unittest discover -s tests -v
```

Expected PROEP result:

```text
PROEP result: [42, 200]
```

## Example: ordinary code vs. EOP

**Ordinary Python (disgraceful)**

```python
result = 6 * 7
print(result)
```

**EOP (exceptional)**

```python
try:
    raise Multiply(6, 7)
except Multiply as instruction:
    result = instruction.a * instruction.b
```

## Rules of engagement

1. **Exceptions are the API.** Importing, creating, invoking, and printing are represented by custom exceptions.
2. **Only exception subclasses may be defined using ordinary top-level `class` syntax.**
3. **Ordinary class and function definitions belong inside an exception subclass's `__init__` method.** They must be nested inside a `try`/`except` sequence that raises and catches an instance of that **same exception type**; the inner instance uses a termination flag to prevent infinite recursion.
4. **No ordinary class or function definitions in application-level `except` blocks.** Retrieve the definitions produced by exception constructors instead.
5. **40-level rule:** PROEP business operations require at least 40 simultaneously active exception-handler levels. These are obtained with exception-guided recursive calls, not with 40 statically nested `try` blocks (which CPython may reject).
6. **Recursive execution:** Business-operation entrypoints recurse before doing useful work.
7. **Parallel execution:** Independent tasks may raise exceptions on separate threads or processes. Each worker must catch its own exceptions.
8. **Exception batching:** Sequential lists of exceptions are permitted (one `try`/`except` per iteration).
9. **Bootstrap exception:** Minimal exception-subclass constructors and a single initial call are allowed to bootstrap the whole process; all normal work is gated afterward. This is an explicit compromise, not an invisible claim of formal purity.

Read the detailed [specification](docs/specification.md) and [design limitations](docs/limitations.md).

## Samples

- [`examples/eop.py`](examples/eop.py): imports, object creation, and arithmetic raised as exceptions.
- [`examples/peop.py`](examples/peop.py): independent exceptional workers via `threading`.
- [`examples/reop.py`](examples/reop.py): recursion required before useful work.
- [`examples/proep.py`](examples/proep.py): the full spectacularly inefficient combination.

## PROEPS — the only metric that matters

```text
PROEPS = exceptions raised / useful operations completed
```

Higher is more philosophically pure. Lower is more employable.

## Python caveats

- A `raise` aborts its current `try` block. Sibling `except` clauses **do not** catch exceptions raised inside another handler. Nest handlers or construct a recursive chain.
- Exceptions in different threads **do not propagate to the parent thread**. Worker handlers must capture their own outcomes.
- Building `raise SomeException(...)` first runs that exception's constructor, **before** the actual raise.
- Python does not automatically enforce the satirical source-level rules. These examples demonstrate the convention, not a validated new compiler.
- Threads permit overlapping execution; they do not guarantee simultaneous instructions or CPU-parallel Python bytecode.

## Contributing

PRs that increase exception density while preserving correctness are welcome. Please run tests and disclose any bootstrap loopholes.

## License

MIT. See [LICENSE](LICENSE).

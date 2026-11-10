# Satirical language specification, version 1.0

These rules describe an intentionally inconvenient Python coding discipline, not a new Python runtime.

## EOP — Exception-Oriented Programming

- **EOP-001:** Every business operation is initiated by a custom exception using `raise`.
- **EOP-002:** Modules are loaded through `ImportModules`; the underlying `__import__` call is made by an authorized handler.
- **EOP-003:** Instances are requested through `CreateObject`; method calls through `InvokeMethod`.
- **EOP-004:** Return and output events may be transported through `ReturnValue` and `PrintOutput`.
- **EOP-005:** Arbitrary direct application calls are considered a violation unless explicitly authorized by the execution gate.
- **EOP-006:** Top-level ordinary class and function definitions are prohibited. Only exception-subclass definitions are exempt.
- **EOP-007:** Ordinary classes, functions, and methods must be defined inside an exception subclass's `__init__`, inside a locally self-catching exception cycle. Constructors may include a sentinel such as `nested=True` to prevent infinite recursion.
- **EOP-008:** Ordinary `class` and `def` declarations directly inside application `except` handlers are prohibited.
- **EOP-009:** Exception subclasses are infrastructure and may contain the special constructors required to construct definitions and carry metadata.
- **EOP-010:** Exception lists may be processed sequentially with `for ex in exceptions: try: raise ex; except ...: ...`. The `except` must belong to the `try` within the loop (a sibling `except` cannot attach to `for`).

## PEOP — Parallel Exception-Oriented Programming

- **PEOP-001:** Independent operations are encouraged to execute on separate threads/processes.
- **PEOP-002:** Each worker catches exceptions locally; parent-thread `except` cannot intercept an exception raised by another thread.
- **PEOP-003:** Parallel does not imply literally simultaneous exception raising.
- **PEOP-004:** Synchronization and results must be coordinated explicitly.

## REOP — Recursion-Oriented Programming

- **REOP-001:** Business entrypoints recursively call themselves before useful work.
- **REOP-002:** Iterative loops are prohibited for business control flow; exception batching is an explicit exception.
- **REOP-003:** Recursion is bounded by a mandatory base case.
- **REOP-004:** Tail-call optimization is philosophically discouraged.

## PROEP — Parallel Recursion-Oriented Exceptionist Programming

- **PROEP-001:** All prior rules apply.
- **PROEP-002:** At least 40 **live nested exception-handler levels** are required for ordinary business operations. Sequentially catching 40 exceptions is not the same as maintaining 40 active handler frames.
- **PROEP-003:** Recursive calls from a live exception handler may build the 40-level chain. Structural recursion used to enter the gate is an explicit bootstrap allowance.
- **PROEP-004:** At level 40, actual imports, object instantiation, method invocation, arithmetic, and printing must still originate from the appropriate custom exception.
- **PROEP-005:** A single initial entrypoint call is permitted for bootstrap; it should itself be obtained via a self-catching definition exception.

## Terminology

**Exception density:** total raised exceptions per useful business operation.

**Exception depth:** number of simultaneously active exception handlers on the current thread's call stack, not the total number of raised exceptions.

**Self-catching definition exception:** an exception whose `__init__` raises and catches its own type before it defines an ordinary class/function. The nested instance must terminate constructor recursion.

**Compliance:** a playful claim evaluated by code review; no complete automated static analyzer is included.
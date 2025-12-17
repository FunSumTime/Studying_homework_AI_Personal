# Week 5 – Arrays vs Linked Lists

## Arrays

- Stored in **contiguous memory**, meaning elements are placed next to each other in memory.
- **Random access** is fast: accessing an element by index is `O(1)`.
- Inserting at the **end** of an array is usually `O(1)` (amortized).
- Inserting or removing an element in the **middle** costs `O(n)` because elements must be shifted.
- Indexing example:

  List: ([1,2,3,4]) Index: ([0,1,2,3])

---

## Linked Lists

- Made up of **nodes**, where each node:
- Holds data
- Has a pointer (reference) to the next node
- Nodes are **not contiguous in memory** — they can be anywhere unless explicitly pooled.
- No random access:
- To find an element, you must traverse node by node → `O(n)`
- Insertions and deletions are **cheap** (`O(1)`) _if you already have the node_.
- Otherwise, you must search first.
- Appending logic:
- Start at the head
- Traverse until `current.next` is `None`
- Create a new node and link it there
- Inserting at the **front** of a linked list is very cheap.

### Example Representation

## Week 5

- In Python, `print()` adds a newline by default.
- The `end` parameter controls what gets printed after the value.
- `end=""` prevents a new line.
- Useful for printing linked lists or progress output.

## References vs Memory (Critical Concept)

- Variables are references (labels), not containers.
- Assignment (`=`) rebinds a reference.
- Mutation changes the object in memory.
- Data structures are modified by mutating fields, not reassigning variables.

## Python Object Semantics

- Python uses references, not raw pointers.
- References allow mutation through object interfaces.
- Assignment rebinds references; it does not modify memory.
- Encapsulation prevents unsafe memory manipulation.
- Python trades low-level control for safety and consistency.

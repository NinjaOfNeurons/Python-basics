#  Async Programming in Python (asyncio)

This README contains my learning notes on **asynchronous programming in Python** using `asyncio`.  
The goal is to understand how the **event loop**, coroutines, and tasks work together to run code efficiently.

---

##  What does async actually mean?

Async does **not** mean parallel execution.

Async means:
> When one task is waiting (I/O, sleep, lock), the event loop runs another task instead of blocking.

This helps in better **time utilization** and improves performance for I/O-bound work.

---

##  Event Loop (Core of asyncio)

The **event loop** is the central controller of async programs.

### What the event loop does
- Executes coroutines
- Schedules and manages tasks
- Switches between tasks when they are waiting

### Key Points
- `await` activates a coroutine and gives control back to the event loop
- A coroutine **will not run automatically**
- The event loop must be explicitly started

### Running the main coroutine
```python
asyncio.run(main())
````

Without `asyncio.run()`, the coroutine will **never execute**.

---

## Coroutines

* Defined using `async def`
* Execution pauses at `await`
* While paused, the event loop can run other coroutines

In simple words:

> Coroutines cooperate with the event loop to avoid blocking.

---

## Tasks

### `asyncio.create_task()`

* Wraps a coroutine into a **Task**
* Schedules it immediately on the event loop
* Multiple tasks can run **concurrently**

### Key Insight

If tasks were run sequentially, the total time might be high.
With tasks, when one task is waiting, the event loop runs another one.

Overall execution time feels much faster (waiting time is reused).

---

##  TaskGroup (Python 3.11+)

```python
async with asyncio.TaskGroup() as tg:
    tg.create_task(task1())
    tg.create_task(task2())
```

### Key Takeaways

* All tasks inside the block run **concurrently**
* If **any task fails**, all remaining tasks are **automatically cancelled**
* Provides clean and safe **error handling**

 Recommended approach for structured concurrency.

---

##  `asyncio.gather()`

```python
await asyncio.gather(coro1(), coro2())
```

### What it does

* Runs multiple coroutines concurrently
* Collects and returns their results

### Limitations

* Error handling is weak
* If one coroutine fails:

  * Other coroutines are **not automatically cancelled**

Small demos ke liye fine, but for production code it can be risky.

---

##  Locks

```python
async with lock:
    # critical section
```

### Why locks are needed

* Protect shared resources
* Ensure only **one task at a time** enters the critical section

Key idea:

> Until the lock is released, no other task can execute that section.

---

## Semaphore

* Similar to a lock, but allows **limited concurrent access**
* Controls how many tasks can run at the same time
* Useful for:

  * API rate limiting
  * Connection pools

---

##  Futures

* Represents a value that will be available **in the future**
* Tasks internally rely on futures
* Rarely used directly in beginner code

---

##  Events

* Used for signaling between tasks
* One task waits until another task sets the event

```python
event = asyncio.Event()
await event.wait()
event.set()
```

---

##  Summary (Mental Model)

* Async ≠ Parallel
* Async = **non-blocking execution**
* Event loop controls everything
* `await` hands control back to the event loop
* Tasks enable concurrency
* TaskGroup provides safe error handling
* Locks and semaphores protect shared state

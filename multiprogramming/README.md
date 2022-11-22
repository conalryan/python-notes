# Multiprogramming

Parallel processing

Three main ways to achieve it
  1. Threading
  2. Multiple Processes
  3. Asynchronous communication

All three supported in standard library.

Computer programs spend a lot of their time doing nothing. This occurs when the CPU is
waiting for the relatively slow disk subsytem, network stack, or other hardware to fetch
data.

Some applications can achieve more throughput by taking advantage of this slcack time by
seemingly doing more than one thing at a time.

With a single-core computer, this doesn't really happen; with a multicore computer, an
application really can be executing different instructions at the same time.

## 1. Threading
  Subdivides a single process into multiple subprocesses, or thresds, each of which
  can be performing a different task. Threading in Python is good for IO-bound applications,
  but does not increase the efficiency of compute-bound applications.

## 2. Multiprocessing
  Forks (spawns) new processes to do multiple tasks. Multiprocessing is good
  for both CPU-bound and IO-bound applications.

## 3. Asynchronous
  Communication uses an event loop to poll multiple I/O channels rather than
  waiting for one to finish. Async communication is good for IO-bound applications.

# Alternatives to Multiprogramming

## asyncio
  Put events (typically I/O events) in a list, or queue, and starting an event loop that processes
  the events one at a time.
  If the granularity fo the event loop is small, this can be as efficient as multiprogramming.
  Useful for improving I/O throughput, such as networking clients and servers, or scouring a file system.
  Like threading (in Python) is will not help with raw computation speed.
  asyncio module in standard library provides the means to write asynchronouse clients and servers.

## twisted
  Large and well-supported third-pary module that provides support for many kinds of asynchronous communication.
  Has prebuilt objects for servers, clients, and protocols, as well as tools for authentication, translation, and many others.
  twistedmaxtrix.com/trac

# Pools
  Provided by multiprocessing
  Both thread and process pools
  Simplifies multiprogramming tasks
  Processes a list (or other iterable) of data and do something with the results.
  Object creates a pool of n processes.
    `.map()`
        Call `.map()` method with a function that will do the work, and an iterable of data.
        Returns a list the same size as the list that was passed in.
        Returned list contains the results returned by the function for each item in the original list.

  For a thread pool, import Pool from multiprocessing.dummy. It works exactly the same, but creates threads.

# Threads
  Like processes (but lighter weight; occupy much less memory, and take less tiem to create, than do processes)
  Process itself is one thread
  Process can create one more additional thread
  Similar to creating new processes with fork()

## Time sharing
    Modern operating systems (OSs) use time-sharing to manage multiple programs which
    appear to the user to be running simultaneously. Assuming a standard machine with only one
    CPU, that simultaneity is only an illusion, since only one program can run at a time, but it is a
    very useful illusion.

## Process
    Each program that is running counts as a process.
    Can create any number of threads
    Similar to a process calling fork() function.
    Process itself is a thread, and could be considered the "main" thread.
    Just as processes can be interrupted at any time, so can threads.

## Processing table
    The OS maintains a process table, listing all current processes.
    Each process will be shown as currently being in either Run state of Sleep state.

## Variable Sharing
    Variables declared before thread starts are shared
    Variables declared after thread starts are local
    Threads communicate via shared variables
    Major difference between ordinary processes and threads is how variables are shared
    Each thread has its own local variables, just as is the case for a process.
    Access to global variables is controlled by locks.

## Debugging Thread Programs
  Harder than non-threaded programs
  Context changes abruptly
  Use pdb.trace
  Set breakpoint programmatically
  Especially difficult with pre-emptive threads
  Tracking down the cause of deadlocks can be very hard
  Child threads will not inherit the PDB process from the main thread. Invoke PDB from within the function
  which is run by the thread, by calling pdb.set_trace() at one or more points within the code
  ```pyrhton
    import pdb
    while True:
        pdb.set_trace() # app will stop here and enter debugger
        k = c.recv(1)
        if k == ’’:
            break
  ```
  Then run program as usual, not through PDB. The program suddenly moves into debugging mode on its own.
  Then setp through using the n or s commands, query the vlaues of variables, etc.
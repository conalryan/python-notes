#!/usr/bin/env python

"""
Threads
    Like processes (but lighter weight; occupy much less memory, and take less tiem to create, than do processes)
    Process itself is one thread
    Process can create one more additional thread
    Similar to creating new processes with fork()

Time sharing
    Modern operating systems (OSs) use time-sharing to manage multiple programs which
    appear to the user to be running simultaneously. Assuming a standard machine with only one
    CPU, that simultaneity is only an illusion, since only one program can run at a time, but it is a
    very useful illusion.

Process
    Each program that is running counts as a process.
    Can create any number of threads
    Similar to a process calling fork() function.
    Process itself is a thread, and could be considered the "main" thread.
    Just as processes can be interrupted at any time, so can threads.

Processing table
    The OS maintains a process table, listing all current processes.
    Each process will be shown as currently being in either Run state of Sleep state.

Variable Sharing
    Variables declared before thread starts are shared
    Variables declared after thread starts are local
    Threads communicate via shared variables
    Major difference between ordinary processes and threads is how variables are shared
    Each thread has its own local variables, just as is the case for a process.
    Access to global variables is controlled by locks.

Debugging Thread Programs
    Harder than non-threaded programs
    Context changes abruptly
    Use pdb.trace
    Set breakpoint programmatically
    Especially difficult with pre-emptive threads
    Tracking down the cause of deadlocks can be very hard
    Child threads will not inherit the PDB process from the main thread. Invoke PDB from within the function
    which is run by the thread, by calling pdb.set_trace() at one or more points within the code
        import pdb
        while True:
            pdb.set_trace() # app will stop here and enter debugger
            k = c.recv(1)
            if k == ’’:
                break
    Then run program as usual, not through PDB. The program suddenly moves into debugging mode on its own.
    Then setp through using the n or s commands, query the vlaues of variables, etc.
"""


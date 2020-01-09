#!/usr/bin/env python

"""
Multiprogramming
    Parallel processing
    Three main ways to achieve it
        Threading
        Multiple Processes
        Asynchronous communication
    All three supported in standard library

    Computer programs spend a lot of their time doing nothing. This occurs when the CPU is
    waiting for the relatively slow disk subsytem, network stack, or other hardware to fetch
    data.

    Some applications can achieve more throughput by taking advantage of this slcack time by
    seemingly doing more than one thing at a time.

    With a single-core computer, this doesn't really happen; with a multicore computer, an
    application really can be executing different instructions at the same time.

    Threading
        Subdivides a single process into multiple subprocesses, or thresds, each of which
        can be performing a different task. Threading in Python is good for IO-bound applications,
        but does not increase the efficiency of compute-bound applications.

    Multiprocessing
        Forks (spawns) new processes to do multiple tasks. Multiprocessing is good
        for both CPU-bound and IO-bound applications.

    Asynchronous
        Communication uses an event loop to poll multiple I/O channels rather than
        waiting for one to finish. Async communication is good for IO-bound applications.

Alternatives to Multiprogramming
    asyncio
        Put events (typically I/O events) in a list, or queue, and starting an event loop that processes
        the events one at a time.
        If the granularity fo the event loop is small, this can be as efficient as multiprogramming.
        Useful for improving I/O throughput, such as networking clients and servers, or scouring a file system.
        Like threading (in Python) is will not help with raw computation speed.
        asyncio module in standard library provides the means to write asynchronouse clients and servers.
    twisted
        Large and well-supported third-pary module that provides support for many kinds of asynchronous communication.
        Has prebuilt objects for servers, clients, and protocols, as well as tools for authentication, translation, and many others.
        twistedmaxtrix.com/trac


"""
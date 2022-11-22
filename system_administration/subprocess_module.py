#!/usr/bin/env python

"""
Subprocess module
    Spawns and manages new processes
    Works on Windows and non-windows systems
    Use this to run local non-Python programs, to log into remote systems, and generally to execute command lines.
    Popen
        Implements a low-level class name Popen
    Convenience methods
        Built on top of Popen(), commonly used since they have a simpler interface than Popen
        You can capture *stdout and stderr separately. If you don't capture them, they will go to the console.
        run()
            proc subprocess.run(cmd, ...)
            Run command with arguments. Wait for command to complete, then return a CompletedProcess instance.
            Python 3.5+
        call()
        check_call()
            subprocess.check_call(cmd, ...)
            Run command with arguments. Wait for command to complete. If the exit code was zero then return,
            otherwise raise CalledProcessError.
            The CalledProcessError object will have the return code in the returncode attribute.
        check_output()
            check_ouput(cmd, ...)
            Run command with arguments and return its output as a byte string. It the eixt code was non-zero it raises a CalledProcessError.
            The CalledProcessError object will have the return code in the returncode attribute and output in output attribute.
    Pass in an iterable containing the command split into individual words, including any file names.
    Use glob.glob() and shlex.split()

CalledProcessError attributes
Attribute       Description
------------------------------
args            The arguments used to launch the process. This may be a list or a string.

returncode      Exit status of the child process. Typically, an exit status of 0 indicates that it ran successfully.
                A negative value -N indicates that the child was terminated by signal N (POSIX only).

stdout          Captured stdout from the child process. A bytes sequence, or a string if run() was called with an encoding or errors. None if stdout was not captured.
                If you ran the process with stderr=subprocess.STDOUT, stdout and stderr will be combined in this attribute, and stderr will be None. stderr

Note
    The following commands are internal to CMD.EXE, and must be preceded by cmd /c or they will not work:
    ASSOC, BREAK, CALL ,CD/CHDIR, CLS, COLOR, COPY, DATE, DEL, DIR, DPATH, ECHO, ENDLOCAL, ERASE, EXIT,
    FOR, FTYPE, GOTO, IF, KEYS, MD/MKDIR, MKLINK (vista and above), MOVE, PATH, PAUSE, POPD, PROMPT, PUSHD,
    REM, REN/RENAME, RD/RMDIR, SET, SETLOCAL, SHIFT, START, TIME, TITLE, TYPE, VER, VERIFY, VOL
"""
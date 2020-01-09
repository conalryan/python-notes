#!/usr/bin/env python

"""
os
    - Interface to work with various operating systems (Windows, mac, linux).
    - File and folder utilities.
    - Date and time utilities.
    - Run external program.
"""
import os, stat, pwd, grp

print('--> dir(os)')
print(dir(os))


"""
exec()
    Execute file, with different configurations of arguments, environment, etc.
    Be careful exec is unsafe and hacky!
"""
print('--> exec()')
program = 'a = 5\nb = 10\nprint("Sum =", a + b)'
exec(program)


"""
system()
    Execute the command (a string) in a subshell.
"""
print('--> system()')
os.system('ls')


"""
kill
    Kill a process with a signal.
"""


print('# ====================================== Directory ===============================================')
"""
getcwd()
    Return unicode string representing current working directory.
"""
print('--> os.getcwd()')
cwd = os.getcwd()
print(cwd)


"""
listdir()
    Return ist of all entries in the directory.
"""
print('--> os.listdir()')
print(os.listdir('data'))


"""
glob
    Search with wildcards
    Python does not expand wildcards automatically like shell.
"""
from glob import glob

print(glob('data/*txt'))


"""
chdir()
    Change to directory of given path.
"""
print('--> os.chdir()')
os.chdir("/Users/")
print(os.getcwd())
# Now change it back
os.chdir(cwd)


"""
makedirs()
    Super-mkdir (like unix mkdir -p no error if file exists make parents as needed)
"""
print('--> os.makdedirs()')
os.makedirs('made_by_os/makedirs')


"""
removedirs(name)
    Super-rmdir; remove leaf directory and all emtpy intermediate ones.
"""
print('--> os.removedirs()')
os.removedirs('made_by_os/makedirs')


"""
mkdir
    Create a directory
"""
print('--> os.mkdir()')
os.mkdir('made_by_os_mkdir')


"""
rmdir()
    Remove a directory.
"""
print('--> os.rmdir()')
os.rmdir('made_by_os_mkdir')


"""
rename()
    Rename a file or directory.
"""
print('--> os.rename()')
os.rename(os.getcwd() + '/data/test.txt', os.getcwd() + '/data/tests.txt')
print(os.listdir(os.getcwd() + '/data/'))
# Change name back
os.rename(os.getcwd() + '/data/tests.txt', os.getcwd() + '/data/test.txt')


"""
renames()
    Super-rename; create directories as necessary.
"""
print('--> os.renames()')
os.renames(os.getcwd() + '/data/test.txt', os.getcwd() + '/data/tests.txt')
print(os.listdir(os.getcwd() + '/data/'))
# Change name back
os.renames(os.getcwd() + '/data/tests.txt', os.getcwd() + '/data/test.txt')


"""
link()
    Create a hard link to a file.
"""
print('--> os.link()')
os.link(os.getcwd() + '/data/test.txt', 'test_link')


"""
unlink()

"""
print('--> os.unlink()')
os.unlink(os.getcwd() + '/test_link')


"""
symlink()
    Create a symbolic link
"""
print('--> symlink()')
os.symlink(os.getcwd() + '/data/test.txt', 'test_link')
os.unlink(os.getcwd() + '/test_link')


"""
readlink()
    Return string representation of symlink target.
"""
print('--> readlink()')
os.symlink(os.getcwd() + '/data/test.txt', 'test_link')
rdlnk = os.readlink(os.getcwd() + '/test_link')
print(rdlnk)
os.unlink(os.getcwd() + '/test_link')


print('# ============================================= Stat =============================================')
"""
stat()
    Perform a stat system call on the given path.
"""
print('--> stat()')
st = os.stat(os.getcwd() + '/data/some_file.txt')
uid = st.st_uid
gid = st.st_gid
print(uid, gid)

user = pwd.getpwuid(uid)[0]
group = grp.getgrgid(gid)[0]
print(user, group)


"""
lstat()
    Like stat(path), but do not follow symbolic links.
"""
print('--> os.lstat()')
print(os.lstat(os.getcwd()))


"""
fstat()
    Return stat result for an open file descriptor.
"""
print('--> os.fstat()')
fd = os.open(os.getcwd() + '/data/test.txt', os.O_RDONLY)
st = os.fstat(fd)
print(st)
os.close(fd)


"""
open()
    Open a file (for low level IO).
"""
print('--> os.open()')
fd = os.open(os.getcwd() + '/data/test.txt', os.O_RDONLY)
print(fd)
os.close(fd)


"""
isatty()
    Return True if file descriptor is an open file descriptor.
"""
print('--> os.isatty()')
fd = os.open(os.getcwd() + '/data', os.O_RDONLY)
print(fd)
print(os.isatty(fd))
os.close(fd)


"""
read()
    Read a file descriptor.
"""
print('--> os.read()')
fd = os.open(os.getcwd() + '/data/test.txt', os.O_RDONLY)
rd = os.read(fd, 100)
print(rd)
os.close(fd)


"""
fchmod()
    Change permissions of file given by file descriptor.
    https://en.wikipedia.org/wiki/Chmod.
"""
print('--> fchmod()')

# Print file permission
# Get the ST_MODE of the tuple returned by os.stat
permission = os.stat(os.getcwd() + '/data/some_file.txt')[stat.ST_MODE]
# Convert to octal and get the last 3 bits
print(oct(permission)[-3:])

fd = os.open(os.getcwd() + '/data/some_file.txt', os.O_RDONLY)

# Set a file read-write-execute by group
os.fchmod(fd, stat.S_IRWXG)
print(oct(os.stat(os.getcwd() + '/data/some_file.txt')[stat.ST_MODE])[-3:])

# Change back to a file read-write-execute by owner
os.fchmod(fd, stat.S_IRWXU)
print(oct(os.stat(os.getcwd() + '/data/some_file.txt')[stat.ST_MODE])[-3:])

# Close opened file.
os.close(fd)


"""
fchown()
    Change owner/group id of the file given by file descriptor.
"""
print('--> fchown()')

st = os.stat(os.getcwd() + '/data/some_file.txt')
uid = st.st_uid
gid = st.st_gid
print(uid, gid)

fd = os.open(os.getcwd() + '/data/some_file.txt', os.O_RDONLY)

os.fchown(fd, uid, gid)

os.close(fd)


"""
lchown()
    Change owner/group of path (don't follow symlink).
"""
print('--> lchown()')
os.lchown(os.getcwd() + '/data/some_file.txt', uid, gid)


print('# ===================================== Environment Variables ====================================')
"""
putenv()
    Change or add an environment variable.
    Warning: Better to use os.environ https://stackoverflow.com/questions/17705419/python-os-environ-os-putenv-usr-bin-env?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
"""
print('--> os.putenv()')
os.putenv('TEST_PUT_ENV', '22')
print(os.getenv('TEST_PUT_ENV'))  # Prints None

"""
getenv()
    Get specified environment variable or None/Default (returns string).
    WARNING: Better to use os.environ https://stackoverflow.com/questions/17705419/python-os-environ-os-putenv-usr-bin-env?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
"""
print('--> os.getenv()')
print(os.getenv('JAVA_HOME'))


"""
unsetenv()
    Delete an environment variable.
    Warning: Better to use os.environ https://stackoverflow.com/questions/17705419/python-os-environ-os-putenv-usr-bin-env?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
"""
os.unsetenv('TEST_PUT_ENV')
print(os.getenv('TEST_PUT_ENV'))


"""
environ
"""
print('--> os.environ')
print(os.environ)

# Set environment variable
# os.environ[<some_var>] = some_value
os.environ['TEST_ENVIRON'] = '22'
print(os.environ)

# Get environment variable
# WARNING: Will throw KeyError is the key doesn't exist
env_var = os.environ['TEST_ENVIRON']
print(env_var)

# Use getter to avoid KeyError and return optional default
env_get_var = os.environ.get('TEST_ENVIRON', "It's not set yet")
print(env_get_var)

# Delete environment variable
# os.environ.pop[<some_var>]
os.environ.pop('TEST_ENVIRON')
print(os.environ)

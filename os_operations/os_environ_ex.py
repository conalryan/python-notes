#!/usr/bin/env python

import sys
import os

# Mac is 'Darwin'
# Linux starts with 'Linux'
if sys.platform == 'win32':
    user_key = 'USERNAME'
else:
    user_key = 'USER'

# Set an environment variable
os.environ['ENV_VAR'] = "42"

# Get an environment variable
env_var = os.environ['ENV_VAR']
print("Env var is",env_var,"user is",os.environ[user_key])

# Avoid key error using os.environ.get(<some_env_var>)
print("count is",os.environ.get('ENV_VAR'),"user is",os.environ.get(user_key))

# Can also use os.getenv
# WARNING getenv just returns the value from os.environ so it's better to use os.environ
user = os.getenv(user_key)
var = os.getenv('ENV_VAR')
print("env var is",var,"user is",user)

# Expand variables in place (handy for translating shell scripts)
cmd = "var is ${} user is ${}".format(var, user_key)
print("cmd:", cmd)
print(os.path.expandvars(cmd))


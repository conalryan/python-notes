#!/usr/bin/env python

"""
requests module
    HTTP the easy way!
    Pythonic front end to urllib, urllib2, httplib, etc
    Makes HTTP transactions simple
    urllib and friends are powerful but complex for non-trivial tasks.
    You have to do a lot of work if you want to provide authentication, proxies, headers, or data, etc.
    requests module is much simpler and included with Anaconda or is readily available from PyPI via pip.

Keyword Parameters for requests methods
Option              Data Type           Description
----------------------------------------------------
allow_redirects     bool                set to True if PUT/POST/DELETE redirect following is allowed

auth                tuple               authentication pair (user/token,password/key)

cert                str or tuple        path to cert file or ('cert', 'key') tuple

cookies             dict or CookieJar   cookies to send with request

data                dict                parameters for a POST or PUT request

files               dict                files for multipart upload

headers             dict                HTTP headers

json                str                 JSON data to send in request body

params              dict                parameters for a GET request

proxies             dict                map protocol to proxy URL

stream              bool                if False, immediately download content

timeout             float or tuple      timeout in seconds or (connect timeout, read timeout) tuple

verify              bool                if True, then verify SSL cert
"""
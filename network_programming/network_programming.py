#!/usr/bin/env python

"""
Network Programming
    Download web pages or file from the Internet
    Consume web services
    Send e-mail using a mail server
    Learn why requests is the best HTTP client

Grabbing a web pages
    import urlopen from urlib.request
    urlopen() similar to open()
    Iterate through (or read from) response
    Use info() method for metadata

    urlib.request
        urlopen()
            Reading data form web pages
            Returns a file-like object
            Iterate over lines of HTML
            read()
                Read all of the contents with read()
                URL is opened in binary mode
                You can download any kind of file which a URL represents - PDF, MP3, JPG, etc by using read()
                Note: When downloading HTML, or other test, a bytes object is returned, use decode() to convert to a string.

    requests module
        Pythonic front end to urllib, urllib2, httplib, etc
        Makes HTTP transactions simple
        urllib and firends are powerful but complex for non-trivial tasks.
        You have to do a lot of work if you want to provide authentication, proxies, headers, or data, etc.
        requests module is much simpler and included with Anaconda or is readily available from PyPI via pip.
"""
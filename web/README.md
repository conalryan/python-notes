# Web Examples

The unsupported Django 2.0 snapshot has been removed. The current runnable API
is in `ai_examples/service.py` with FastAPI/Pydantic and offline HTTP contract
tests. The small Flask example remains a basic route exercise; Flask itself is
still supported. For a full Django app, generate a project using a currently
supported release rather than reusing old settings and migrations.

Never deploy example development servers or embedded development keys. Use
explicit settings, HTTPS, validation, authentication, and current framework
deployment guidance. Browser audio blobs must be decoded before PCM processing.
# Current HTTP and SSH Examples

The current HTTPX client/server example is in `ai_examples`. For an explicitly
chosen asset, run `uv run --extra ai python -m network_programming.download URL DEST`.
It requires HTTPS, refuses overwrites, checks status, bounds downloaded bytes,
and deletes only its own incomplete file on failure. The downloader does not
launch a shell or a desktop application. The URL is a trusted CLI argument;
do not expose this helper as an arbitrary-URL server endpoint without SSRF controls.

Requests and `urllib.request` remain supported. Supplementary Requests examples
can use `uv run --extra legacy`; always set timeouts, close responses, and avoid
network actions on import. The old duplicated PDF downloaders and course-specific
API consumers have been removed in favor of the tested current HTTP boundaries.

The SSH example is opt-in:
`uv run --extra ssh python -m network_programming.paramiko_commands HOST --user USER`.
Use an SSH agent or a key and independently verified `known_hosts`. Unknown host
keys must fail; `AutoAddPolicy` is not a substitute for verifying server identity.
The example only runs a fixed `whoami` command and never interpolates user data
into a remote shell command. No SSH connection runs during imports or tests.
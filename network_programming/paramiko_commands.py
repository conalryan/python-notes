"""Opt-in SSH example: verified host identity and agent/key authentication."""

import argparse


def main() -> None:
    import paramiko

    parser = argparse.ArgumentParser(description="Run a fixed identity query on a trusted SSH host")
    parser.add_argument("host")
    parser.add_argument("--user", required=True)
    arguments = parser.parse_args()
    with paramiko.SSHClient() as ssh:
        # RejectPolicy is the default. Unknown/changed hosts fail instead of being trusted.
        # Provision known_hosts using fingerprints verified through a trusted channel.
        ssh.load_system_host_keys()
        ssh.connect(
            arguments.host,
            username=arguments.user,
            timeout=5,
            banner_timeout=5,
            auth_timeout=5,
            allow_agent=True,
            look_for_keys=True,
        )
        # Keep the command fixed: exec_command uses the remote shell, unlike a local argv.
        stdin, stdout, stderr = ssh.exec_command("whoami", timeout=5)
        stdin.close()
        print(stdout.read().decode("utf-8", errors="replace"))
        error = stderr.read().decode("utf-8", errors="replace")
        if stdout.channel.recv_exit_status() != 0:
            raise RuntimeError(error)


if __name__ == "__main__":
    main()

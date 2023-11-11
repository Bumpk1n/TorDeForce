"""

SSH Fingerprinting, using shodan again
Could definitely implement some sort of web bruteforce SSH lookup. 
Python probably wouldn't be best idea for that, as is relatively too slow - maybe rust?

Limitations:
- If SSH is mapped to a non-default port (e.g. not port 22 or 2222) on the IP, you're screwed essentially, as you'd have to scan every possible port on every possible IP...
- If SSH isn't exposed through Tor in /etc/torrc, makes this useless
- Have to scan the whole internet, although could be made slightly more efficient by targeting specific geographical IP ranges

https://twitter.com/CharlieVedaa/status/541031447986184192
"""

import paramiko
import socks

# Paramiko doesn't natively support socks proxies with SSH :(
# Have to use socks module to manually set proxy.

def get_remote_ssh_fingerprint(hostname):
    sock = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM)
    sock.set_proxy(socks.SOCKS5, '127.0.0.1', 9050)
    sock.connect((hostname, 22))

    t = paramiko.Transport(sock)
    t.start_client()
    key = t.get_remote_server_key()
    fingerprint = ":".join(a + b for a, b in zip(key.get_fingerprint().hex()[::2], key.get_fingerprint().hex()[1::2]))

    return fingerprint

# This module definitely needs work, would be cool to implement some sort of bruteforcing of IP ranges in an efficient manner.
# Maybe store in SQL database to actually become useful instead of just a theoretical project.
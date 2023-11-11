import requests
import mmh3 
import codecs
import os
from modules.ssh import *
from modules.https import *
from modules.regex import *
from modules.favicon import *

root_dir = '/opt/TorDeForce'

def get_tor_session():
    session = requests.session()
    session.proxies = {'http':  'socks5h://127.0.0.1:9050',
                       'https': 'socks5h://127.0.0.1:9050'}
    return session

hostname = open(os.path.join(root_dir, 'server/hostname')).read().strip('\n')

print("[*] Local tor domain found: ", hostname, f'\n')

scan_dir = os.path.join(root_dir, 'client', 'scans', hostname.split('.')[0][0:8])
print("[*] Scan directory created: ", scan_dir, f'\n')

port = ':80'
url = 'http://' + hostname + port

def check_scan(scan_dir):
    if os.path.isdir(scan_dir):
        print('Scan already performed on this domain')
        choice = input('Proceed? (y/n): ')
        if choice.upper() == 'Y':
            pass
        else:
            exit()

    else:
        print(f'Creating scan directory at: {scan_dir}')
        os.mkdir(scan_dir)

session = get_tor_session()

# HTTPS module:
# fingerprint_onion_domain(session, domain)

# SSH Module
# get_remote_ssh_fingerprint(domain)

# Regex module should always be called last - after directory has been created.
print(ip_search(root_dir))
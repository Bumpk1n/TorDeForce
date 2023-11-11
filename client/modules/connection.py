import requests

def ping_connect(hostname):
    response = os.system("ping -c 1 " + hostname)
    if response == 0:
        return '[*] Host is up!'
    else:
        return '[-] Host is not available'

def http_connect(session, hostname):
    try:
        response = session.get('http://' + url)
        return '[*] HTTP Port 80 open'
    except requests.RequestException.ConnectionError:
        return '[-] HTTP Port 80 closed'
    
def https_connect(session, hostname)
    try:
        response = session.get('https://' + url)
        return '[*] HTTPS Port 443 open'
    except requests.RequestException.ConnectionError:
        return '[-] HTTPS Port 443 closed'
    except requests.RequestException.SSLError:
        return '[+] Certificate issues - could indicate self-signed certificate => investigate further!'
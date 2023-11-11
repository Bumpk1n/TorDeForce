import ssl
import socket
import hashlib
import socks
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

def connect_to_tor_domain(onion_url):
    socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 9050)  # Tor's SOCKS proxy address
    with socks.socksocket(socket.AF_INET, socket.SOCK_STREAM) as s:
                with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                    cert = ssock.getpeercert(binary_form=True)
                    return cert


def get_ssl_certificate_onion(onion_url):
    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    context.verify_mode = ssl.CERT_NONE  # Don't verify certificate - I'm guessing a large proportion of Tor sites will be self-signed

    socks.set_default_proxy(socks.SOCKS5, 'localhost', 9050)  # Tor Proxy

    with socks.socksocket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((onion_url, 443)) # Assume HTTPS server is on 443, not 8443 (but could be customised in the future)

        with context.wrap_socket(s, server_hostname=onion_url) as ssock:
            cert = ssock.getpeercert(binary_form=True)
            certificate = x509.load_der_x509_certificate(cert, default_backend()) # Cryptography module is incredible
            fingerprint = certificate.fingerprint(hashes.SHA1())
            
            sha1_fingerprint = hashlib.sha1(fingerprint).hexdigest() # Format to Sha1

            print(f'Visit: https://www.shodan.io/search/report?query=ssl.cert.fingerprint:{sha1_fingerprint}')

#            final_fingerprint = (':'.join([sha1_fingerprint[i:i+2] for i in range(0, len(sha1_fingerprint), 2)])).upper() # This formats it like the firefox certificates, e.g. E0:A1:23:B4:52:5D:69:B5:4D:47:41:59:32:2A:E9:AD:84:9C:10:4A
            return sha1_fingerprint

#print(get_ssl_certificate_onion('www.facebookwkhpilnemxj7asaniu7vnjjbiltxjqhye3mhbshg7kx5tfyd.onion'))



"""

https://software.imdea.org/~juanca/papers/caronte_ccs15.pdf

https://twitter.com/shodanhq/status/730909678520016896?lang=en-GB

"""


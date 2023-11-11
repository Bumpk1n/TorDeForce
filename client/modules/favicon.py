import mmh3 
import codecs
import os

def get_favicon(session, url, scan_dir):
    fav_file = "/favicon.ico"
    req = session.get(url + fav_file)

    favicon = codecs.encode(req.content, 'base64')

    open(os.path.join(scan_dir, 'favicon.ico'), 'wb').write(req.content)


    fav_hash = mmh3.hash(favicon)

    print("Favicon hash: ", fav_hash)

    print("To find if any matches made, visit: https://www.shodan.io/search/report?query=http.favicon.hash:{fav_hash}")

    # In this example, favicon is from StackOverflow: https://www.shodan.io/search/report?query=http.favicon.hash:593396886
    # StackOverflow is located from the favicon.
    # Essentially, if the same favicon is used in the clearnet we can fingerprint servers based off their favicon hash. 

    return True
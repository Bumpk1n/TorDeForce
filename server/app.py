from flask import Flask, send_from_directory, render_template, request, url_for, session, redirect, flash
import os
import re
import requests
from requests.exceptions import ConnectionError
import hashlib

app = Flask(__name__)

# I think Javascript is disabled by most Tor users, so HttpOnly (XSS patching) shouldn't matter too much - but better safe than sorry I guess?
app.config.update(
    SECRET_KEY="SuperSecurePasswordThatCouldntPossiblyBeCrackedInMyLifetimeRight",
    SESSION_COOKIE_HTTPONLY=True,
    REMEMBER_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Strict",
)

app.config['root_path'] = '/opt/TorDeForce/server'
app.config['md5_admin_pwd'] = '9cc2ae8a1ba7a93da39b46fc1019c481' # xkcd told me this password is near uncrackable!

@app.route('/')
def hello_world():
    if not session.get('auth'):
        return redirect(url_for('login'))
    else:
        return redirect(url_for('dashboard'))

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form['password']
        print(password)
        hashed_pwd = hashlib.md5(password.encode()).hexdigest()
        print(hashed_pwd)
        
        if app.config['md5_admin_pwd'] == hashed_pwd:
            session['auth'] = True
            return redirect(url_for('dashboard'))
        
        else:
            flash('Incorrect Password')
            return redirect(url_for('login'))

    else:
        flash('Vault Password')
        return render_template('login.html')
    
@app.route('/dashboard', methods = ['GET', 'POST'])
def dashboard():
    if not session.get('auth'):
        return redirect(url_for('login'))
    else:
        if request.method == 'GET':
            flash('Enter .onion domain to lookup')
            return render_template('dashboard.html')
        else:
            domain = request.form['domain']
            print(domain)
            
            if not re.search('.onion$', domain):
                flash('Forbidden! - Domain must only be in format: "XYZ.onion"')
                return render_template('dashboard.html')
            
            else:
                try:
                    req_proxies = {'http':  'socks5h://127.0.0.1:9050', 'https': 'socks5h://127.0.0.1:9050'}

                    # Admin notes: Have disabled our proxies currently, while the website goes under some development.
                    # Our filters ensure that the server only requests tor domains, so our super secret real IP address can't be leaked - right?

                    req = requests.get('http://' + domain) # proxies=req_proxies) <-- Disabled!

                    flash(f'Domain alive with status code: {req.status_code}')
                    return render_template('dashboard.html')
                
                except ConnectionError:

                    # Proxies have been disabled, the server shouldn't be able to connect to any sites...
                    flash(f'Cannot reach {domain} :(')
                    return render_template('dashboard.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico',mimetype='imagex-icon')

if __name__ == '__main__':
    app.run(debug=True, port=8000)

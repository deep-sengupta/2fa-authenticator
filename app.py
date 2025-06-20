from flask import Flask, render_template, request, redirect, url_for, jsonify
import pyotp
import re
import base64
import json
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key'

DATA_FILE = 'accounts.json'

def load_accounts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_accounts():
    with open(DATA_FILE, 'w') as f:
        json.dump(accounts, f)

accounts = load_accounts()

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        account_name = request.form['account_name'].strip()
        setup_key = request.form.get('setup_key', '').strip()

        if account_name in accounts:
            error = "Account already exists"
            return render_template('index.html', accounts=accounts, error=error)

        if setup_key:
            secret = re.sub(r'\s+', '', setup_key.upper())
            try:
                base64.b32decode(secret, casefold=True)
            except Exception:
                error = "Invalid setup key format"
                return render_template('index.html', accounts=accounts, error=error)
        else:
            secret = pyotp.random_base32()

        accounts[account_name] = secret
        save_accounts()
        return redirect(url_for('index'))

    return render_template('index.html', accounts=accounts, error=error)

@app.route('/get_code/<account>')
def get_code(account):
    if account in accounts:
        code = pyotp.TOTP(accounts[account]).now()
        return jsonify({'code': code})
    return jsonify({'code': 'N/A'})

@app.route('/delete/<account>', methods=['POST'])
def delete(account):
    if account in accounts:
        del accounts[account]
        save_accounts()
    return '', 204

@app.route('/rename/<old_name>', methods=['POST'])
def rename_account(old_name):
    data = request.get_json()
    new_name = data.get('new_name', '').strip()

    if not new_name:
        return jsonify({'success': False, 'error': 'New name is empty'}), 400

    if old_name not in accounts:
        return jsonify({'success': False, 'error': 'Old account not found'}), 404

    if new_name in accounts:
        return jsonify({'success': False, 'error': 'New name already exists'}), 409

    accounts[new_name] = accounts.pop(old_name)
    save_accounts()
    return jsonify({'success': True}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

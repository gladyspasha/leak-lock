from flask import Flask, request, render_template
import hashlib
import requests

app = Flask(__name__)

def request_api_data(query_characters):
    url = "https://api.pwnedpasswords.com/range/" + query_characters
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        password = request.form.get('password')
        count = pwned_api_check(password)
        if count:
            return render_template('result.html', password=password, count=count)
        else:
            return render_template('result.html', password=password, count='NOT found')
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

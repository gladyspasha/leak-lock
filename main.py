import requests  # like having a browser without a browster
import hashlib # contains many of the SHA Hashings
import sys


def request_api_data(query_characters):
    # API below
    url = "https://api.pwnedpasswords.com/range/" + query_characters  # uses Hashing
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res


def get_password_leaks_count(hashes, hash_to_check):
    # splitting password an num times it's been hacked
    hashes = (line.split(':')  for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    # Check Password if it exists in API response
    sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()  # In documentation for more info
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count :
            print(f'{password} was found {count} times... you should probably change your password')
        else:
            print(f'{password} was NOT found. Carry on!!')
        return 'done!'
    

if __name__ == '__main__':  # so it only runs from the main file
    sys.exit(main(sys.argv[1:]))

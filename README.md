# leak-lock
# Password Checker

This Python program checks the security of passwords by comparing them against a database of known compromised passwords using the Have I Been Pwned API.

## How to Use

1. Ensure that you have Python 3 installed on your machine.

2. Clone this repository by running ``` git clone https://github.com/Veolinan/PassPwd.git ```

3. Open the terminal or command prompt and navigate to the project directory.
If you are using windows run  ``` cd PassPwd ```

4. Install the required libraries by running the following command:
```
pip install requests

```

5. Run the `app.py` file using the Python interpreter by running command ``` py app.py ``` on cmd




## How it Works

The program uses the SHA-1 hashing algorithm from the `hashlib` library to securely hash the passwords. It then sends the first five characters of the hashed password to the Have I Been Pwned API to receive a list of hashes that match the queried characters.

The `get_password_leaks_count` function compares the queried hash suffix with the received hashes to determine if the password has been compromised. If a match is found, it returns the count of how many times the password has been leaked. If no match is found, it returns 0.

The `pwned_api_check` function checks if a password exists in the API response by calling the other functions and returns the count of password leaks.

The `main` function accepts command-line arguments (passwords) and calls `pwned_api_check` for each password. It then prints the results accordingly.



The output indicates the number of times each password has been found in compromised databases. If a password has not been found, it displays a "Not found!" message.

## Contributions

Contributions to this project are welcome. If you find any issues or have suggestions for improvement, please feel free to submit a pull request.

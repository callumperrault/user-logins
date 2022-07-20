import hashlib
import yaml

with open('./usernames-passwords.yaml', 'r') as credentials:
    usernames_and_passwords = yaml.safe_load(credentials)


def is_valid_credentials(username, password):
    # Password is hashed here
    hashed_password = hashlib.sha256(password.encode())
    hashed_password = hashed_password.hexdigest()
    
    # Username and password are compared to the ones in the config file, True is returned if they
    # match and false is returned otherwise
    for users in usernames_and_passwords:
        if users['username'] == username:
            if users['password_hash'] == hashed_password:
                return(True)

    return(False)


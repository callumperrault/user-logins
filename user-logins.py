import hashlib

# Dictionary to store usernames and hashed passwords
usernames_and_passwords = {
    "hello" : "b8fd23c8ad9f90270d6ab278db7aae63318cb9b1d58922bf711a38d29251263f"
}

def is_valid_credentials(username, password):
    # Password is hashed here
    hashed_password = hashlib.sha256(password.encode())
    hashed_password = hashed_password.hexdigest()
    
    # Username and password are compared to the ones in the dictionary, True is returned if they
    # match and false is returned otherwise
    for key in usernames_and_passwords:
        if key == username:
            if usernames_and_passwords[key] == hashed_password:
                return(True)

    return(False)



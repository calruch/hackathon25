import os
from werkzeug.security import generate_password_hash

def generate_credentials():
    password = generate_password_hash("password123", method='scrypt', salt_length=16)
    if not os.path.exists("credentials.txt"):
        with open("credentials.txt", "w") as f:
            f.write("admin:" + password + "\n")
            f.write("user:" + password + "\n")

if __name__ == "__main__":
    generate_credentials()
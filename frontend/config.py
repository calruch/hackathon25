import os

class Config:
    # session & credentials
    SECRET_KEY     = os.getenv("SECRET_KEY", "You_Shall_Not_Pass")
    SESSION_KEY    = os.getenv("SESSION_KEY", "Gandalf_the_White")
    CREDENTIALS_FILE = os.getenv("CREDENTIALS_FILE", "credentials.txt")

    # backend service URL for in-painting
    BACKEND_URL    = os.getenv("BACKEND_URL", "http://backend:5000")

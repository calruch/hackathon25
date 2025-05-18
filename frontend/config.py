import os

class Config:
    # session & credentials
    SECRET_KEY     = os.getenv("SECRET_KEY", "You_Shall_Not_Pass")
    SESSION_KEY    = os.getenv("SESSION_KEY", "Gandalf_the_White")
    CREDENTIALS_FILE = os.getenv("CREDENTIALS_FILE", "credentials.txt")

    # backend service URLs
    ADD_CAT_URL    = os.getenv("BACKEND_URL", "http://localhost:5000")
    WEATHER_URL = os.getenv("WEATHER_SERVICE_URL", "http://localhost:5001")


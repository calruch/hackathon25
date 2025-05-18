import os

class Config:
    # Shared secret to authenticate requests
    SECRET_KEY = os.getenv("SECRET_KEY", "Gandalf_the_White")
    # Port to listen on
    PORT = int(os.getenv("PORT", 5001))
    # wttr.in format code
    WEATHER_FORMAT = os.getenv("WEATHER_FORMAT", "3")
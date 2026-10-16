import os
from dotenv import load_dotenv  # 1. Import the library

# 2. Load the variables from the .env file into os.environ
load_dotenv()


def load_config():
    return {
        "APP_ENV": os.getenv("APP_ENV", "development"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL", "INFO"),
    }


print(load_config())

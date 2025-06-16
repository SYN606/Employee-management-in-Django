import os
from dotenv import load_dotenv

load_dotenv()

env = os.getenv("ENV", "development")


if env == "production":
    from .production import *
else:
    from .production import *

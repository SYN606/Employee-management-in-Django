import os
from dotenv import load_dotenv

load_dotenv()

env = os.getenv("ENV", "development")

if env == "production":
    print("Production")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                          "employee.settings.production")
else:
    print("Development")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                          "employee.settings.development")

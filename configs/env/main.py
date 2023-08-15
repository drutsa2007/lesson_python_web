# сначала установите библиотеку
# pip install python-dotenv

import os
from dotenv import load_dotenv

load_dotenv()

MYTOKEN = os.getenv("TOKEN")
MYHOST = os.getenv("HOST")
MYPORT = os.getenv("PORT")

print(MYTOKEN)
print(MYHOST)
print(MYPORT)

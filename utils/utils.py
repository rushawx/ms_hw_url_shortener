import math
import random
import string

from db.engine import session


async def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


async def shorten(url: str) -> str:
    n = int(math.log(len(url), 2))
    chars = []
    for i in range(n):
        chars.append(
            string.ascii_lowercase[random.randint(0, len(string.ascii_lowercase) - 1)]
        )
    print(chars)
    return "".join(chars)

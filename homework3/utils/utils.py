import random
import string


def random_str(length=10):
    return "".join(random.choice(string.ascii_letters) for i in range(length))

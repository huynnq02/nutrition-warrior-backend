from random import choice
from ..models.key import Key

def get_random_api_key():
    keys = Key.objects.all()
    print(keys)
    if not keys:
        raise ValueError("No API keys found in the database.")
    key = choice(keys).key
    print(key)
    return key

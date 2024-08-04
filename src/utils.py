import random
from db import Url
import os

SHORTEN_URL_LENGTH = 10
BASE_URL = "https://numberly.com/"
POSSIBLE_CHARACTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def shorten_url(url):
    shorten_extension = "".join(
        random.choices(POSSIBLE_CHARACTERS, k=SHORTEN_URL_LENGTH)
    )
    short_url = BASE_URL + shorten_extension
    Url.create(long_url=url, short_url=short_url)
    return short_url


def expand_url(shortened_url):
    try:
        url = Url.get(Url.short_url == shortened_url)
        url.redirection_count += 1
        url.save()
        return url.long_url
    except Url.DoesNotExist:
        raise Exception("URL non trouvé.")


def get_url_stats(url):
    try:
        url = Url.get(Url.short_url == url)
        return {
            "long_url": url.long_url,
            "short_url": url.short_url,
            "redirection_count": url.redirection_count,
        }
    except Url.DoesNotExist:
        try:
            url = Url.get(Url.long_url == url)
            return {
                "long_url": url.long_url,
                "short_url": url.short_url,
                "redirection_count": url.redirection_count,
            }
        except Url.DoesNotExist:
            raise Exception("URL non trouvé.")

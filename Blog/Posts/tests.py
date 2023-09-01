from django.test import TestCase

import requests as re

url = 'http://127.0.0.1:8000/api/v1/posts/'


def get(url):
    response = re.get(url=url)
    return response.json()


def post(url, data):
    response = re.post(
        url=url,
        data=data,
    )

    return response.text


data = {
    'title': '6 Some post title',
    'text': 'Some text title',
}

# print(get(url))
print(post(url, data))

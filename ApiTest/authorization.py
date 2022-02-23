import requests
from requests.auth import HTTPBasicAuth


def test_authorization():
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36',
    }
    r = requests.get(url='https://www.httpbin.org/basic-auth/test/test123', headers=headers,
                     auth=HTTPBasicAuth('test', 'test123'), verify=False)
    print(r.json())

import requests
import siteripper
from bs4 import BeautifulSoup


class BsRequest:
    def __init__(self):
        cfg = siteripper.read_config()
        self.session = requests.Session()
        self.session.headers.update(
            {'User-Agent': cfg['general']['user-agent']}
        )

    def get(self, url):
        self.session.auth = siteripper.get_auth_for_url(url)
        cookies = siteripper.get_cookies_for_url(url)
        
        r = self.session.get(url, cookies=cookies)

        return BeautifulSoup(r.text, 'html.parser')

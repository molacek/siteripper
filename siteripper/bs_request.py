import requests
import siteripper
from bs4 import BeautifulSoup


class BsRequest:
    def __init__(self, debug=False):
        cfg = siteripper.read_config()
        self.debug = debug
        self.session = requests.Session()
        self.referer = None
        self.session.headers.update(
            {'User-Agent': cfg['general']['user-agent']}
        )

    def _debug_msg(self, label, value):
        if self.debug:
            print(f"BsRequest: {label}")
            print(value)

    def get(self, url):
        self.session.auth = siteripper.get_auth_for_url(url)
        cookies = siteripper.get_cookies_for_url(url)

        self._debug_msg("Cookies", cookies)
        self._debug_msg("Requesting URL", url)

        self.session.headers.update({"referer": self.referer})
        self._debug_msg("Headers", self.session.headers)
        r = self.session.get(url, cookies=cookies)
        self._debug_msg("Respose status code", r.status_code)
        self.referer = url

        if r.status_code == 200:
            return BeautifulSoup(r.text, 'html.parser')

        if r.status_code == 302:
            return r.headers["Location"]

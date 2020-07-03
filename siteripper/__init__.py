import configparser

from http.cookiejar import MozillaCookieJar
from urllib.parse import urlparse
from xdg import XDG_CONFIG_HOME

class SiteRipper:
    def __init__(self):
        pass

def _strip_http_only(domain):
    if domain.startswith('#HttpOnly_'):
        domain = domain[10:]
    return(domain)
    
def _parse_cookies_file():
    cfg = read_config()
    with open(cfg['general']['cookie-file'], "r") as f:
        ck_file = f.read().strip()
    cookie_lines = [c.split('\t') for c in ck_file.split('\n')]
    return [(_strip_http_only(cl[0]), cl[5], cl[6]) for cl in cookie_lines[4:]]


def get_auth_for_url(url):
    """Returns (username, password) tuple if configuration for host exists.
    Else returns None"""
    cfg = read_config()
    
    o = urlparse(url)
    if o.netloc in cfg["passwords"]:
        [username, password] = cfg["passwords"][o.netloc].split(':')
        return(username, password)
    
    return None


def get_cookies_for_url(url):
    cfg = read_config()
    o = urlparse(url)
    return {name: value for (d, name, value) in _parse_cookies_file() if o.netloc.endswith(d)}
    

def read_config():
    config_filename = XDG_CONFIG_HOME / "siteripper.conf"
    config = configparser.ConfigParser()
    config.read(config_filename)
    return(config)

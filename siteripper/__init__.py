import configparser

from http.cookiejar import MozillaCookieJar
from urllib.parse import urlparse
from xdg import XDG_CONFIG_HOME

class SiteRipper:
    def __init__(self):
        pass

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
    ns_cookiejar = MozillaCookieJar()
    ns_cookiejar.load(cfg['general']['cookie-file'], ignore_discard=True)
    o = urlparse(url)
    return {x.name: x.value for x in ns_cookiejar if o.netloc.endswith(x.domain)}
    

def read_config():
    config_filename = XDG_CONFIG_HOME / "siteripper.conf"
    config = configparser.ConfigParser()
    config.read(config_filename)
    return(config)
#import subprocess
import siteripper
import subprocess

from urllib.parse import urlparse

def get(url, filename=None):
    # Read config
    cfg = siteripper.read_config()

    wget_params = ["wget"]

    # Use cookie file
    if "cookie-file" in cfg["general"]:
        wget_params.extend(["--load-cookies", cfg["general"]["cookie-file"]])

    # Use custom filename
    if filename is not None:
        wget_params.extend(["-O", filename])

    # Use passwords
    auth = siteripper.get_auth_for_url(url)
    if auth is not None:
        (user, password) = auth
        wget_params.extend(["--user", user, "--password", password])

    wget_params.extend([url])
    
    rc = subprocess.run(wget_params)
    if rc.returncode != 0:
        print(f"Error downloading {url}. Error code: {rc.returncode}")
        return False

    return True
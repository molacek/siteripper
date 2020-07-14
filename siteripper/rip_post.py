import imageservice
import sys

from . import bs_request

def extract_post_message(divs, post_id=None):
    print(post_id)
    if post_id is None:
        return [d for d in divs if d.get("id", "").startswith("post_message_")][0]

    return [d for d in divs if d.get("id", "") == f"post_message_{post_id}"][0]

def get_post_id(url):
    if "#" not in url:
        return None
    return url.split("#")[-1].split("_")[-1][4:]


def rip_post(url):
    print("Downloading", url)
    url = url.strip()
    bs = bs_request.BsRequest()
    post_html = bs.get(url)
    all_divs = post_html.find_all('div')
    post = extract_post_message(all_divs, get_post_id(url))
    all_images = post.find_all('img')
    for l in [i.parent for i in all_images if i.parent.name == 'a']:
        print("Downloading", l["href"])
        imageservice.download(l["href"])


def run():
    rip_post(sys.argv[1])

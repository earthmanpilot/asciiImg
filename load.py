from io import BytesIO
import requests
import numpy as np
from PIL import Image
import logging


def load_image(url):
    res = requests.get(url)
    if res.status_code == 200 and "jpeg" in res.headers["content-type"]:
        img_arr = np.array(Image.open(BytesIO(res.content)))
        return img_arr
    else:
        logging.info(f"Image load fail status code: [{res.status_code}]")
        return None


if __name__ == "__main__":
    i = load_image(
        "https://images.unsplash.com/photo-1611915387288-fd8d2f5f928b?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max"
    )
    print(i)

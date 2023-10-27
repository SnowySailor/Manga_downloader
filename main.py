'''
Main file
'''

from downloader import Downloader

def get_cookies() -> str:
    with open('cookies', 'r') as f:
        return f.read()

products = {
    'nihonjinkokoro': {
        'url': 'https://member.bookwalker.jp/app/03/webstore/cooperation?r=BROWSER_VIEWER/59917bbf-d2d3-4fdf-a58f-7519f75d1017/https%3A%2F%2Fbookwalker.jp%2FholdBooks%2F',
        'height': 1500,
        'width': 1100,
        'cut': (0,0,0,0)
    },
    'insomniacs_v1': {
        'url': 'https://member.bookwalker.jp/app/03/webstore/cooperation?r=BROWSER_VIEWER/5d0dc914-5498-4ed0-8875-ee97cd9b7c3f/https%3A%2F%2Fbookwalker.jp%2FholdBooks%2F',
        'height': 1600,
        'width': 1150,
        'cut': (38,0,37,0)
    },
    'insomniacs_v2': {
        'url': 'https://member.bookwalker.jp/app/03/webstore/cooperation?r=BROWSER_VIEWER/a49d8494-e7dd-4ede-9f49-4f8314c0de42/https%3A%2F%2Fbookwalker.jp%2FholdBooks%2F',
        'height': 1600,
        'width': 1150,
        'cut': (38,0,37,0)
    },
    'insomniacs_v3': {
        'url': 'https://member.bookwalker.jp/app/03/webstore/cooperation?r=BROWSER_VIEWER/12559ddc-9dd6-4a2a-a885-8442ec352aa0/https%3A%2F%2Fbookwalker.jp%2FholdBooks%2F',
        'height': 1600,
        'width': 1150,
        'cut': (38,0,37,0)
    },
    'insomniacs_v4': {
        'url': 'https://member.bookwalker.jp/app/03/webstore/cooperation?r=BROWSER_VIEWER/0f5901ca-619d-4c05-9abd-7bf41c924e1c/https%3A%2F%2Fbookwalker.jp%2FholdBooks%2F',
        'height': 1600,
        'width': 1150,
        'cut': (38,0,37,0)
    },
    'insomniacs_v5': {
        'url': 'https://member.bookwalker.jp/app/03/webstore/cooperation?r=BROWSER_VIEWER/9280567d-f5ad-47f8-98ca-07805790ba16/https%3A%2F%2Fbookwalker.jp%2FholdBooks%2F',
        'height': 1600,
        'width': 1150,
        'cut': (38,0,37,0)
    }
}

name = 'insomniacs_v5'
product = products[name]
width = product['width']
height = product['height']
cut = product['cut']
url = product['url']

settings = {
    # Manga urls, should be the same website
    'manga_url': [url],
    # Your cookies
    'cookies': get_cookies(),
    # Folder names to store the Manga, the same order with manga_url
    'imgdir': [
        f'downloads/{name}_{width}_{height}_{"-".join(map(str, cut))}',
    ],
    # Resolution, (Width, Height), For coma this doesn't matter.
    'res': (width, height),
    # Sleep time for each page (Second), normally no need to change.
    'sleep_time': 1,
    # Time wait for page loading (Second), if your network is good, you can reduce this parameter.
    'loading_wait_time': 20,
    # Cut image, (left, upper, right, lower) in pixel, None means do not cut the image. This often used to cut the edge.
    # Like (0, 0, 0, 3) means cut 3 pixel from bottom of the image.
    # or set dynamic to allow the scrypt to cut_images dynamictly (This work only correct if start_page is None)
    # this removed whitespace on the corners, initialised by the Cover.
    'cut_image': cut,
    # File name prefix, if you want your file name like 'klk_v1_001.jpg', write 'klk_v1' here.
    'file_name_prefix': '',
    # File name digits count, if you want your file name like '001.jpg', write 3 here.
    'number_of_digits': 3,
    # Start page, if you want to download from 3 page, set this to 3, None means from 0
    'start_page': None,
    # End page, if you want to download until 10 page, set this to 10, None means until finished
    'end_page': None,
}

if __name__ == '__main__':
    downloader = Downloader(**settings)
    downloader.download()

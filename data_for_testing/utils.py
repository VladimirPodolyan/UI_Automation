import io
import os
import logging

from PIL import Image


sidebar_page_path = f'file://{os.getcwd()}/data_for_testing/sidebar_page.html'
tabs_page_path = f'file://{os.getcwd()}/data_for_testing/tabs_page.html'

available_tabs = ('London', 'Paris', 'Tokyo')


def set_logging_settings(level=logging.INFO):
    logging.getLogger("urllib3").setLevel(logging.ERROR)
    logging.basicConfig(level=level, format='[%(asctime)s][%(levelname)s][%(filename)s:%(lineno)s] %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    return logging


def resize_image(screenshot_binary, scale=3, img_format='JPEG'):
    img = Image.open(io.BytesIO(screenshot_binary))
    img = img.resize((img.width // scale, img.height // scale), Image.ANTIALIAS)

    result_img_binary = io.BytesIO()
    img.convert('RGB').save(result_img_binary, format=img_format, optimize=True)
    return result_img_binary.getvalue()

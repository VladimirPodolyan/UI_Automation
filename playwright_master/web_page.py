import logging
import os

from playwright_master.web_driver import WebDriver


class WebPage:
    def __init__(self, locator, name=None):
        self.driver = WebDriver.driver
        self.context = WebDriver.context
        self.locator = locator
        self.name = name
        if not name:
            self.name = locator

    def get(self, url, *args, **kwargs):
        """ Get some page and wait until loaded """
        sensitive_url = url.replace(os.getcwd(), '****') if os.getcwd() in url else url
        logging.info(f'Go to url {sensitive_url}')
        self.context.goto(url, *args, **kwargs)
        self.wait_until_opened()
        return self

    def wait_until_opened(self):
        """ Wait until page loaded """
        logging.info(f'Wait until page opened {self.name}')
        self.context.wait_for_selector(self.locator)
        return self

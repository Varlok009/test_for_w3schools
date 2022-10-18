from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
from conftest import logger


class BasePage:
    def __init__(self, browser: webdriver, url: str, timeout=5) -> None:
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self) -> None:
        self.browser.get(self.url)

    def is_element_present(self, how: By, what: str) -> bool:
        try:
            self.browser.find_element(how, what)
            logger.info(f'element {what} found successfully on page {self.url}')
        except NoSuchElementException:
            logger.error(f'element {what} not found on page {self.url}')
            return False
        return True

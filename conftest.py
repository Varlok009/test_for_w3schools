import pytest
import logging
from selenium import webdriver


logging.basicConfig(level=logging.INFO, filename="test_log.log", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler(f"{__name__}.log", mode='w')
formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.info(f'start test {__name__}')


@pytest.fixture(scope="function")
def browser() -> None:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()

import pytest
import selene
from selene.support.shared import browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def set_webdriver():
    browser.config.driver = webdriver.Chrome(ChromeDriverManager().install())
    return browser.config.driver

@pytest.fixture()
def set_browser_size():
    browser.driver.set_window_size (3000, 1080)

    @pytest.fixture()
   def open_browser (set_webdriver,set_browser_size)
browser.open('https://google.com')
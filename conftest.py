import pytest
from selene import browser


@pytest.fixture(scope="function")
def pop_browser():
    browser.config.base_url = 'https://google.com'
    browser.config.window_height = 1000
    browser.config.window_width = 1000
    yield
    browser.quit()

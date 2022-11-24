from selene import have
from selene.support.shared import browser


def test_search(open_browser):
    browser.element('[name=q]').type('selene').press_enter()
    browser.element('[id=search]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))

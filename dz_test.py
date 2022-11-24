from selene import have
from selene.support.shared import browser


def test_search(open_browser):
    browser.element('[name=q]').type('selene').press_enter()
    browser.element('[id=search]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_bad(open_browser):
    browser.element('[name=q]').type('jhnmtnmjhx jmhrth').press_enter()
    browser.element('[id=result-stats]').should(have.text('Результатов: примерно 0'))

from selene import browser, be, have


def test_search(pop_browser):
    browser.open('/')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="res"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_failure(pop_browser):
    browser.open('/')
    browser.element('[name="q"]').should(be.blank).type('pqppppqqaaaa').press_enter()
    browser.element('[id="botstuff"]').should(have.text('не найдено'))
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    # parser.addoption('--browser_name', action='store', default="chrome",
    #                  help="Choose browser: chrome or firefox") # default='chrome'
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: es or fr")


@pytest.fixture(scope="function")
def browser(request):
    # browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    link = f"http://selenium1py.pythonanywhere.com/{user_language}/catalogue/coders-at-work_207/"
    browser = None
    if user_language == "es":
        print(f"\nstart chrome browser for test..\nlanguage:{user_language}")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
        browser.get(link)
    if user_language == "fr":
        print(f"\nstart chrome browser for test..\nlanguage:{user_language}")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
        browser.get(link)
    yield browser
    print("\nquit browser..")
    browser.quit()

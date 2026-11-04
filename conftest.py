import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Language for browser interface, e.g. es, fr, en",
    )


@pytest.fixture(scope="function")
def browser(request):
    # Читаем значение --language из командной строки
    language = request.config.getoption("--language")

    # Настраиваем Chrome с нужным языком
    options = Options()
    options.add_experimental_option(
        "prefs", {"intl.accept_languages": language}
    )
    options.add_argument(f"--lang={language}")

    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
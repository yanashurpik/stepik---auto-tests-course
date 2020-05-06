import pytest
from selenium import webdriver

links = ['https://stepik.org/lesson/236895/step/1',
'https://stepik.org/lesson/236896/step/1',
'https://stepik.org/lesson/236897/step/1',
'https://stepik.org/lesson/236898/step/1',
'https://stepik.org/lesson/236899/step/1',
'https://stepik.org/lesson/236903/step/1',
'https://stepik.org/lesson/236905/step/1']


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('page', links)
def test_web(browser, page):
    browser.implicitly_wait(10)
    import time
    import math
    answer = str(math.log(int(time.time())))


    browser.get(page)
    input1 = browser.find_element_by_css_selector("#ember70")
    input1.send_keys(answer)

    button = browser.find_element_by_css_selector(".submit-submission")
    button.click()


    respons_sel = browser.find_element_by_css_selector(".smart-hints__hint")
    response = respons_sel.text

    assert response == "Correct!", "Result is not correct"





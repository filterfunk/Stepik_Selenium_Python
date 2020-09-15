# Запускать командой pytest -v --tb=line --reruns 1 --browser_name=chrome Rerun_test.py
# где --reruns 1 - количество перезапусков упавшего теста
link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")


def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#magic_link")

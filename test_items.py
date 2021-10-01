import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_btn_add_to_basket(browser):
    browser.get(link)
    btn = browser.find_elements_by_css_selector("button[class*='btn-add-to-basket']")
    # time.sleep(2)
    assert len(btn) > 0, "Кнопка добавления в корзину - отсутствует"

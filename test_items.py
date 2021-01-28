link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
import time



def test_guest_should_see_cart(browser):
    browser.get(link)
    time.sleep(10)
    cart_button = browser.find_element_by_css_selector('[type="submit"]')
    #assert cart_button == True, "Cart is not presented"
    assert cart_button is not None, "Cart link is not presented"


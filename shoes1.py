import bs4, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

# current bugs
# sometimes fails to add shoe to cart, when this happens restart the script

# put url of shoes
url = 'https://m.champssports.com/?uri=product&sku=AQ1248&model=265142'

# personal information
fname = 'Jacob'
lname = 'Woo'
street2 = '1726 Baxley Pine Trace'
zipcode2 = '30324'
city2 = 'Suwanee'
phone2 = '6786221523'
email2 = 'jacobkwoo@gmail.com'
state = 'CA'
creditcardnumber = '4246315228702195'
creditcardmonth = '03'
creditcardyear = '22'
credticardcsv = '843'


cart_url = 'https://m.champssports.com/?uri=cart'
shipping_info_loaded = False
credit_info_loaded = False
shoe_status = False
successful_load = False

browser = webdriver.Firefox(executable_path='/Users/upstar77/Documents/geckodriver/geckodriver')


while successful_load == False:
    print('Loading page...')
    browser.get(url)
    print('Successful!')

    # size
    print('Selecting size...')
    select = Select(browser.find_element_by_id('size'))
    select.select_by_value('10.0')
    print('Successful!')

    # add to cart
    print('Adding to cart...')
    add_to_cart = browser.find_element_by_xpath('//*[@id="pdp_addtocart_button"]')
    add_to_cart.click()
    print('Successful!')

    print('Going to cart...')
    browser.get(cart_url)


    cart_count = browser.find_element_by_xpath('//*[@id="cart-button"]/div[@class="cart_count"]').text

    if cart_count != "0":
        print('Going to checkout...')
        checkout = browser.find_element_by_xpath('//*[@id="cart_checkout_button_bottom"]')
        checkout.click()
        print('Successful!')
        print('Going to billing...')
        successful_load = True


# waits for page to load

try:
    element = WebDriverWait(browser, 300).until(EC.presence_of_element_located((By.XPATH, '//*[@id="billFirstName"]')))
    print('Page loaded')
    shipping_info_loaded = True
except TimeoutException:
    print('Page took too long to load')

if shipping_info_loaded == True:
    time.sleep(1)
    print('Filling out shipping info')
    first_name = browser.find_element_by_xpath('//*[@id="billFirstName"]')
    first_name.send_keys(fname)
    last_name = browser.find_element_by_xpath('//*[@id="billLastName"]')
    last_name.send_keys(lname)
    street = browser.find_element_by_xpath('//*[@id="billAddress1"]')
    street.send_keys(street2)
    zipcode = browser.find_element_by_xpath('//*[@id="billPostalCode"]')
    zipcode.send_keys(zipcode2)
    city = browser.find_element_by_xpath('//*[@id="billCity"]')
    city.send_keys(city2)
    city = browser.find_element_by_xpath('//*[@id="billState"]/option[10]')
    city.click()
    phone = browser.find_element_by_xpath('//*[@id="billHomePhone"]')
    phone.send_keys(phone2)
    email = browser.find_element_by_xpath('//*[@id="billEmailAddress"]')
    email.send_keys(email2)

    print('Successful!')
    print('Skipping delivery options')
    next_step = browser.find_element_by_xpath('//*[@id="billPaneContinue"]')
    next_step.click()
    if browser.current_url == 'http://www.footlocker.com/shoppingcart/?sessionExpired=true':
        successful_load = False
    print('Button clicked')

    try:
        element = WebDriverWait(browser, 300).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="shipMethod3"]')))
        print('Page passed')
        next_step_loaded = True
        print('Successful!')
        print('Loading next step')
        if next_step_loaded == True:
            next_step_2 = browser.find_element_by_xpath('//*[@id="shipMethodPaneContinue"]')
            next_step_2.click()
    except TimeoutException:
        print('Page took too long to load')

try:
    element = WebDriverWait(browser, 300).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="payMethodPanestoredCCCardNumber"]')))
    print('Page loaded')
    credit_info_loaded = True
except TimeoutException:
    print('Page took too long to load')

if credit_info_loaded == True:
    time.sleep(1)
    print('Filling out credit card information')
    credit_card_number = browser.find_element_by_xpath('//*[@id="CardNumber"]')
    credit_card_number.send_keys(creditcardnumber)
    credit_card_number_month = browser.find_element_by_xpath('//*[@id="CardExpireDateMM"]')
    credit_card_number_month.send_keys(creditcardmonth)
    credit_card_number_year = browser.find_element_by_xpath('//*[@id="CardExpireDateYY"]')
    credit_card_number_year.send_keys(creditcardyear)
    time.sleep(1)
    print('Filling out csv')
    credit_card_number_csv = browser.find_element_by_xpath('//*[@id="CardCCV"]')
    credit_card_number_csv.send_keys(credticardcsv)
    credit_card_number_csv.submit()
    print('Successful')
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

chromeOption = webdriver.ChromeOptions()
chromeOption.add_argument('--incognito')
browser = webdriver.Chrome(r'C:\Users\danie\Documents\chromedriver.exe', options=chromeOption)

browser.get("https://www.bestbuy.com/site/happiness-is-a-warm-blanket-charlie-brown-dvd-2011/2095286.p?skuId=2095286")
firstName = "Daniel"
lastName = "Zhou"
address = "11005 Hiskey Lane"
city = "Tustin"
state = "CA"
zipCode = "92782"
email = "danielz117@hotmail.com"
phoneNumber = "714 399 8853"
cardNumber = "4242 4242 4242 4242"
cardSecurity = "424"
expirationMonth = "03"
expirationYear = "2025"



buyButton = False
goToCartButton = False
checkoutButton = False
guestButton = False
contactInfo = False
continuePaymentButton = False
address2 = False
address1148 = False
cardInfo = False

while not buyButton:
    try:
        addButton = browser.find_element_by_class_name("btn-disabled")
        print("No Stock")
        time.sleep(1)
        browser.refresh()
    except:
        addButton = browser.find_element_by_class_name("btn-primary")
        print("Stock Available")
        addButton.click()
        buyButton = True

while not goToCartButton:
    try:
        toCart = browser.find_element_by_class_name("c-button-secondary")
        print("In Cart")
        toCart.click()
        goToCartButton = True
    except:
        time.sleep(1)

while not checkoutButton:
    try:
        time.sleep(1)
        toCheckout = browser.find_element_by_class_name("btn-primary")
        print("Checking Out")
        toCheckout.click()
        checkoutButton = True
    except:
        time.sleep(1)

while not guestButton:
    try:
        time.sleep(1)
        toGuest = browser.find_element_by_class_name("cia-guest-content__continue")
        print("Guest")
        toGuest.click()
        guestButton = True
    except:
        time.sleep(1)

while not contactInfo:
    try:
        time.sleep(3)
        browser.find_element_by_id("consolidatedAddresses.ui_address_2.firstName").send_keys(firstName)
        print("Info Recorded")
        contactInfo = True
        address2 = True

    except: 
        browser.find_element_by_id("consolidatedAddresses.ui_address_1148.firstName").send_keys(firstName)
        print("Info Recorded")
        contactInfo = True
        address1148 = True

if address2:
    browser.find_element_by_id("consolidatedAddresses.ui_address_2.lastName").send_keys(lastName)
    browser.find_element_by_id("consolidatedAddresses.ui_address_2.street").send_keys(address)
    browser.find_element_by_id("consolidatedAddresses.ui_address_2.city").send_keys(city)
    browser.find_element_by_id("consolidatedAddresses.ui_address_2.zipcode").send_keys(zipCode)
    browser.find_element_by_id("user.emailAddress").send_keys(email)
    browser.find_element_by_id("user.phone").send_keys(phoneNumber)
    stateSelect = Select(browser.find_element_by_id("consolidatedAddresses.ui_address_2.state"))

if address1148:
    browser.find_element_by_id("consolidatedAddresses.ui_address_1148.lastName").send_keys(lastName)
    browser.find_element_by_id("consolidatedAddresses.ui_address_1148.street").send_keys(address)
    browser.find_element_by_id("consolidatedAddresses.ui_address_1148.city").send_keys(city)
    browser.find_element_by_id("consolidatedAddresses.ui_address_1148.zipcode").send_keys(zipCode)
    browser.find_element_by_id("user.emailAddress").send_keys(email)
    browser.find_element_by_id("user.phone").send_keys(phoneNumber)
    stateSelect = Select(browser.find_element_by_id("consolidatedAddresses.ui_address_1148.state"))

stateSelect.select_by_visible_text(state)

while not continuePaymentButton:
    try:
        toPayment = browser.find_element_by_class_name("btn-secondary")
        print("Payment")
        toPayment.click()
        continuePaymentButton = True
    except: 
        time.sleep(1)

while not cardInfo:
    try:
        time.sleep(1)
        browser.find_element_by_id("optimized-cc-card-number").send_keys(cardNumber)
        print("Card Number Recorded")
        cardInfo = True
    except:
        time.sleep(1)

monthSelect = Select(browser.find_element_by_name("expiration-month"))
monthSelect.select_by_visible_text(expirationMonth)
yearSelect = Select(browser.find_element_by_name("expiration-year"))
yearSelect.select_by_visible_text(expirationYear)
browser.find_element_by_id("credit-card-cvv").send_keys(cardSecurity)

completeOrder = browser.find_element_by_class_name("btn-primary")
completeOrder.click()



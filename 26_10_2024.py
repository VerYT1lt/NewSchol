# 1 Скачивание файлов
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("https://example.com/download-page")
#
# download_button = driver.find_element_by_id("download-button")
# download_button.click()
#2
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Chrome()
# driver.get("https://example.com/registration")
#
#
# driver.find_element(By.NAME, "username").send_keys("example_user")
# driver.find_element(By.NAME, "email").send_keys("user@example.com")
# driver.find_element(By.NAME, "password").send_keys("SecurePassword123")
#
# driver.find_element(By.NAME, "submit").click()
#3
# from selenium.webdriver.chrome import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
#
# driver = webdriver.Chrome()
# driver.get("https://example.com/product-page")
#
#
# add_to_cart_button = driver.find_element(By.ID, "add-to-cart")
#
#
# ActionChains(driver).move_to_element(add_to_cart_button).click().perform()
#
#
# cart_count = driver.find_element(By.CLASS_NAME, "cart-count").text
# assert cart_count == "1", "Товар не был добавлен в корзину"
#4
# from selenium.webdriver.chrome import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("https://example.com/product-page")
#
#
# add_to_cart_button = driver.find_element(By.ID, "add-to-cart")
#
#
# ActionChains(driver).move_to_element(add_to_cart_button).click().perform()
#
#
# cart_count = driver.find_element(By.CLASS_NAME, "cart-count").text
# assert cart_count == "1", "Товар не был добавлен в корзину"


#5
import time

from selenium.common import NoSuchElementException
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://example.com/infinite-scroll-page")


last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


elements = driver.find_elements(By.CLASS_NAME, "item")
for element in elements:
     print(element.text)
#6

driver.get("https://example.com/page1")
data_page1 = driver.find_element(By.ID, "data").text

driver.get("https://example.com/page2")
data_page2 = driver.find_element(By.ID, "data").text


if data_page1 != data_page2:
    print("Данные отличаются.")
else:
    print("Данные совпадают.")

#7
driver.get("https://example.com")
try:
    logo = driver.find_element(By.CLASS_NAME, "site-logo")
    print("Логотип найден.")
except NoSuchElementException:
    print("Логотип не найден.")
#8
driver.get("https://example.com/alert-page")


driver.find_element(By.ID, "show-alert").click()


alert = driver.switch_to.alert
print("Текст алерта:", alert.text)
alert.accept()
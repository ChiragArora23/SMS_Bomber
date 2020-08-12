from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

brower = webdriver.Chrome(ChromeDriverManager().install())

frequency = 10

mobile_number = ''

for i in range(frequency):
    brower.get("https://www.flipkart.com/account/login?ret=/")
    time.sleep(2)

    number = brower.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div[2]/div/form/div[1]/input')
    number.send_keys(mobile_number)

    forgot = brower.find_element_by_link_text('Forgot?')
    forgot.click()

    time.sleep(5)

brower.quit()



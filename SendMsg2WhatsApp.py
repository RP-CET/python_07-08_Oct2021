#pip install selenium==4.0.0.b4
#download https://msedgedriver.azureedge.net/93.0.961.52/edgedriver_win64.zip
#put msedgedriver.exe in the same path as this Python Script

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge("msedgedriver.exe")  # Optional argument, if not specified will search path.


driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 120)
x_arg = '//div[@class="_3Qnsr"]'
x = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))

# Replace 'Friend's Name' with the name of your friend 
# or the name of a group 
target = '"+65 1234 4321"'
  
driver.get("https://web.whatsapp.com/send?phone=" + target)  
wait = WebDriverWait(driver, 120)

inp_xpath = '//div[@class="_13NKt copyable-text selectable-text"][@dir="ltr"][@data-tab="9"]'
input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))


# Put message to be sent here
msg = "Message sent using Python, test 1!!!"
input_box.send_keys(msg + Keys.ENTER)


time.sleep(1)

# Put message to be sent here
msg2 = "Second message is sent!"
input_box.send_keys(msg2 + Keys.ENTER)

input()
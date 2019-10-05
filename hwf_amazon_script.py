from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

#int driver
driver = webdriver.Chrome()

#open the url
driver.get('https://www.amazon.com/gp/help/customer/display.html')
sleep(1)

search = driver.find_element(By.XPATH, "//div[@class='a-search a-span12']/input[@type='search' and @id='helpsearch']")
search.clear()
search.send_keys('cancel order')

driver.find_element(By.XPATH, "//input[@type='submit' and @aria-labelledby='helpSearchSubmit-announce']").click()

search_new= driver.find_element(By.XPATH,"//div[@class='help-content']/h1")
sleep(3)
#verify
assert 'Cancel Items or Orders' in driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text
driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

driver = webdriver.Chrome()
driver.get("https://surprise.katespade.com/contact-us")
select = Select(driver.find_element(By.ID, "contact-us-topic-dropdown"))
select.select_by_visible_text("Order Status") 
driver.find_element(By.ID, "contact-comment").send_keys("Test comment") 
driver.find_element(By.ID, "contact-order-number").send_keys("Order number") 
driver.find_element(By.ID, "contact-full-name").send_keys("Farhan Dev") 
driver.find_element(By.ID, "contact-email").send_keys("farhan@email.com")
driver.find_element(By.ID, "contact-confirm-email").send_keys("farhan@email.com")
driver.find_element(By.ID, "contact-phone-number").send_keys("(308) 523-2216") 
sleep(10)
# driver.find_element(By.NAME, "submit").click()
driver.quit()

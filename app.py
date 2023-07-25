from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.coachoutlet.com/contact-us")
topic_dropdown = Select(driver.find_element(By.ID, "contact-us-topic-dropdown"))
topic_dropdown.select_by_visible_text("Order Status")
comment_field = driver.find_element(By.ID, "contact-comment")
comment_field.send_keys("This is a test comment.")
name_field = driver.find_element(By.ID, "contact-full-name")
name_field.send_keys("John Doe")
email_field = driver.find_element(By.ID, "contact-email")
email_field.send_keys("johndoe@example.com")
confirm_email_field = driver.find_element(By.ID, "contact-confirm-email")
confirm_email_field.send_keys("johndoe@example.com")
phone_field = driver.find_element(By.ID, "contact-phone-number")
phone_field.send_keys("1234567890")

sleep(10)

# submit_button = driver.find_element(By.CLASS_NAME, "subscribe-contact-us")
# submit_button.click()

driver.quit()

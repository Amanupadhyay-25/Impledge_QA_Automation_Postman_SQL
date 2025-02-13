from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Step 1: Login
driver.get(url)
driver.find_element(By.NAME, "email").send_keys(username)
driver.find_element(By.NAME, "password").send_keys(password + Keys.RETURN)
time.sleep(3)

# Step 2: Navigate to Package Types
driver.find_element(By.LINK_TEXT, "Package Types").click()
time.sleep(2)

# Step 3: Delete the Newly Added Package
driver.find_element(By.XPATH, "//td[contains(text(), 'Aman_Upadhyay')]/following-sibling::td/button[text()='Delete']").click()
time.sleep(2)
driver.switch_to.alert.accept()  # Confirm deletion

# Step 4: Logout
driver.find_element(By.LINK_TEXT, "Logout").click()
driver.quit()

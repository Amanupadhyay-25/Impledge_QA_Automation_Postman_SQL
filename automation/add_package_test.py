from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

# Credentials
url = "https://ecspro-qa.kloudship.com"
username = "kloudship.qa.automation@mailinator.com"
password = "Password1"

# Initialize WebDriver (Make sure you have ChromeDriver installed)
driver = webdriver.Chrome()

# Step 1: Login
driver.get(url)
driver.find_element(By.NAME, "email").send_keys(username)
driver.find_element(By.NAME, "password").send_keys(password + Keys.RETURN)
time.sleep(3)  # Wait for login

# Step 2: Navigate to Package Types
driver.find_element(By.LINK_TEXT, "Package Types").click()
time.sleep(2)

# Step 3: Click Add Manually
driver.find_element(By.ID, "add_package_button").click()
time.sleep(2)

# Step 4: Add Package Details
random_size = random.randint(1, 19)
driver.find_element(By.NAME, "name").send_keys("Aman_Upadhyay")
driver.find_element(By.NAME, "dimensions").send_keys(str(random_size))
driver.find_element(By.ID, "save_button").click()
time.sleep(2)

# Step 5: Logout
driver.find_element(By.LINK_TEXT, "Logout").click()
driver.quit()

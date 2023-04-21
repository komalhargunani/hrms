
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from Config.config import TestData

# Create variables for login credentials.
username = "komal.hargunani"
password = "Komal@123"
# Install the chrome web driver from selenium.
#!apt-get update
#!apt install chromium-chromedriver


driver = webdriver.Chrome(executable_path=TestData.chrome_executable_path)
# Launch the browser and open the github URL in your web driver.
driver.get("https://hrms.synerzip.in/")

# Find the username/email field and send the username to the input field.
uname = driver.find_element(By.XPATH, "//input[@id='txtUsername']")
uname.send_keys(username)

# Find the password input field and send the password to the input field.
pword = driver.find_element(By.XPATH, "//input[@id='txtPassword']")
pword.send_keys(password)

# Click sign in button to login the website.
driver.find_element(By.XPATH, "//a[@id='btn-login']").click()

list = []
listmain = driver.find_elements(By.XPATH, "//strong")
print(len(listmain))
for i in listmain:
    listelement = i.text
    list.append({'listelement': listelement})
print(list)

import webdriver_manager.drivers.chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

serv_obj = Service("/home/excellarate/Documents/chromedriver_selenium/111/chromedriver")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://hrms.synerzip.in/symfony/web/index.php/auth/login")
driver.find_element(By.ID, 'txtUsername').send_keys("Komal.Hargunani")
driver.find_element(By.ID, 'txtPassword').send_keys("Komal@123")
driver.find_element(By.ID, 'btn-login').click()
driver.save_screenshot("./hrmslogin.png")
print(driver.title)

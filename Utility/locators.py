from selenium.webdriver.common.by import By


class LoginPageLocators:
    txt_username = (By.XPATH, "//input[@id='txtUsername']")
    txt_password = (By.XPATH, "//input[@id='txtPassword']")
    btn_login = (By.XPATH, "//a[@id='btn-login']")


class HomePageLocators:
    calendar = (By.XPATH, "//h2[contains(text(),'My Calender')]")
    rewardsAndRecognition = (By.XPATH, "//h2[contains(text(),'Rewards and recognition posts')]")
    mainMenuList = (By.ID, "main-menu")
    listItem = (By.TAG_NAME, "li")
    birthdaylist = "//strong"
    myleavecolumn = "//div[@id='myleave']/fieldset[1]/table[1]/thead[1]/tr[1]/th"
    myleaverows = "//div[@id='myleave']/fieldset[1]/table[1]/tbody[1]/tr"
    todaydate =  "//div[@class='fc-row fc-week ui-widget-content']/div[1]/table[1]/tbody[1]/tr[1]/td[contains(@class, 'fc-today')]"
    randrvideos = "//table[@id='rr_integration']/tbody[3]/tr[1]/td[1]/a"

class MyInfoLocators():
    myinfopagelink = (By.XPATH, "//a[@id='menu_pim_viewMyDetails']")
    editbutton = (By.XPATH, "//input[@value='Edit']")
    firstname = (By.XPATH, "// input[@name = 'personal[txtEmpFirstName]']")
    middlename = (By.XPATH, "//input[@name = 'personal[txtEmpMiddleName]']")
    lastname = (By.XPATH, "//input[@name='personal[txtEmpLastName]']")
    savebtn = (By.XPATH, "//input[@id='btnSave']")
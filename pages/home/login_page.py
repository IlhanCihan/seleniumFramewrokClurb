from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver

class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "Sign in"
    _email_field = "email"
    _password_field = "passwd"
    _login_button = "SubmitLogin"

    # def getLoginLink(self):
    #     return self.driver.find_element(By.LINK_TEXT, self._login_link)
    #
    # def getEmailField(self):
    #     return self.driver.find_element(By.ID, self._email_field)
    #
    # def getPasswordField(self):
    #     return self.driver.find_element(By.ID, self._password_field)
    #
    # def getloginButton(self):
    #     return self.driver.find_element(By.ID, self._login_button)

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="linktext")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="name")


    def login(self, email, password):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

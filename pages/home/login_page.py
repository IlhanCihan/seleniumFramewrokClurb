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


    def login(self, email="", password=""):
        self.clickLoginLink()
        self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("/html//header[@id='header']//nav//a[@title='View my customer account']/span[.='automation test']", locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//?/p[@innertext='There is 1 error']", locatorType="xpath")
        return result

    def clearFields(self):
        emailField =  self.getElement(locator=self._email_field)
        emailField.clear()
        passwordField = self.getElement(locator=self._password_field)
        passwordField.clear()

    # def verifyTitle(self):
    #     if "Automation Practice Website" in self.getTitle():
    #         return True
    #     else:
    #         return False

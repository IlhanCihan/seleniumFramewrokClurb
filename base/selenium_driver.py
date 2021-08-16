from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import unittest
import pytest


class LoginTests(unittest.TestCase):
    baseURL = "http://automationpractice.com/index.php"
    driver = webdriver.Chrome(executable_path="C:\\Users\\ASUS\\Desktop\\Selenium\\drivers\\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(baseURL)
    lp = LoginPage(driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.driver.get(self.baseURL)
        self.lp.login("automationtest12345@gmail.com", "test123")
        result = self.lp.verifyLoginSuccessful()

        assert result == True
        self.driver.quit()

        # LoginLink = driver.find_element(By.LINK_TEXT, "Sign in")
        # LoginLink.click()
        #
        # emailField = driver.find_element(By.ID, "email")
        # emailField.send_keys("automationtest12345@gmail.com")
        #
        # passwordField = driver.find_element(By.ID, "passwd")
        # passwordField.send_keys("test123")
        #
        # loginButton = driver.find_element(By.ID, "SubmitLogin")
        # loginButton.click()

        # !! This is to confirm that we logged in should be diferent if logged in with different account
        # userName = driver.find_element(By.XPATH, "/html//header[@id='header']//nav//a[@title='View my customer account']/span[.='automation test']")
        # if userName is not None:
        #     print("Successfully logged in")
        # else:
        #     print("Failed to login")

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.driver.get(self.baseURL)

        self.lp.login("automationtest12345@gmail.com", "testWithInvalidPassword")
        result = self.lp.verifyLoginFailed()

        assert result == False


# ff = LoginTests()
# ff.test_validLogin()
# ff.test_invalidLogin()
if __name__ == "__main__":
    unittest.main()

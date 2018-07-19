import time
from unittest import TestCase
from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


class TestSignUpPage(TestCase):

    def setUp(self):
        self.driver = Chrome(executable_path="/home/dalton/Downloads/chromedriver")
        self.driver.get("https://secure.retailmenot.com/accounts/register")

    def tearDown(self):
        self.driver.quit()

    def testLogInOptionPresent(self):
        try:
            log_in = self.driver.find_element_by_xpath("//a[@data-qa='log-in-link']")
            log_in.click()
            self.assertEqual(self.driver.current_url, "https://secure.retailmenot.com/accounts/login")
        except NoSuchElementException:
            self.fail("Link with the text 'Log In' not found on page")

    def testEmailPasswordSignupPresent(self):
        try:
            self.driver.find_element_by_xpath("//input[@data-qa='email-input']")
        except NoSuchElementException:
            self.fail("Could not find email element")
        try:
            self.driver.find_element_by_xpath("//input[@data-qa='password-input']")
        except NoSuchElementException:
            self.fail("Could not find password element")
        try:
            self.driver.find_element_by_xpath("//button[@data-qa='submit-button']")
        except NoSuchElementException:
            self.fail("Could not find Sign Up button")

    def testPrivacyPolicyPresent(self):
        try:
            self.driver.find_element_by_xpath("//a[@data-qa='privacy-policy-link']")
        except NoSuchElementException:
            self.fail("Privacy policy link not found.")

    def testSubscribeCheckboxPresent(self):
        try:
            self.driver.find_element_by_id("subscribe")
        except NoSuchElementException:
            self.fail("Could not find the subscribe checkbox")

    def testSubscribeCheckboxSelectedByDefault(self):
        try:
            subscribe = self.driver.find_element_by_id("subscribe")
            self.assertTrue(subscribe.get_attribute("checked"))
        except NoSuchElementException:
            self.fail("Could not find the subscribe checkbox")

    def testContinueWithFacebookPresentOnScreen(self):
        try:
            self.driver.find_element_by_xpath("//button[@data-qa='facebook-sign-up-button']")
        except NoSuchElementException:
            self.fail("Could not find the 'Continue with Facebook' button.")

    def testSignUpButtonDisabledByDefault(self):
        try:
            sign_up = self.driver.find_element_by_xpath("//button[@data-qa='submit-button']")
            self.assertEqual(sign_up.value_of_css_property("background-color"), "rgba(211, 211, 211, 1)")
        except NoSuchElementException:
            self.fail("Could not find Sign Up button")

    def testInvalidEmailThrowsErrors(self):
        try:
            email_input = self.driver.find_element_by_xpath("//input[@data-qa='email-input']")
            email_input.send_keys("invalid email")
            email_input.send_keys(Keys.TAB)
            email_error = self.driver.find_element_by_xpath("//form/div/ul/li")
            self.assertEqual("Please enter a valid email address", email_error.text)
        except NoSuchElementException:
            self.fail("Failed to find either the email_input or email_error")

    def testShortPasswordThrowsErrors(self):
        try:
            password_input = self.driver.find_element_by_xpath("//input[@data-qa='password-input']")
            password_input.send_keys("short")
            password_input.send_keys(Keys.TAB)
            password_errors = self.driver.find_elements_by_xpath("//form/div[2]/ul/li")
            short_error = password_errors[0]
            self.assertEqual("Password must be 8 characters or more", short_error.text.strip())
        except NoSuchElementException:
            self.fail("Failed to find either the password_input or password_errors")

    def testFormNotValidUntilCompletelyFilledOut(self):
        invalid_background_color = "rgba(211, 211, 211, 1)"
        valid_background_color = "rgba(36, 183, 227, 1)"
        try:
            email = self.driver.find_element_by_xpath("//input[@data-qa='email-input']")
            password = self.driver.find_element_by_xpath("//input[@data-qa='password-input']")
            submit = self.driver.find_element_by_xpath("//button[@data-qa='submit-button']")

            email.send_keys("dalton.hill2022@gmail.com")
            self.assertEqual(submit.value_of_css_property("background-color"), invalid_background_color)
            password.send_keys("mostSecurePassword1")
            time.sleep(.5)
            self.assertEqual(submit.value_of_css_property("background-color"), valid_background_color)

        except NoSuchElementException:
            self.fail("Failed to find the email, password, or submit elements.")



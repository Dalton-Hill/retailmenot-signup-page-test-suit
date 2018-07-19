import time
from unittest import TestCase
from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException


# Note: I noticed the fields/links have a "data-qa" html attribute: in practice I'd use this as it seems your developers
# explicitly put this in for tests, however, I wanted to give a demonstration of how I'd accomplish these problems
# without this help

class TestSignUpPage(TestCase):
    register_url = "https://secure.retailmenot.com/accounts/register"

    def setUp(self):
        self.driver = Chrome(executable_path="/home/dalton/Downloads/chromedriver")
        self.driver.get('https://secure.retailmenot.com/accounts/register')

    def tearDown(self):
        self.driver.quit()

    def testLogInOptionPresent(self):
        """
        Ensures "Log In" link is available on the Sign Up page and also that the link takes you to the correct login url
        """
        try:
            log_in = self.driver.find_element_by_xpath("//a[@data-qa='log-in-link']")
            log_in.click()
            self.assertEqual(self.driver.current_url, "https://secure.retailmenot.com/accounts/login")
        except NoSuchElementException:
            self.fail("Link with the text 'Log In' not found on page")

    def testEmailPasswordSignupPresent(self):
        """
        Ensures Sign Up page contains the following fields/Elements: Email, Password and SignUp
        """
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

# test ensure invalid email address displays error message and sign up still disabled (USE MULTIPLE INVALID TYPES)
# test ensure invalid password raises error (USE MULTIPLE)

# test ensure invalid email + valid password sign up still gray
# test ensure valid email + invalid password sign up still gray
# test ensure valid + valid sign up is clickable and returns expected text

# test ensure duplicate email raises error
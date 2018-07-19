import time
from unittest import TestCase
from selenium.webdriver import Chrome


# can we hit the url and receive a page with email+password+signup fields
class TestSignUpPage(TestCase):
    register_url = "https://secure.retailmenot.com/accounts/register"

    def setUp(self):
        self.driver = Chrome(executable_path="/home/dalton/Downloads/chromedriver")

    def tearDown(self):
        self.driver.quit()

    def testLogInOptionsPresent(self):
        self.driver.get('https://secure.retailmenot.com/accounts/register')


    # ensure "email me the best deals on RetailMeNot" is available to select
# ensure a mention to agreed to privacy policy is visible to the user
# ensure user has access to Log In as an alternative option
# ensure the "continue with facebook" button is present on screen

# is the sign up button disabled by default?

# test ensure invalid email address displays error message and sign up still disabled (USE MULTIPLE INVALID TYPES)
# test ensure invalid password raises error (USE MULTIPLE)

# test ensure invalid email + valid password sign up still gray
# test ensure valid email + invalid password sign up still gray
# test ensure valid + valid sign up is clickable and returns expected text

# test ensure duplicate email raises error
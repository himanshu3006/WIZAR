#  Copyright 2017-2018 WiZR
#
#  Licensed under the  License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

# Importing classes for utilising current library

"""
SimpleLoginPage Procedure for WiZR HOME PAGE
https://staging.wizr.com 

"""

from robotpageobjects import Page, robot_alias
from robot.api import logger
import time
from Utility import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class SimpleLoginLogoutPage(Page):
    """
       This POM class used to login to page
       https://staging.wizr.com/home 
    """
    
    # inheritable dictionary mapping human-readable names
    # to Selenium2Library locators. You can then pass in the
    # keys to Selenium2Library actions instead of the locator
    # strings.
    selectors = {
        #The CSS locator to find Partner button
        "Partner button": "css=#app>div>div>div>div>button",
        #Xpath locator to enter email id
        "Enter email": "xpath=//input[@name='email']",
        # Xpath locator to enter password
        "Enter password": "xpath=//input[@name='password']",
        # Xpath locator to click Login button
        "Login button": "xpath=//button[contains(@type,'submit')]",
        # Xpath locator to click profile buuton
        "profile button": "xpath=//*[@id='app']/div/div[1]/div[1]/div[2]/div/div[2]/div/button",
        # Xpath locator to click Logout button
        "Logout": "xpath=/html/body/div[2]/div/div/div/div/div/div/div/div/div"

    }

    def __init__(self, *args, **kwargs):
        Page.__init__(self)
        self.Utility_obj = Utility()

    # Use robot_alias and the "__name__" token to customize
    # where to insert the optional page object name
    # when calling this keyword. Without the "__name__"
    # token this method would map to either "Type In Search Box",
    # or "Type In Search Box Pubmed". Using "__name__" we can call
    # "Type in Pubmed Search Box  foo".

    # robot alias method to login to Wizr
    @robot_alias("simple__login__procedure")
    def simple__login__procedure(self, email, password):
        """
           These functions accepts the email and password and verify argument passed,
           login into https://staging.wizr.com console
           if login sucesfull then it returns next page POM
           and it exit looging error
        """
        #to click partner button
        self.click_button("Partner button")
        self.wait_until_element_is_enabled("Enter email",self.Utility_obj.MEDIUM,"element not found even wait for many seconds")
        time.sleep(self.Utility_obj.SIMPLE)
        # enter email and password
        self.input_text("Enter email", email)
        self.input_text("Enter password", password)
        # click on Login button
        self.click_button("Login button")
        # to display Successfully Login message in Log
        logger.info("Successfully Login")
        # When navigating to another type of page, return
        # the appropriate page object.
        # We always return something from a page object, 
        # even if it's the same page object instance we are
        # currently on.
        return self

    # robot alias method to Logout from the Wizr
    @robot_alias("logout_procedure")
    def logout_procedure(self):
        # to click on profile button
        self.click_element("profile button")
        # wait for small period of time
        time.sleep(self.Utility_obj.SMALL)
        # to click on Logout button
        self.click_element("Logout")
        logger.info("Successfully Logout")
        # We always return something from a page object,
        # even if it's the same page object instance we are
        # currently on.
        return self


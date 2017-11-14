#  Copyright 2017-2018 WiZR
#
#  Licensed under the  License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from robotpageobjects import Page,robot_alias
import re
import time
from robot.api import logger
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, \
    ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from robot.libraries.Screenshot import Screenshot
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.support import *
from Utility import *
from Selenium2Library.keywords.keywordgroup import KeywordGroupMetaClass


class WizrHomePage(Page):
    """
        Wizr page will help us to do all the stuff related to dashboard page
         i.e navigating to different device to different modules
    """
    name = "Wizer"

    selectors = {
        # """
        #     Wizr page selector will help us to find all the  related to dashboard page element
        #       by help of css or xpath
        #     i.e finding each element path and assigned to some locator variables
        # """
                # login selector
        "Partner button": "css=#app>div>div>div>div>button",
        "Enter email": "xpath=//input[@name='email']",
        "Enter password": "xpath=//input[@name='password']",
        "login_withGoogle":"xpath=//button[@class='auth0-lock-social-button auth0-lock-social-big-button']",
        "Login button":"xpath=//button[contains(@type,'submit')]",
        "Login path":"xpath=//span[contains(text(),'Log In')]",
        "Forget Password": "css=.auth0-lock-alternative-link",
        "SecondEmail click": "xpath=//div[contains(@class,'auth0-lock-social-button-text')]/..",
        "Image Logo": "xpath=//img[@alt='Wizr Logo'])",
        "Click NYAccount": "xpath=//*[contains(text(),'Not your account?')]",
        "last_Logined": "xpath=//span[contains(text(),'Last time you logged in with')]",
        "Send Email": "xpath=//span[text()='Send email']",
        "Reset pswd": "xpath=//span[@class='animated fadeInUp']",
                 # logout  selector
        "Qgrid Logout": "xpath=(//*[@type='button'])[3]",
        # "Qgrid Button":"xpath=//p[contains(text(),'Q')]",
        "Specified User":"xpath=//h1[contains(text(),'QATeam5 Q.')]",
        "Logout Wizr": "xpath=//p[text()='Logout']/..",
                 # dashboard page selector
        "Total Camera": "xpath=id('app')/div/div[2]/a[1]/div/div/div/div/h1",
        "Total Location": "xpath=id('app')/div/div[2]/a[3]/div/div/div/div/h1",
        "Total Edgedevice": "xpath=id('app')/div/div[2]/a[2]/div/div/div/div/h1",
        "Total Incident": "xpath=id('app')/div/div[2]/a[4]/div/div/div/div/h1",
        "Camera Table": "xpath=//table/tbody",
        "Camera List": "xpath=//tr/td[2]",
        "Demo": "xpath=//tr[4]/td[3]",
        "Display list": "xpath=//h4",
        "Display Elementlist": "xpath=//h1",
                # login with google selector
        "Wizr1st TimeLogin":"xpath=//div[contains(text(),'Log in with Google')]",
        "google_accountList":"xpath=//ul[@class='sIznTe pggQ5e']/li",
        "welcome_googleMsg":"xpath=//span[@class='description']",
        "okCancel_Permission":"xpath=//div[@class='ok-cancel']/button",
        "ivtree_ID":"xpath=//input[@type='email']",
        "ivtree_password":"xpath=//input[@type='password']",
        "gmail_next":"xpath=//span[contains(text(),'Next')]",
        "google_1stlogout":"xpath=(//button)[2]",
        "google_2ndlogout":"xpath=//p[contains(text(),'Logout')]",
        "user":"xpath=(//h1)[last()]",
                # leftGrid selector
        "left_grid":"xpath=(//button)[1]",
        "select_feature":"xpath=(//hr)[1]/../div[2]/a",
        "select_module":"xpath=//img[@role='presentation']/../../div/div",
                #rightGrid selector
        "right_grid":"xpath=(//button)[2]",
        "rightGrd_list":"xpath=//h1[contains(text(),'Lists')]",
        "rightGrd_feature":"xpath=//h1[contains(text(),'Lists')]/../div/p",

    }


    def __init__(self,*args, **kwargs):
        Page.__init__(self)
        self.Utility_obj = Utility()

    @robot_alias("login__as__User")
    def login__as__User(self, email, password):
        '''
        Login into wizer application with valid email & password
        :param email:qateam5@wizr.com
        :param password:qateam123
        :return: wizrDashboard Page
        '''
        try:
            # click on partner button
            self.click_button("Partner button")
            self.driver.implicitly_wait(10)
            time.sleep(3)
            # enter email & password
            self.input_text("Enter email", email)
            self.input_text("Enter password", password)

            time.sleep(4)
            self.click_button("Login button")
            logger.info('LOGINED successfully', html=True)
        except:
            logger.info('Login failed', html=True)
        # taking screenshot at last of operation
        self.Utility_obj.takescreen()
        logger.info('logined successfully', html=True)
        return self

    def click__name__logoutbutton(self):
        '''
        this function helps to click Q-grid & click logout button
        :return:
        '''
        try:

            # click Q-grid
            time.sleep(15)
            self.click_button("Qgrid Logout")
            time.sleep(15)
            # taking screenshot at last of operation
            self.Utility_obj.takescreen()
            logger.info("Qgrid Logout pop should display", html=True)
            # click logout button inside grid
            self.click_element("Logout Wizr")
            self.driver.implicitly_wait(20)
        except:
            logger.info('logout failed', html=True)
        # taking screenshot at last of operation
        self.Utility_obj.takescreen()
        logger.info("logout from wizr page", html=True)
        return self

    def identify__user(self):
        '''
        this functions help us to know who has logined into application
        :return:
        '''
        try:
            # self.driver.implicitly_wait(40)
            time.sleep(5)
            # self.click_button("Qgrid Button")
            self.click_element("Qgrid Logout")
            self.driver.implicitly_wait(20)
            individual_login = self.get_text("Specified User")
            logger.info('Individual logined as : %s' % individual_login)
            # self.select_window()
            time.sleep(15)
            self.switch_browser('1')
            time.sleep(8)
            title = self.get_window_titles()
            logger.info('Window title is : %s' % title)
        except:
            logger.info('user not identified', html=True)
        # taking screenshot at last of operation
        self.Utility_obj.takescreen()
        logger.info('Individual logined ', html=True)
        return self

    def verify__dashboarDevices(self):
        '''
         Device verifications in DashboardPage
        :return: devices name with total number of devices
        '''
        try:
            # get the total device type camera,Locations,Edge devices,Incidenet Mangement,
            Elementlist = list(self.find_elements("Display list"))
            # get the total number of devices
            TotalDeviceList = list(self.find_elements("Display Elementlist"))

            for index, text in enumerate(Elementlist):
                # element=self.get_text(text)
                self.driver.implicitly_wait(40)
                logger.info('Device Name : %s, Number of devices : %s ' % (
                    self.get_text(text), self.get_text(TotalDeviceList[index])))
        except:
            logger.info('dashboard device not listed', html=True)
        # taking screenshot at last of operation

        self.Utility_obj.takescreen()

        logger.info('grid device verified', html=True)
        return self

    def get__leftGrid__list(self):
        '''
        this functions help us to list out the element present in leftGrid
        :return:
        '''
        try:
            time.sleep(10)
            self.click_element("left_grid")
            time.sleep(5)
            gridList=list(self.find_elements("select_feature"))
            #print all left grid list module
            for index, text in enumerate(gridList):
                functionName=self.get_text(text)
                logger.info('Module name : %s'%functionName)
            time.sleep(5)

        except NoSuchElementException as e:
            raise e

        self.Utility_obj.takescreen()
        logger.info('Display selected grid device ', html=True)
        return self

    def click__from__leftGrid(self, ModuleName):
        '''
        this functions help us to select module from left grid list and navigate to respective module
        :param functionName:
        :return:
        '''
        try:
            # get the module type Dashboard,Customers,Incidenet Mangement,
            moduleList = list(self.find_elements("select_feature"))
            logger.info('Argument is : %s' % ModuleName)
            ModuleName = str(ModuleName)
            for index, module in enumerate(moduleList):
                module= str(self.get_text(module))
                # comparision of aruments with list element
                if module == ModuleName:
                    logger.info('Module Name is : %s' % ModuleName)
                    dynamic_xpath = "//div[contains(text()," + "'" + ModuleName + "'" + ")]"
                    self.click_element("%s" % dynamic_xpath)
                    logger.info("Searched module %s clicked" %module)
                    break
                else:
                    logger.info("%s module not searched" %module)


        except StaleElementReferenceException as e:
            raise e

        self.Utility_obj.takescreen()
        logger.info('Selected module page Displayed', html=True)
        return self

    def click__particularDevice(self, device):
        '''
        click on desired device which is being passed as argument from robot class
        :param device:Total Cameras
        :return: devices page
        '''
        try:
            # get the total device type camera,Locations,Edge devices,Incidenet Mangement,
            Elementlist = list(self.find_elements("Display list"))

            # Used try-block to handle StaleElementReferenceException
            for index, text in enumerate(Elementlist):
                # used regular expression for searching matching device and goto respective devices pages
                if re.search("%s" % device, self.get_text(text)):
                    dynamic_xpath = "//h4[contains(text()," + "'" + device + "'" + ")]"
                    self.click_element("%s" % dynamic_xpath)
                    logger.info("Selected Device  clicked", html=True)
                else:
                    logger.info("Selected Device  not clicked", html=False)
                break

        except (StaleElementReferenceException , NoSuchElementException) as sn :
            raise sn

        self.Utility_obj.takescreen()
        logger.info('Display selected grid device ', html=True)
        return self

    def enter__name__Wrongemail(self, wrongEmail, pwrd):
        '''
            Login into wizer application with another email & password
        :param email:qatea@wizr.com
        :param password:qateam123
        :return: not valid user logined into wizrDashboard Page
        '''
        try:
            # click on partner button
            time.sleep(10)
            self.click_button("Partner button")
            # self.driver.implicitly_wait(40)
            wait = WebDriverWait(self.driver, 30)
            nyAccount=wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Not your account?')]")))
            nyAccount.click()
            # self.click_element("Click NYAccount")
            # # self.driver.implicitly_wait(40)
            time.sleep(5)
            wait = WebDriverWait(self.driver, 50)
            wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='email']")))
                # .sendkeys(wrongEmail)

            logger.info("wrong email")
            self.input_text("Enter email", wrongEmail)
            time.sleep(5)
            wait = WebDriverWait(self.driver, 50)
            wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
            self.input_text("Enter password", pwrd)
            wait = WebDriverWait(self.driver, 30)
            login = wait.until(EC.element_to_be_clickable((
                By.XPATH, "//button[contains(@type,'submit')]")))
            login.click()
            # self.click_button("Login button")
            # self.driver.implicitly_wait(40)

        except (ElementNotVisibleException,ValueError) as ev:
            # raise RuntimeError('not valid user')
            logger.info('not valid user',html=True)
            raise ev
        # taking screenshot at last of operation
        self.Utility_obj.takescreen()
        return self

    def click__name__forgetPswd(self, email, EmailNotification):
        '''
        Login into wizer application with email & forget password
        :param email:
        :param password:
        :return: reset msg send to mentioned email
        '''
        try:
            # click on partner button
            self.click_button("Partner button")
            time.sleep(4)
            self.click_element("Click NYAccount")
            time.sleep(8)
            self.input_text("Enter email", email)
            # enter password
            self.click_element("Forget Password")
            time.sleep(5)
            try:
                emailNot= EmailNotification
                if emailNot in EmailNotification:
                    self.clear_element_text("Enter email")
                    self.input_text("Enter email", EmailNotification)
                    time.sleep(5)
                else:
                    logger.info("can't left blank",html=True)
                time.sleep(4)
                self.click_element("Send Email")
                time.sleep(8)
                # resetMSG = self.get_text("Reset pswd")
                # logger.info('Feedback message of mail :%s'%resetMSG)
                # assert "We've just sent you an email to reset your password." == resetMSG
            except:
                raise RuntimeError('Element is not currently interactable and may not be manipulated')
        except (NoSuchElementException, ValueError) as nv:
            raise nv
        # taking screenshot at last of operation
        self.Utility_obj.takescreen()
        return self

    def click__forgetPswdByInvalidEmail(self, invalidEmailNotification):
        '''
        Login into wizer application with email & forget password
        :param email:
        :param password:
        :return: reset msg send to mentioned email
        '''
        try:
            # click on partner button
            self.click_button("Partner button")
            time.sleep(4)
            self.click_element("Click NYAccount")
            time.sleep(8)
            # enter password
            self.click_element("Forget Password")
            time.sleep(5)
            try:
                emailNot=  invalidEmailNotification
                if emailNot in  invalidEmailNotification:
                    self.input_text("Enter email",  invalidEmailNotification)
                    time.sleep(5)
                else:
                    logger.info("can't left blank",html=True)
                time.sleep(4)
                self.click_element("Send Email")
                time.sleep(8)
                # resetMSG = self.get_text("Reset pswd")
                # logger.info('Feedback message of mail :%s'%resetMSG)
                # assert "We've just sent you an email to reset your password." == resetMSG
            except:
                raise RuntimeError('Element is not currently interactable and may not be manipulated')
        except  (ElementNotVisibleException,ValueError) as ev:
            raise ev
        # taking screenshot at last of operation
        self.Utility_obj.takescreen()
        return self

    def click__with__googleID(self,emailID,gmailpswd, option):
        '''
        this function helps to using google credential to login to wizr by
        :param emailID:
        :return: wizr home page
        '''
        try:
            self.driver.implicitly_wait(40)
            self.click_element("Partner button")
            time.sleep(10)
            self.click_element("login_withGoogle")
            self.ivtree__credentials(gmailId =emailID,gmailPassword=gmailpswd)
            # EmailList = list(self.find_elements("google_accountList"))
            # time.sleep(5)
            # for index, text in enumerate(EmailList):
            #     # used regular expression for searching matching device and goto respective devices pages
            #     if re.search("%s" % emailID, self.get_text(text)):
            #         dynamic_xpath = "//p[@data-email=" + "'" + emailID + "']"
            #         # // p[ @ data - email = 'p@ivtree.com']
            #         self.click_element("%s" % dynamic_xpath)
            #         logger.info("Selected and clicked emailID", html=True)
            #     else:
            #         logger.info("Not Selected and clicked emailID", html=False)
            #     break
        except (ElementNotVisibleException,ValueError) as ev:
            logger.info('Element is not currently interactable and may not be manipulated',html=False)
            raise ev
        # logger.info('Google welcome message : %s'%self.get_text("welcome_googleMsg"))

        # permission = list(self.find_elements("okCancel_Permission"))
        # for index, opinion in enumerate(permission):
        #     # used regular expression for searching matching device and goto respective devices pages
        #     if re.search("%s" % option, self.get_text(opinion)):
        #         select_xpath = "//button[@id=" + "'" + option + "']"
        #         #  # // button[@id='deny']
        #         self.click_element("%s" % select_xpath)
        #         logger.info("Selected and clicked permission", html=True)
        #     else:
        #         logger.info("Not Selected and clicked permission", html=False)
        #     break

        # taking screenshot at last of operation
        self.Utility_obj.takescreen()
        logger.info("searching Partner visibility", html=True)
        return self

    def ivtree__credentials(self,gmailId,gmailPassword):
        '''
        this function help us to login wizr through ivtree credentials
        :param gmailId:
        :param gmailPassword:
        :return:
        '''
        try:
            self.input_text("ivtree_ID",gmailId)
            time.sleep(5)
            self.click_element("gmail_next")
            time.sleep(5)
            self.input_text("ivtree_password",gmailPassword)
            time.sleep(5)
            self.click_element("gmail_next")
            time.sleep(10)
        except (ElementNotVisibleException,ValueError) as ev:
            logger.info("Credentials not match", html=True)
            raise ev
        # taking screenshot at last of operation
        self.Utility_obj.takescreen()
        logger.info("Credentials matched", html=True)
        return self

    def login__second__time(self):
        '''
        this function help to login as 2nd time to wizr
        :return:
        '''
        try:
            # click on partner button
            time.sleep(60)
            title=self.get_title()
            logger.info(title)
            self.click_button("Partner button")
            self.driver.implicitly_wait(40)
            time.sleep(5)
            self.click_element("SecondEmail click")
            time.sleep(3)
        except NoSuchElementException :
            raise
        # taking screenshot at last of operation
        self.Utility_obj.takescreen()
        logger.info('logined 2nd time successfully', html=True)
        return self

    def login__with__secondCredentials(self,secondEmail,secondPassword):
        try:
            self.click_button("Partner button")
            time.sleep(3)
            self.click_element("Click NYAccount")
            time.sleep(8)
            # enter email & password
            self.input_text("Enter email", secondEmail)
            self.input_text("Enter password", secondPassword)

            time.sleep(4)
            self.click_button("Login button")
            logger.info('LOGINED successfully SECOND TIME', html=True)
        except (ElementNotVisibleException,ValueError) as ev:
            logger.info('LOGINED SECOND TIME Fail', html=True)
            raise ev
        # taking screenshot at last of operation
        self.Utility_obj.takescreen()
        logger.info('logined successfully SECOND TIME', html=True)
        return self

    def logout__from__googleCredentials(self):
        '''
        this functions help us to logout from wizr with google credentials
        :return:
        '''
        try:
            self.click_button("google_1stlogout")

            time.sleep(20)
            text=self.get_text("user")
            logger.info('logined user name: %s'%text)
            self.click_element("google_2ndlogout")
        except NoSuchElementException :
            raise
        # taking screenshot at last of operation
        self.Utility_obj.takescreen()
        logger.info("logged out from google WiZR ", html=True)
        return self

    def loop__entry(self):
        '''
            this functions help to run single action multiples times
        :return:
        '''
        try:
            count=1
            for loop in range(1,10):
                logger.info('hello subject Welcome for looping count :%d'%count)
                self.login__second__time()
                count += 1

        except :
            pass
        return self

    def get__rightGrid__list(self):
        '''
        this functions help us to list out the element present in rightGrid
        :return:
        '''
        try:
            time.sleep(10)
            self.click_element("right_grid")
            name=self.get_text("rightGrd_list")
            logger.info('Name of list: %s'%name)
            time.sleep(5)

            gridList=list(self.find_elements("rightGrd_feature"))
            #print all left grid list module
            for index, text in enumerate(gridList):
                functionName=self.get_text(text)
                logger.info('Module name : %s'%functionName)
            time.sleep(5)

        except NoSuchElementException as e:
            raise e

        self.Utility_obj.takescreen()
        logger.info('Display selected grid device ', html=True)
        return self

    def click__from__rightGrid(self, rtgridName):
        '''
        this functions help us to select rtgridName from right grid list and navigate to respective rtgridName
        :param rtgridName:
        :return:
        '''
        try:
            # get the rtgridName type Incidents,Locations,Cameras,Edge Devices,Alerts,Users
            gridList = list(self.find_elements("rightGrd_feature"))
            logger.info('Argument is : %s' % rtgridName)
            rtgridName = str(rtgridName)
            for index, module in enumerate(gridList):
                module= str(self.get_text(module))
                # comparision of aruments with list element
                if module == rtgridName:
                    logger.info('Module Name is : %s' % rtgridName)
                    dynamic_xpath = "//a[contains(text()," + "'" + rtgridName + "'" + ")]"
                    self.click_element("%s" % dynamic_xpath)
                    logger.info("Searched module %s clicked" %module)
                    break
                else:
                    logger.info("%s module not searched" %module)

        except StaleElementReferenceException as e:
            raise e

        self.Utility_obj.takescreen()
        logger.info('Selected rtgridName page Displayed', html=True)
        return self


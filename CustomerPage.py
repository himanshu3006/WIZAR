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



import time
import re
from robot.api import logger
from robotpageobjects import Page,robot_alias
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from Utility import *


class CustomerPage(Page):
    """
          Customer page will help us to do all the stuff related to customer page
          i.e navigating to customer creation, edition of already created customers,
           selecting particular customer and visualation of their respective incident

      """

    selectors={
        #left grid selector help to click left grid button and show the hidden modules
        "Left grid": "xpath=(//button[contains(@type,'button')])[1]",
        #customer grid help to click on customer element
        "Customer Grid": "xpath=(//*[text()='Customers'])[1]",
        #selector for fetching customer table data
        "customer link": "xpath=(//a)",
        "CustomersId List":"xpath=//tr/td[1]",
        "CustomerName List":"xpath=//tr/td[2]",
        "CustomerAddress List":"xpath=//tr/td[5]",
                     #Add New Customer
        "element":"xpath=//h3[contains(text(),'New Customer')]",
        "Customer Name":"xpath=//input[@name='name']",
        "Customer pta":"xpath=//input[contains(@id,'-Address-31224')]/..",
        "Customer Address":"xpath=//label[contains(text(),'Address')]",
        "Primary Contact":"xpath=(//label[contains(text(),'Contact Name')])[1]",
        "Create Customer":"xpath=//span[contains(text(),'Add')]/..",

        #Page navigator
        "|< button":"xpath=(//button[contains(@type,'button')])[11]",
        "< button":"(//button[contains(@type,'button')])[12]",
        # NUmeric selector helps to navigatae between customer pages
        "Page Number":"xpath=//button[contains(@type,'button')]/div/span",
        # > selector helps to navigatae between customer pages
        "> button":"xpath=(//button[contains(@type,'button')])[last()-2]",
        #>| selector helps to navigatae between last pages
        ">| button":"xpath=(//button[contains(@type,'button')])[last()-1]",
        #addCustomer selector helps to create new customers
        "Add Customer":"xpath=(//button[contains(@type,'button')])[last()]",
                     # edit setting
        # "Cancel button":"xpath=//span[contains(text(),'Cancel')]/../..",
        "Cancel button":"xpath=//div[contains(text(),'Edit Customer')]/div/button",
        "note_text":"xpath=//input[@name='secondaryContact.notes']",
        "save_button":"xpath=//span[contains(text(),'Save')]/..",
        "delete_button":"xpath=//span[contains(text(),'Delete')]/..",
        "Confirm_delete": "xpath=//span[contains(text(),'confirm delete')]",
                    #customerHREF pages
        "function_list":"xpath=//div[@value='0']/div[1]/button",
        "totalCount_ofFunctions":"xpath=//div[contains(text(),'total')]",


    }

    def __init__(self, *args, **kwargs):
        Page.__init__(self)
        self.Utility_obj = Utility()

    def scroll__bar(self):
        '''
        scrolling of scroll-bar in a page
        :param text:
        :return:
        '''
        alert = None
        try:
            alert = self._current_browser().switch_to_alert()
            logger.info("scrolled ")
            return alert
            self.execute_javascript("current_prompt.scrollBy(0,450)")
            self.driver.implicitly_wait(10)

        except:
            raise RuntimeError('There were no alerts')

    def getting__customer__info(self):
        '''
        getting desired camera information::- id, name & status
        :return: desired info of camera
        '''
        try:
            self.driver.implicitly_wait(10)
            #list of all customerID
            custIDList=list(self.find_elements("CustomersId List"))
            # list of all customerName
            custNameList=list(self.find_elements("CustomerName List"))
            # list of all customerAddress
            custAddressList = list(self.find_elements("CustomerAddress List"))

            #iterarting all customerName with its respective status
            for index,cName in enumerate(custNameList):
                logger.info('Customer ID: %s , Customer Name : %s, Current Address : %s ' % (self.get_text(custIDList[index]),self.get_text(cName),self.get_text(custAddressList[index])))
        except:
            logger.info('customer list not found', html=True)
                # taking screenshot at last of operation
        self.Utility_obj.takescreen()
        logger.info("getting customer details", html=True)
        return self

    def add_new__customer(self, nameOfCustomer, primContctOfCustomer, address):
        '''

        :return:
        '''
        #click on AddCustomer Button
        self.click_button("Add Customer")
        self.driver.implicitly_wait(20)
        #enter text into CustomerName field by help of passing argument
        self.input_text("Customer Name",nameOfCustomer)
        time.sleep(10)

        try:
            #click on address text field
            # self.click_element("Customer pta")
            # logger.info("CLIcked msg",html=True)
            # self.driver.implicitly_wait(40)
            # self.Utility_obj.takescreen()
            # self.driver.implicitly_wait(120)

            # self.click_element("Customer Address")
            self.input_text("Customer Address",address)
            self.driver.implicitly_wait(120)
            time.sleep(10)
            self.driver.switch_to_frame("frameName")
            self.driver.switch_to_frame("frameName.0.child")
            select = Select(self.driver.find_element_by_tag_name("span"))
            select.select_by_index(1)
            # self.click_button(addr[1])
        except:
            logger.info("Address not selected",html=True)
        self.Utility_obj.takescreen()

        # logger.info('Address source code %s'%self.get_source())
        # self.driver.find_element_by_xpath("//input[contains(@id,'undefined-Enteraddress-Address-56580')]").send_keys(address)
        # self.driver.implicitly_wait(20)
        # self.Utility_obj.takescreen()
            # self.input_text("Customer Address",address)
            # self.driver.implicitly_wait(10)
            # self.Utility_obj.takescreen()
            # self.current_frame_contains("address",loglevel='INFO')
            # logger.info('Address source code %s' % self.page_source())
            # self.Utility_obj.takescreen()
            # self.driver.implicitly_wait(10)
        # source_code12 = addr.get_attribute('innerHTML')
        # logger.info('Address source code %s' % source_code12)
        # self.get_attribute('innerHTML')
        # self.get_source()
        # logger.info('Address source code %s' % (self.get_source()))
        # addr=self.input_text("Customer Address", address)
        # self.input_text_into_prompt(addr)
        time.sleep(4)
        # select = Select(self.driver.find_element_by_xpath('//label[contains(text(),"Address")]/div/div/div'))
        # select.select_by_index(1)
        # select.select_by_visible_text(address)
        self.input_text("Primary Contact", primContctOfCustomer)
        self.scroll__bar()
        self.driver.implicitly_wait(30)
        self.click_button("Create Customer")
        # taking screenshot at last of operation
        self.Utility_obj.takescreen()
        logger.info('Customer added successfully', html=True)
        return self

    def click__particularCustomer(self):
        '''

        :return:
        '''

        # taking screenshot at last of operation
        self.Utility_obj.takescreen()
        logger.info("getting particular customer details", html=True)
        return self

    def getting__particularCustomer__detail(self, bool, idOfCustomer, nameOfCustomer,href, ActionToPerform):
        '''
        Here we get particular customer NAME & ID by passing customerID / customer name as argument
        And click on edit button for any modification
        :return:
        # '''
        # Used try-block to handle StaleElementReferenceException
        try:
            time.sleep(4)
            logger.info('Welcome to customerPage',html=True)
            self.flag= BuiltIn().get_variable_value("${bool}")
            logger.info('hello CUSTOMER',html=True)
            # flag help us to select which action we want to perform based on given argument i.e.(idOfCustomer, nameOfCustomer)
            if str(self.flag) == 'id':
                # list of all customerID
                logger.info('hello id',html=True)
                custIDList = list(self.find_elements("CustomersId List"))
                logger.info('Customer ID to be searched is :: %s' % (idOfCustomer))
                idOfCustomer = str(idOfCustomer)
                for index, custID in enumerate(custIDList):
                        # string conversion
                    ID = str(self.get_text(custID))
                    if ID == idOfCustomer:
                     # if id matches than controller will move inside loop to get further detail based on customer id
                        id_xpath = "//td[contains(text(),'" + idOfCustomer + "')]"
                        logger.info('Customer ID is :: %s' % (self.get_text(id_xpath)))  # get customer id

                        nam_xpath = "//td[contains(text(),'" + idOfCustomer + "')]" + "/../td[2]"
                        logger.info('Customer name is :: %s' % (self.get_text(nam_xpath)))  # get matching customer name

                        edit_xpath = "//td[contains(text(),'" + idOfCustomer + "')]" + "/../td[6]"
                        logger.info('Customer edit is :: %s' % (self.get_text(edit_xpath)))  # get matching customer
                        time.sleep(6)
                        #below code is for click customerName(present) or click on edit button(absent)
                        self.option = BuiltIn().get_variable_value("${selectAction}")
                        #if statement let us to go to respective incidentPage('linkCustomer' or 'editCustomer')
                        if str(self.option) == 'linkCustomer':
                            self.click_element(nam_xpath)
                            break
                        #elif statement let us to modify respective customer based on id
                        elif str(self.option) == 'editCustomer':
                            self.click_element(edit_xpath)
                            time.sleep(8)
                            self.scroll__bar()
                            self.driver.implicitly_wait(20)
                            self.Utility_obj.takescreen()

                            # what action to perform with the popup window (cancel, save, delete)
                            for value in range(1, 3):
                                if value == int(ActionToPerform):
                                    self.click_button("Cancel button")
                                    break
                                elif value == ActionToPerform:
                                    self.click_button("save_button")
                                    break
                                elif value == ActionToPerform:
                                    self.double_click_element("delete_button")
                                    # self.click_button("delete_button")
                                    break
                                else:
                                    logger.info("Not clicked", html=True)

                        else:
                            logger.info('Stay in Customer page',html=True)

                    else:
                        logger.info('Customer %s Id not matched with argument' % idOfCustomer)

            elif str(self.flag) == 'name':
                # list of all customerName
                custNameList = list(self.find_elements("CustomerName List"))
                logger.info('Customer Name to be searched is :: %s' % (nameOfCustomer))
                namOfCustomer = str(nameOfCustomer)
                self.scroll__bar()
                # if name matches than controller will move inside to get further detail obased on camera name
                for index, custName in enumerate(custNameList):
                    name = str(self.get_text(custName))
                    # namOfCustomer = str(nameOfCustomer)
                    if name == namOfCustomer:
                    # if name matches than controller will move inside loop to get further detail based on customer name
                        logger.info('Customer name hello  :: %s' % (namOfCustomer))
                        name_xpath = "//a[contains(text(),'" + namOfCustomer + "')]"
                        logger.info('Customer name is :: %s' % (self.get_text(name_xpath)))

                        id_xpath = "//a[contains(text(),'" + namOfCustomer + "')]" + "/../../td[1]"
                        # //a[contains(text(),'QA Team')]/../../td[1]
                        logger.info('Customer ID is :: %s' % (self.get_text(id_xpath)))

                        edit_xpath = "//a[contains(text(),'" + namOfCustomer + "')]" + "/../../td[6]/button"
                        # //a[contains(text(),'QA Team')]/../../td[6]/button
                        logger.info('Edit customer is :: %s' % (self.get_text(edit_xpath)))

                        # if idMatch == name:
                        self.click_element(edit_xpath)
                        time.sleep(8)
                        self.scroll__bar()
                        self.driver.implicitly_wait(20)
                        self.Utility_obj.takescreen()

                        # what action to perform with the popup window (cancel, delete, save)
                        for value in range(1, 3):
                            if value == int(ActionToPerform):
                                self.click_button("Cancel button")
                                break
                            elif value == ActionToPerform:
                                self.click_button("save_button")
                            elif value == ActionToPerform:
                                self.click_button("delete_button")
                            else:
                                logger.info("Not clicked", html=True)

                    else:
                        logger.info('Customer %s name not matched with list'%namOfCustomer)

            else:
                logger.info('Cant find appropriate argument match of customer by %s and $s'%idOfCustomer, nameOfCustomer)

        except:
            logger.info('Customer status not matched with', html=True)
        # taking screenshot at last of operation
        self.Utility_obj.takescreen()
        logger.info("Customer status matched with verified argument",html=True)
        return self

    def navigate__to__linkPage(self):
        '''
        this function helps us to get all the functions of customer that they have
        like (incidents, locations,cameras,edgeDevice, alert)

        :return:
        '''
        try:
            listOfFeature=list(self.find_elements("function_list"))
            for index, feature in enumerate(listOfFeature):
                logger.info('List of functions for customer :%s'%str(self.get_text(feature)))
        except:
            logger.info('link not found', html=True)
        # taking screenshot at last of operation
        self.Utility_obj.takescreen()
        logger.info("getting list of customer function", html=True)
        return self

    def click__Customer__function(self, choice):
        '''
        this function helps us to select anyone functions of customer that they have
        like (incidents, locations,cameras,edgeDevice, alert)
        and get all the respective details
        :return:
        '''
        try:
            #listOfFeature includes customer feature like (incidents, locations,cameras,edgeDevice, alert)
            listOfFeatures = list(self.find_elements("function_list"))
            choice = str(choice)
            for feature in listOfFeatures:
                if re.search(choice,self.get_text(feature)):
                    logger.info('matching function %s'%choice)
                    c = choice.capitalize()
                    logger.info('Capitalize of function is:: %s' % c)
                    dynamic_xpath="//div[contains(text(),'"+ choice.capitalize() +"')]"
                    # nc=self.get_text(dynamic_xpath)
                    logger.info('Customer function to select is:: %s'%dynamic_xpath)
                    self.click_element(dynamic_xpath)

            # Total_Count = self.get_text("totalCount_ofFunctions")
            # logger.info('Total function list count of %s '%Total_Count)
            # time.sleep(20)
        except:
            logger.info('Customer not found', html=True)
        # taking screenshot at last of operation
        self.Utility_obj.takescreen()
        logger.info("getting particular customer details", html=True)
        return self

    def get_function_totalCount(self):
        '''
        this function help us to get totalCount of page element list
        :return:
        '''
        try:
            time.sleep(10)
            Total_Count = self.get_text("totalCount_ofFunctions")
            logger.info('Total function list count of %s ' % Total_Count)
            time.sleep(10)
        except:
            logger.info('not able to get particular customer details', html=True)
        # taking screenshot at last of operation
        self.Utility_obj.takescreen()
        logger.info("getting particular customer details", html=True)
        return self

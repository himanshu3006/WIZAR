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
from telnetlib import EC
from selenium import *
import time , re
from robot.api import logger
from robotpageobjects import Page,robot_alias
from selenium.common.exceptions import StaleElementReferenceException, InvalidElementStateException, \
    NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait





from selenium.webdriver.support import *
from selenium.webdriver.support.ui import Select
from Utility import *


class CameraPage(Page):
    """
        Camera page will help us to do all the stuff related to camera page
        i.e navigating to camera creation, deletion, zone/liveView/location/Setting setting
    """


    selectors = {
    # """
    #     Camera page selector will help us to find all the  related to camera page element
    #       by help of css or xpath
    #     i.e finding each element path and assigned to some locator variables
    # """
        "CameraId List":"xpath=//tr/td[1]",
        "CameraName List": "xpath=//tr/td[2]",
        "Snapshot List": "xpath=//tr/td[3]",
        "CameraStatus List":"xpath=//tr/td[7]",
        "Active Camera":"xpath=(//input[contains(@type,'checkbox')])[1]",
        "Wall Camera":"xpath=//span[contains(text(),'Wall')]",
        "Toggle Camera":"xpath=//span[contains(text(),'Toggle Filter')]",
                # Add New Camera
        "Add Camera":"xpath=(//button[contains(@type,'button')])[last()]",
        "Find Name":"xpath=//span[contains(text(),'Cameras')]",
        "cam Name": "xpath=//input[@name='deviceName']",
        "cam Location":"xpath=//input[contains(@autocomplete,'off')]",
        "hidden loc":"xpath=//div[@style='padding: 8px 0px; display: block; width: 256px;']",
        "def loc":"xpath=//div[contains(text(),'Default location')]",
        "cam URL": "xpath=//input[@name='cameraUrl']",
        "Cloud view":"xpath=(//input[contains(@type,'checkbox')])[2]",
        "Mac Address":"xpath=//input[contains(@name,'cameraMacAddress')]",
         #need to be hardcoded by absolute path
        "Optloc":"xpath=html/body/div[3]/div/div/div/div/div/div[1]/span/div/div/div[contains(text(),'Default location')]",
        # "Add Button":"xpath=(//div/button[@type='button'])[22]",
        # "Add Button":"xpath=//*[contains(@data-reactid,'159')]",
        "Stream Camera":"xpath=//h3[contains(text(),'Camera Stream')]",
        "Stream speed":"xpath=//label[contains(text(),'Stream Speed')]/..",
        "Standard stream":"xpath=html/body/div[2]/div/div[1]/div/div/div[2]/form/div[3]/div[1]/div/div[1]/div[1]/div[2]",
        "Edge device":"xpath=//label[contains(text(),'Edge Device')]",
                    #full zone algorithm
        "Full Zone": "xpath=//div[contains(text(),'Full Zone Settings')]",
        "Object txt":"xpath=//label[contains(text(),'Objects')]",
        "Object click":"xpath=//label[contains(text(),'Objects')]/../div/div",
        "People click":"xpath=//label[contains(text(),'People')]",
        "Truck click":"xpath=//label[contains(text(),'Basic Car & Truck')]",
                    # close/cancel/create of new cameraPage
        "Cancel button":"xpath=//span[contains(text(),'Cancel')]/../..",
        "Create Camera": "xpath=//span[contains(text(),'Add')]/..",
        "Close button":"xpath=//span[contains(text(),'Close')]",
                    ## tripleDot  area of camera
        "triple_dot":"xpath=(//button[@type='button'])[7]/div",
        "triple_frame":"xpath=(//div[@data-reactroot=''])[2]",
        "triple_text":"xpath=((//div[@data-reactroot=''])[2]/div/div/div/div/div)",
        "seeting_option":"xpath=//*[contains(text(),'setting')]",
        "setting camPage":"xpath=(//button[@type='button'])[6]",
        "cam setting":"xpath=//div[contains(text(),'Camera Settings')]",
        "camera path":"xpath=(//div/div/p)[4]",
        # "Delete cam":"xpath=//span[contains(text(),'delete')]",
        # "Delete cam":"xpath=//button[@type='button']/div/div/span",
        "Delete cam":"xpath=html/body/div[2]/div/div[1]/div/div/div[2]/form/div[7]/div[1]/button",
        "Enable successMsg":"xpath=//span[contains(text(),'Camera enabled successfully.')]",
                    #live view xpath
        "Live View":"xpath=(//button[@type='button'])[8]",
        "camStream":"xpath=//h3",
        "Restart Stream":"xpath=//span[contains(text(),'Click to Restart Stream')]",
        "liveView Disconnect":"xpath=//h1",
        "Cross cancel":"xpath=(//button[@type='button'])[last()]",
                        # camera settings popup
        "Disable_camSetting":"xpath=//span[contains(text(),'Disable')]/../..",
        "Enable_camSetting":"xpath=//span[contains(text(),'Enable')]/../..",
        "enable_disableCamera":"xpath=//span[contains(text(),'delete')]/../../../../../button",
        "Cancel CS": "xpath=//span[contains(text(),'Cancel')]/../..",
        # "Delete cam":"xpath=(//button[contains(@type,'button')])[last()]/../div[1]",
        "Confirm delete": "xpath=//span[contains(text(),'confirm delete')]/../../..",
        "Save CS":"xpath=//span[contains(text(),'Save')]/../../..",

    }

    def __init__(self, *args, **kwargs):
        Page.__init__(self)
        self.Utility_obj = Utility()
        # sel = self.selenium

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
            time.sleep(8)

        except:
            raise RuntimeError('There were no alerts')

    def add__camera__viewCloud(self, camName, cameraLocation, MacAddress):
        '''
        Add new camera with valid data
        :param camName: name of camra from argument
        :param MacAddress: camera macAddress
        :param camLocation: name of camera location from argument
        :return: camera created successfully
        '''
        try:
            self.click_button("Add Camera")  # Click addButtonOfCamera
            self.Utility_obj.takescreen()
            time.sleep(20)
            self.Utility_obj.takescreen()
            self.input_text("cam Name", camName)  # Enter CameraNameThroughArguments
            # self.driver.implicitly_wait(60)
            self.input_text("cam Location", cameraLocation)
            time.sleep(20)

            # self.execute_javascript("document.findElementByXpath('(//button[contains(@type,'button')])[last()]').sendKeys('Default location')")
            time.sleep(20)
            # try:
            #     self.input_text("cam Location", cameraLocation)
            #     time.sleep(40)
            #     alert = self.driver.switch_to_alert()
            #     print alert.text
            #     alert.accept()
            # except:
            #     print "no alert to accept"
            # self.input_text("cam Location", cameraLocation)  # Enter Location from the resouce file
            time.sleep(10)

            # main_window_handle = None
            # while not main_window_handle:
            #     main_window_handle = self.driver.current_window_handle
            # self.driver.find_element_by_xpath(u'//*[text()="Camera Location*"]').click()
            # signin_window_handle = None
            # while not signin_window_handle:
            #     for handle in self.driver.window_handles:
            #         if handle != main_window_handle:
            #             signin_window_handle = handle
            #             break
            # self.driver.switch_to.window(signin_window_handle)
            # # self.input_text("cam Location", cameraLocation)
            # # time.selfleep(20)
            # # self.driver.find_element_by_xpath(u'//input[@id="id_1"]').send_keys(cameraLocation)
            # # driver.find_element_by_xpath(u'//input[@value="OK"]').click()
            # # driver.find_element_by_xpath(u'//input[@id="id_2"]').send_keys(user_text_2)
            # # driver.find_element_by_xpath(u'//input[@value="OK"]').click()
            # self.driver.switch_to.window(main_window_handle)  # or driver.switch_to_default_content()

            self.click_element("Cloud view")
            self.driver.implicitly_wait(60)
            self.input_text("Mac Address", MacAddress)
            time.sleep(10)

            stream = self.get_text("Stream speed")
            logger.info(stream)
            # self.click_element("Stream speed")
            # time.sleep(20)
            # # self.click_element("Stream speed")
            # streams = list(self.find_elements("//div[.='Standard')]"))
            # self.click_element(streams[1])
            # time.sleep(20)
            # streamed = list(self.find_elements("//div[.='Fast')]/.."))
            # self.click_element(streamed[3])
            # for index,ss in enumerate(stream):
            #     self.driver.implicitly_wait(20)
            #     logger.info('speed :%s'%self.get_text(ss[index]))
            #     if index == 3:
            #         self.cameraLocationick_element(ss[3])

            time.sleep(8)
            self.scroll__bar()
            self.driver.implicitly_wait(20)
            edge = self.get_text("Edge device")
            logger.info(edge)

            ele1 = list(self.find_elements("//div[.='Wizr Cloud']"))
            self.click_button(ele1[1])  # clicking on list to select
            self.driver.implicitly_wait(20)
            time.sleep(4)
            ele = list(self.find_elements("//div[.='WiZR-Stage-QA-server-1']/.."))
            self.driver.implicitly_wait(20)
            self.click_element(ele[3])
            self.scroll__bar()
            time.sleep(20)
            self.click_element("Create Camera")  # click on create camera
            # taking screenshot at last of operation
            self.Utility_obj.takescreen()
            logger.info('Camera added successfully without url', html=True)


        except InvalidElementStateException as ex:
            logger.info("Exception message ",ex.message)

        return self


    def add__camera__url(self, camName, camURL, cameraLocation, edgeDevice):
        '''
        Add new camera using insicam url with valid data
        :param camName: name of camra from argument
        :param camURL: name of camera url from argument
        :param camLocation: name of camera location from argument
        :param ssStand: name of camera speed from argument
        :return: camera created successfully
        '''
        try:
            time.sleep(2)
            self.Utility_obj.takescreen()
            self.click_button("Add Camera")         #Click addButtonOfCamera

            time.sleep(7)
            self.input_text("cam Name", camName)    #Enter CameraNameThroughArguments
            self.driver.implicitly_wait(20)
            self.input_text("cam Location", cameraLocation)  # Enter Location from the resouce file
            self.driver.implicitly_wait(20)
            self.input_text("cam URL", camURL)  # Enter CameraURLThroughArgument
            self.driver.implicitly_wait(20)
                #Wizr Cloud
            edge = self.get_text("Edge device")
            logger.info(edge)
            ele1 = list(self.find_elements("//div[.='Wizr Cloud']"))  # getting the list
            # for e in ele1:
            #     logger.info('edge device %s'% (self.get_text(e)))
            #     time.sleep(10)
            #     self.Utility_obj.takescreen()
            self.click_button(ele1[1])  # clicking on list to select
            time.sleep(5)
                    #WiZR-Stage-QA-server
            ele = list(self.find_elements("//div[.='WiZR-Stage-QA-server-1']/.."))  # getting a list
            self.driver.implicitly_wait(20)
            self.click_element(ele[3])
            #
            # '''
            # '''
            # self.input_text("cam URL", camURL)      #Enter CameraURLThroughArgument
            # time.sleep(4)
            #
            # self.click_element("cam Location")      #Click OnCameraText and SelectFromPopup
            # time.sleep(3)
            #
            # ele=self.execute_javascript("document.getElementsByTagName('style')")
            # logger.info('hidden location is %s '%ele)
            # ''''''''
            # ele=getattr(self,"style")
            #
            # self.execute_javascript('arguments[0].setAttribute("style","padding: 8px 0px; display: block; width: 256px;")'.
            #                         Select(self.find_elements("hidden loc")).select_by_visible_text("Default location"))
            #
            # self.click_element("def loc")
            # self.click_element("txt")
            # select(self.find_elements("hidden loc")).select_by_visible_text("Default location")
            # self.clear_element_text("cam Location") #clear and enter text
            # # self.input_password("cam Location",cameraLocation)
            # time.sleep(6)
            # self.click_element("cam Location")
            ##############################
            # camlocList = list(self.find_elements("hidden loc"))
            #
            # # iterarting all cameralocation with its respective status
            # for index, cloc in enumerate(camlocList):
            #     logger.info('Cameras location: %s ' % (self.get_text(cloc[index])))
            #
            #     if cameraLocation in cloc:
            #         print cameraLocation


                #
            # alert = self._current_browser().switch_to_alert()
            # logger.info("selected")
            # return alert
            # selectLoc=list(self.execute_javascript("document.querySelector('')"))
            # for index,option in enumerate(selectLoc):
            #     logger.info('selected oprtion:%s'%self.get_text(selectLoc[index]))

                #     for option in select.find_elements_by_xpath('//*[@id="ctl00_PlaceHolderMain_ctl35_ctl00_SelectResult"]/option'):
                # #     if option.text != 'Channel':
                # #         option.select()  # select() in earlier versions of webdriver
                # alert(document.querySelector('ul [style="background-color: transparent;"]'));
                # alert(document.querySelector('ul[style="background-color: transparent;"]'));
                # time.sleep(5)
                # window_after = self.current_frame_contains('Default location',loglevel='INFO')
                # parent_h = self.current_window_handle
                # # click on the link that opens a new window
                # handles = self.window_handles  # before the pop-up window closes
                # handles.remove(parent_h)
                # self.switch_to_window(handles.pop())
                # # do stuff in the popup
                # select = self.find_element('ctl00_PlaceHolderMain_ctl35_ctl00_SelectResult')
                # # for option in select.find_elements_by_xpath('//*[@id="ctl00_PlaceHolderMain_ctl35_ctl00_SelectResult"]/option'):
                # #     if option.text != 'Channel':
                # #         option.select()  # select() in earlier versions of webdriver
                # # popup window closes
                # self.switch_to_window(parent_h)
                # # and you're back
                # self.find_elements("def loc")
                # try:
                #     alert = self._current_browser().switch_to_alert()
                #     logger.info("Good Morning")
                #      # self.execute_javascript("current_prompt.find_element_by_xpath('//div[contains(text(),'Default location')]')")
                #     return alert
                #     time.sleep(5)
                #     window_after = self.window_handles[1]
                #     self.switch_to_window(window_after)
                #     time.sleep(5)
                #     window_before = self.window_handles[0]
                #     self.find_elements("def loc")
                #

            # self.click_element("Optloc")    #select default location
    ###################################################
            self.scroll__bar()
            time.sleep(4)

            FZ=self.get_text("Full Zone")   #get Full zone text from popup
            logger.info(FZ)                 #print text of FZ
            time.sleep(3)
            self.scroll__bar()              #SCROLL THE SLIDER VERTIVAL BAR
            time.sleep(10)
            algo_obj=self.get_text("Object txt")    #GET algorithm object text
            logger.info(algo_obj)                   #print object text
            self.click_element_at_coordinates("Object click",310, 584)  #click on object coordinate
            # self.click_element("Object click")
            logger.info("Object clicked successfully")          #print msg
            time.sleep(4)
            algo_peop = self.get_text("People click")           #get people algorithm text
            logger.info(algo_peop)                              #print algo  people
            # self.click_element("People click")
            # time.sleep(4)
            # self.click_element("Truck click")
            # time.sleep(3)
            #clicking of create camera button
            self.click_element("Create Camera")                    #click on create camera

        except (NoSuchElementException,ValueError) as nv:
            logger.info('Camera using url not created',html=True)
            raise  nv
        # taking screenshot at last of operation
        self.Utility_obj.takescreen()
        logger.info('Camera added successfully', html=True)
        return self


    def getting__camera__info(self):
        '''
        getting desired camera information::- id, name & status
        :return: desired info of camera
        '''
        try:
            time.sleep(8)
            #list of all cameraID
            camIDList=list(self.find_elements("CameraId List"))
            # list of all cameraName
            camNameList=list(self.find_elements("CameraName List"))
            # list of all cameraStatus
            camStatusList = list(self.find_elements("CameraStatus List"))

            #iterarting all cameraName with its respective status
            for index,cName in enumerate(camNameList):
                logger.info('Cameras ID: %s , Cameras Name : %s, Current status : %s ' % (self.get_text(camIDList[index]),self.get_text(cName),self.get_text(camStatusList[index])))
        except NoSuchElementException as n:
            logger.info('not able to get camera imformation')
            raise  n
            # taking screenshot at last of operation
        self.Utility_obj.takescreen()
        logger.info("getting camera details", html=True)
        return self


    def camera__layout(self,select):
        '''
        this function helps us to click on header of camera
        will click on basis of argument
        '''
        try:
            #list for comparison of select argument and click on respective functionality
            x=['1','2','3']
            if str(select) in x:
            # if str(select) in x:
                self.click_element("Active Camera")

            elif str(select) in x:
                self.click_element("Wall Camera")

            elif str(select) in x:
                self.click_element("Toggle Camera")

            else:
                logger.info("wrong selection")
        except NoSuchElementException as n:
            logger.info('camera wall layout not clicked')
            raise n
         # taking screenshot at last of operation
        self.Utility_obj.takescreen()
        logger.info('camera functionality clicked based on argument', html=True)
        return self


    def verifying__camera__Setting(self, idOfCamera, nameOfCamera, clickSetting):
        '''
        Here we verify camera STATUS,NAME & ID by passing cameraID as argument
        And if status is not running then contoller will goto respective camera setting
        And click on enabled button till status changed to running
        :return:
        # '''
        # Used try-block to handle StaleElementReferenceException  #, selection, camera_setting

        time.sleep(15)
        # get list of camName and camID
        camNameList = list(self.find_elements("CameraName List"))
        camIDList = list(self.find_elements("CameraId List"))

        idoc=logger.info('idOfCamera to be searched is %s::' % (idOfCamera))
        nameOC = logger.info('nameOfCamera to be searched is %s::' % (nameOfCamera))
        try:
            # if id matches than controller will move inside loop to get further detail based on camera id
            if idOfCamera == "1943":
                #loop for iteration of camera id
                for index,value in enumerate(camIDList):
                    #if condition is true or matching
                    if str(idOfCamera) == str(self.get_text(value)):
                        logger.info('Cameras ID found is :: %s' % self.get_text(camIDList[index]))
                        unId = str(idOfCamera)
                        id_xpath = "//td[contains(text()," + unId + ")]"
                        id_camName=self.get_text(id_xpath)
                        logger.info('Camera ID is :: %s' % id_camName)  #get camera id

                        nam_xpath = "//td[contains(text()," + unId + ")]" + "/../td[2]"
                        logger.info('Camera name is :: %s' % (self.get_text(nam_xpath)))    #get matching camera name

                        status_xpath= "//td[contains(text()," + unId + ")]" + "/../td[7]"
                        logger.info('Camera status is :: %s' % (self.get_text(status_xpath)))   #get matching camera status

                        # self.change__status(status_xpath) # contoller moving to change__status functions
                        try:
                            logger.info('Setting to be clicked is : %s' % clickSetting)
                            time.sleep(20)
                            id_camName=str(id_camName)
                            if str(clickSetting) == 'Live View':
                                camera_liveView = "//td[contains(text(),'" + id_camName + "')]/../td[8]/div/div/button"
                                time.sleep(20)
                                logger.info('Camera liveView is :: %s' % (self.get_text(camera_liveView)))

                            elif str(clickSetting) == 'Camera Incidents':
                                camera_incident = "//td[contains(text(),'" + id_camName + "')]/../td[8]/div/div/a"
                                time.sleep(20)
                                logger.info('Camera Incidents is :: %s' % (self.get_text(camera_incident)))

                            elif str(clickSetting) == "dot":
                                triplet_dots = "// td[contains(text(), '" + id_camName + "')]/../td[8]/div/div/div"
                                logger.info('Camera triple dot is :: %s' % (self.get_text(triplet_dots)))
                                time.sleep(20)
                                self.click_element(triplet_dots)
                                # logger.info('Element to be selected is : %s' % selection)
                                # logger.info('camera setting to be selected is : %s' % camera_setting)
                                # self.triple__dot__feature(selection, camera_setting)

                            else:
                                logger.info('setting not selected for camera', html=True)
                                # self.change__status(status_xpath)
                                # camera_id=int(camera_id)
                                # triplet_dots="(//a[contains(@href,'/incidents?deviceId=" + camera_id + "')]/..)/div/button/div"
                        except ValueError as e:
                            logger.info('clickSetting by id not working', html=True)
                            raise e

            else:
                #if name matches than controller will move inside to get further detail obased on camera name
                for index,value in enumerate(camNameList):
                    if str(nameOfCamera) == str(self.get_text(value)):
                        logger.info('sucessullly find Cameras Name  :: %s ' % self.get_text(camNameList[index]))
                        unName = str(nameOfCamera)

                        camera_nam_xpath = "//td[contains(text()," + unName + ")]"
                        nam_element=self.get_text(camera_nam_xpath)
                        logger.info('Camera name is :: %s' % nam_element)

                        camera_id_xpath = "//td[contains(text()," + unName + ")]" + "/../td[1]"
                        camera_id = self.get_text(camera_id_xpath)
                        logger.info('Id of respective Camera :: %s '%camera_id)

                        time.sleep(50)
                        camera_status_xpath = "//td[contains(text()," + unName + ")]" + "/../td[7]"
                        logger.info('Camera status is :: %s' % (self.get_text(camera_status_xpath)))
                        # try:
                        logger.info('Setting to be clicked is : %s' % clickSetting)
                        time.sleep(10)
                        # camera_id=str(camera_id)
                        clickSetting == str(clickSetting)
                        if str(clickSetting) == 'Live View':
                            camera_liveView = "//td[contains(text(),'" + camera_id + "')]/../td[8]/div/div/button"
                            time.sleep(10)
                            logger.info('Camera liveView is :: %s' % (self.get_text(camera_liveView)))

                        elif str(clickSetting) == 'Camera Incidents':
                            camera_incident="//td[contains(text(),'" + camera_id + "')]/../td[8]/div/div/a"
                            time.sleep(10)
                            logger.info('Camera Incidents is :: %s' % (self.get_text(camera_incident)))

                        elif str(clickSetting) == 'dot':
                            triplet_dots= "//td[contains(text(), '" + camera_id + "')]/../td[8]/div/div/div"
                            logger.info('Camera triple_dot is :: %s' % (self.get_text(triplet_dots)))
                            time.sleep(20)
                            self.click_element(triplet_dots)
                                # logger.info('Element to be selected is : %s' % selection)
                                # logger.info('camera setting to be selected is : %s' % camera_setting)
                                # self.triple__dot__feature(selection, camera_setting)

                        else:
                            logger.info('setting not selected for camera',html=True)
                            # self.change__status(status_xpath)
                            # camera_id=int(camera_id)
                            # triplet_dots="(//a[contains(@href,'/incidents?deviceId=" + camera_id + "')]/..)/div/button/div"
                        # except:
                        #     logger.info('clickSetting by name not working',html=True)
                        # finally:

        except:
            logger.info('camera setting not clicked')
        # taking screenshot at last of operation
        self.Utility_obj.takescreen()
        logger.info('camera status matched with verified argument', html=True)
        return self

    def live_view(self):
        # liveView="//td[contains(text(),'1883')]/../td[9]/div/div/button"
        logger.info('Liew view display',html=True)
        return self

    def change__status(self, status_xpath):
        '''
        check status of respective camera
         if status is running execute if loop
          and if not then execute else loop
            where controller will move to setting section of respective camera and goes on clicking till status changed to running
        :param dynamic_xpath:
        :return: enabled success msg
        '''
        try:
            status = self.get_text(status_xpath)
            #if status is matching come out of if loop and print msg
            if status == "Running":
                logger.info("Status Matches" , html=True)

            # if status not matching enter to else part
            elif status==" ":

                #range of loop to iterate
                    status_loop=range(1,10)
                    for x in status_loop:
                        # time.sleep(20)
                        message = ':'.join([str("Count is:: "), str(x)])
                        logger.info(message)
                        #click on setting option of respective camera
                        self.click_element("setting camPage")
                        time.sleep(4)
                        #scroll the bar of pop-up
                        self.scroll__bar()
                        #find and click on enabled button
                        time.sleep(8)
                        self.click_element("Enable CS")
                        # time.sleep(10)
                        # getting enabled msg & storing in a variable & printing the fetched text
                        vsm=self.get_text("Enable successMsg")
                        logger.info(vsm)
                        # comparison of text done with assert function
                        # assert  "Camera enabled successfully." == vsm


                        #if status matched come out of loop
                        if str(x)==status:
                            break

            else:
                self.driver.refresh()
                time.sleep(120)
                self.driver.refresh()

        except StaleElementReferenceException:
                self.fix_error()

             # taking screenshot at last of operation
        self.Utility_obj.takescreen()
        logger.info('status of camera verified', html=True)
        return self

    def triple__dot__feature(self, selection, camera_setting):
        '''
        this function helps us to click on triplet grid dot
        and select specified element like setting or Zone Setting or Location
        :param selection:  arguments passed from respective robotfile
        :return: selected setting page
        '''
        logger.info('Element To Be Selected is : %s' % selection)
        logger.info('Camera Setting To Be Selected is : %s' % camera_setting)
        time.sleep(60)
        # wait = WebDriverWait(self.driver, 30)
        # wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@data-reactroot=''])[2]")))
        # time.sleep(5)
        triple = self.get_text("triple_frame")
        logger.info('frame text : %s' % triple)
        selectText = self.find_elements("triple_text")
        logger.info('frame text : %s' % selectText)
        time.sleep(20)
        try:
            # if selection argument match with Setting then below code will execute with respective camera_setting
            if str(selection) == "Settings":
                dynamicSet = "(//div[contains(text(),'Settings')])[1]"
                d_setting = self.driver.find_element_by_xpath(dynamicSet)
                logger.info('setting xpath is %s '%d_setting)
                self.click_element(d_setting)

                # wait = WebDriverWait(self.driver, 50)
                # wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='deviceName']")))
                time.sleep(10)
                if str(camera_setting) == 'Delete Camera':
                    self.Delete__Camera()

                elif str(camera_setting) == 'Cancel Camera':
                    self.Camera__Setting__Canceled()

                elif str(camera_setting) == 'Disable Camera':
                    self.Camera__Setting__EnableDisabled()

                elif str(camera_setting) == 'Save Camera':
                    self.Camera__Setting__Saved()

                else:
                    logger.info('Camera setting not selected')

                # if selection argument match with ZoneSetting then below code will execute
            elif selection == "Zone Settings":
                dynamicZon = "(//div[contains(text(),'Settings')])[2]"
                dz = self.driver.find_element_by_xpath(dynamicZon)
                time.sleep(15)
                self.click_element(dz)

            # if selection argument match with Location then below code will execute
            elif selection == "Location":
                dynamicLoc = "//div[contains(text(),'Location')]"
                dc = self.driver.find_element_by_xpath(dynamicLoc)
                time.sleep(15)
                self.click_element(dc)
            else:
                    logger.info('No option selected ', html=True)
        except Exception as error:
            logger.info('selection fail to click element %s'%error.message)

        # taking screenshot at last of operation
        self.Utility_obj.takescreen()
        return self

    # wait = WebDriverWait(self.driver, 30)
    # nyAccount = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Not your account?')]")))
    # nyAccount.click()


    # def getNodeText(node):
    #     from xml.dom import minidom
    #
    #     doc = minidom.parse("staff.xml")
    #
    #     nodelist = node.childNodes
    #     result = []
    #     for node in nodelist:
    #         if node.nodeType == node.TEXT_NODE:
    #             result.append(node.data)
    #     return ''.join(result)
    #
    #     name = doc.getElementsByTagName("name")[0]
    #     print("Node Name : %s" % name.nodeName)
    #     print("Node Value : %s \n" % getNodeText(name))

    def Camera__Setting__Canceled(self):
        '''
        this function help us to cancel camera
        :return:
        '''
        try:
            time.sleep(4)
            self.scroll__bar()
            time.sleep(10)
            self.click_element("Cancel CS")
            logger.info("Successfully Canceled", html=True)
        except:
            logger.info('camera setting not canceled')
        # taking screenshot at last of operation
        self.Utility_obj.takescreen()
        logger.info('Selected Camera canceled setting verified', html=True)
        return self

    def Camera__Setting__EnableDisabled(self):
        '''
        this function help us to disable camera
        :return:
        '''
        try:
            time.sleep(4)
            self.scroll__bar()
            time.sleep(10)

            edCam = self.get_text("enable_disableCamera")
            logger.info('Button option for disable or enable is :: %s'%edCam)
            if edCam == 'ENABLE':
                self.click_element("Enable_camSetting")
            elif edCam == 'DISABLE':
                self.click_element("Disable_camSetting")
            else:
                logger.info('Unable to click disable/enable button')
            logger.info("Successfully Enabled / Disabled", html=True)
        except:
            logger.info('camera setting enable/disable not clicked')
        # taking screenshot at last of operation
        self.Utility_obj.takescreen()
        logger.info('Selected Camera setting enabled/disabled verified', html=True)
        return self

    def Camera__Setting__Saved(self):
        '''
        this function help us to save camera
        :return:
        '''
        try:
            time.sleep(4)
            self.scroll__bar()
            time.sleep(10)
            self.click_element("Save CS")
            logger.info("Successfully Saved", html=True)
        except:
            logger.info('camera setting not saved')
        # taking screenshot at last of operation
        self.Utility_obj.takescreen()
        logger.info('Selected Camera setting Saved', html=True)
        return self

    def Delete__Camera(self):
        '''
        this function help us to delete camera
        :return:camera deleted successfully
        '''
        try:
            time.sleep(10)
            # scrolling of vertical scroll-bar
            self.scroll__bar()
            time.sleep(5)
            # self.double_click_element("Delete cam")
            self.click_button("Delete cam")
            logger.info("first Deleted", html=True)
            time.sleep(5)
            self.click_button("Delete cam")
            # self.click_button("Conf delete")
        except ValueError as ve:
            logger.info('Selected Camera Not Deleted')
            raise ve
        # taking screenshot at last of operation
        self.Utility_obj.takescreen()
        logger.info("Selected Camera Successfully Deleted", html=True)
        return self

    def Camera__Live__View(self,filename):
        '''
        this function helps us to see camera live view
        :param filename:
        :return:
        '''
        try:
            self.verificationErrors = []
           # self.video = castro.Castro(filename)
            self.video.start()
            # self.selenium.start()
            # sel = self.selenium

            self.click_element("Live View")
            self.driver.implicitly_wait(40)
            # stream = self.get_text("camStream")
            # logger.info(stream,html=True)
            self.driver.implicitly_wait(60)

            # text=self.get_text("liveView Disconnect")
            # if text== "Disconnect":
            #     self.click_element("Restart Stream")
            #
            # else:
            self.wait_until_page_does_not_contain_element("Restart Stream",timeout="80000")
                # sel.wait_for_page_to_load("30000")
            self.driver.implicitly_wait(60)
            self.scroll__bar()
            self.driver.implicitly_wait(120)
            self.click_element("Cross cancel")
            self.video.stop()
            self.video.process()
            self.assertEqual([], self.verificationErrors)
        except:
            logger.info('Live View not able to record')
        # taking screenshot at last of operation
        self.Utility_obj.takescreen()
        logger.info("Live View Successfully recorded ", html=True)
        return self

    # def tearDown(self):
    #     # self.selenium.stop()
    #     self.video.stop()
    #     self.video.process()
    #     self.assertEqual([], self.verificationErrors)

    # my-cool-screencast.swf

    # def videoRecording(self, filename, Browser, SiteUrl):
    #     def setUp(self):
    #         self.verificationErrors = []
    #         self.video = castro.Castro(filename)
    #         self.video.start()
    #         self.selenium = selenium("localhost", 4444, Browser, SiteUrl)
    #         self.selenium.start()
    #         self.selenium.window_maximize()
    #
    #     def test_my(self):
    #         sel = self.selenium
    #         sel.open("/")
    #         sel.click("link=blog")
    #         sel.wait_for_page_to_load("30000")
    #

if __name__ == "__main__":
    Page.main()


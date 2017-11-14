# these are all clases importing and utilising in our current library
from robotpageobjects import Page, robot_alias
from robot.api.deco import keyword
import time
from robot.api import logger
from Utility import *
class IncidentManagementPage(Page):
    """
    This class will verify Incident is present in Incident Management Queue
    """
    # These are all the selectors which are used in the current library
    selectors = {
        "incilist":"xpath=//img[contains(@alt,'Incident')]",

        "Employee tag":"xpath=//p[contains(text(),'Employee Seen')]",
        "Resident tag":"xpath=//p[contains(text(),'Resident Seen')]",
        "Person tag":"xpath=//p[contains(text(),'Person Seen')]",
        "Vehicle tag":"xpath=//p[contains(text(),'Vehicle Seen')]",
        "Street traffic tag":"xpath=//p[contains(text(),'Street Traffic')]",
        "Light flicker tag":"xpath=//p[contains(text(),'Light Flicker')]",
    }

    def __init__(self, *args, **kwargs):
        Page.__init__(self)
        self.Utility_obj = Utility()

    @keyword('get_incidentid')
    def get_incidentid(self, string):
        '''
        # Method to get Incident Id from the resourse file
        :param string:
        :return:
        '''
        if string:
            logger.info('get_incidentid clicked%s' % type(string), html=True)
            self.incident_id = str(string)
            return self
        else:
            print "please pass Incident id from resource file"
            return self

    @robot_alias("click_name_incimanagement")
    def click_name_incimanagement(self, incident_id):
        '''
        # This robot alias used to verify Incident Management
        :return:
        '''
        try:
            logger.info("Before Searching for incident ID: "+str(incident_id))
            self.Utility_obj.takescreen()
            names = list(self.find_elements("incilist"))
            # Here we Verifying Incident is present in the Queue or not
            for name in names:  # Second Example
                print 'Incident ID is :', name.text
                # Here we getting Slice of Incident id from the string
                inc=str(name.text).__getslice__(4,11)
                if inc == incident_id:
                    xele="// div[contains(text(), 'ID# "+incident_id+"')]"
                    self.click_element(xele)
                    # After element found and Verified by taking screenshot
                    Utility.FLAG="TRUE"
                    self.execute_javascript("window.scrollTo(0, 0)")
                    time.sleep(self.Utility_obj.MEDIUM)
                    # taking screenshot at last of operation
                    self.Utility_obj.takescreen()
                    break
                self.Utility_obj.INCIDENT+=1
            # Printing message if Incident is not present in the Queue and total number of icidents
            if(self.Utility_obj.FLAG=="FALSE"):
                logger.info("\nTotal number of incidents are " + str(self.Utility_obj.INCIDENT))
                logger.info("\n\nIncident Not Found in Queue List")
                logger.info("After Searching for incident ID: " + str(incident_id))
                self.Utility_obj.takescreen()
        except:
            logger.info('incident not clicked',html=True)
        return self

    # this robot to use Inc_man_1 testcase
    @robot_alias("select_any_incidnets_randomly")
    def select_any_incidnets_randomly(self):
        '''
               # This robot alias used to verify Incident Management
               :return:
        '''
        try:
            for x in range(1, 6):
                self.click_element("//*[@id='app']/div[1]/div[3]/div[2]/div[3]/div[1]/div/div/div["+str(x)+"]")
                time.sleep(self.Utility_obj.SIMPLE_WAIT)
                self.Utility_obj.takescreen()
                time.sleep(self.Utility_obj.SIMPLE_WAIT)
            logger.info("Successfully selected randomly")
        except:
            logger.info('Not randomly selected',html=True)
        return self

    # this robot to use Inc_man_1 testcase
    @robot_alias("select_any_incidnets_randomly_and_close")
    def select_any_incidnets_randomly_and_close(self):
        '''
                # This robot alias used to verify Incident Management
                :param testcase_id:
                param incident_id:
                :return:
        '''
        try:
            for x in range(1, 6):
                self.click_element("//*[@id='app']/div[1]/div[3]/div[2]/div[3]/div[1]/div/div/div[" + str(x) + "]")
                time.sleep(self.Utility_obj.SIMPLE_WAIT)
                self.Utility_obj.takescreen()
                self.wait_until_element_is_visible("//*[@id='app']/div[1]/div[3]/div[1]/div/div[1]/div[3]/div/div[2]/div[1]/button/div/div",60,"Close button not visibled")
                self.click_element("//*[@id='app']/div[1]/div[3]/div[1]/div/div[1]/div[3]/div/div[2]/div[1]/button/div/div")
                time.sleep(self.Utility_obj.SIMPLE_WAIT)
                logger.info("Screenshot taking after close incident")
                self.Utility_obj.takescreen()
            logger.info("Successfully selected and close randomly")
        except:
            logger.info('Not randomly selected and closed',html=True)
        return self

    @robot_alias("select_any_incidnets_randomly_and_verify_camera_wall")
    def select_any_incidnets_randomly_and_verify_camera_wall(self):
        '''
                # This robot alias used to verify Incident Management
                :param testcase_id:
                param incident_id:
                :return:
        '''
        try:
            for x in range(1, 6):
                self.click_element("//*[@id='app']/div[1]/div[3]/div[2]/div[3]/div[1]/div/div/div[" + str(x) + "]")
                time.sleep(self.Utility_obj.SIMPLE_WAIT)
                self.Utility_obj.takescreen()
                web_element="//*[@id='app']/div[1]/div[3]/div[1]/div/div[3]/div[3]/div[2]/p"
                Error_Text="This camera does not have a location configured correctly."
                Map_Web_Element=self.get_text(web_element)
                if(Map_Web_Element == Error_Text):
                    logger.info("Camera wall is not present")
                    self.Utility_obj.takescreen()
                    # self.assertEqual(Map_Web_Element, Error_Text, msg="Camera wall is not present in the incident management page")
                    return AssertionError

                else:
                    time.sleep(self.Utility_obj.SMALL)
                    self.click_button("//*[@id='app']/div[1]/div[3]/div[1]/div/div[3]/div[3]/div[2]/div[2]/button")
                    time.sleep(self.Utility_obj.MEDIUM)
                    self.Utility_obj.takescreen()
                    self.click_button("/html/body/div[4]/div/div[1]/div/div/div[2]/button")
                    logger.info("Successfully verify camera wall")
                    self.Utility_obj.takescreen()
        except:
            logger.info('camera Wall Not Verified')
        return self

    @robot_alias("navigate_to_incidentmanagement")
    def navigate_to_incidentmanagement(self):
        '''
                # To navigate Incident Management
                :return:
        '''
        try:
            time.sleep(self.Utility_obj.SMALL)
            self.click_element("Menu")
            self.click_element("incimanage")
            time.sleep(self.Utility_obj.MEDIUM)
            logger.info("Successfully navigate")
        except:
            logger.info('Not navigated',html=True)

        self.Utility_obj.takescreen()
        return self

    @robot_alias("mark_incident_flag")
    def mark_incident_flag(self,mark_incident):
        '''
                 # To mark incident flag
                :return:
        '''
        try:
            logger.info("Screenshot before mark the flag")
            self.Utility_obj.takescreen()
            if(mark_incident=="Correct"):
                self.click_element("//span[contains(.,'Correct')]")
                logger.info("Marked incident as Correct")
                time.sleep(self.Utility_obj.MEDIUM)
                self.Utility_obj.takescreen()

            elif(mark_incident=="False"):
                self.click_element("//span[contains(.,'False')]")
                logger.info("Marked incident as False")
                time.sleep(self.Utility_obj.MEDIUM)
                self.Utility_obj.takescreen()

            elif(mark_incident=="Missed"):
                self.click_element("//span[contains(.,'Missed')]")
                logger.info("Marked incident as Missed")
                time.sleep(self.Utility_obj.MEDIUM)
                self.Utility_obj.takescreen()

            else:
                logger.info("No incident marked")
        except:
            logger.info('Incident flag not marked',html=True)
        self.Utility_obj.takescreen()
        return self

    @robot_alias("verify_tags")
    def verify_tags(self, tag1, tag2, tag3, tag4, tag5, tag6):
        try:
            time.sleep(self.Utility_obj.MEDIUM)
            for x in range(1,7):
                if(tag1=="Employee" or tag2=="Employee" or tag3=="Employee" or tag4=="Employee" or tag5=="Employee" or tag6=="Employee"):
                        self.click_element("Employee tag")
                elif(tag1=="Resident" or tag2=="Resident" or tag3=="Resident" or tag4=="Resident" or tag5=="Resident" or tag6=="Resident"):
                        self.click_element("Resident tag")
                elif (tag1 == "Person" or tag2 == "Person" or tag3 == "Person" or tag4 == "Person" or tag5 == "Person" or tag6 == "Person"):
                        self.click_element("Person tag")
                elif (tag1 == "Vehical" or tag2 == "Vehical" or tag3 == "Vehical" or tag4 == "Vehical" or tag5 == "Vehical" or tag6 == "Vehical"):
                        self.click_element("Vehicle tag")
                elif (tag1 == "Street traffic" or tag2 == "Street traffic" or tag3 == "Street traffic" or tag4 == "Street traffic" or tag5 == "Street traffic" or tag6 == "Street traffic"):
                        self.click_element("Street traffic tag")
                elif (tag1 == "Light flicker" or tag2 == "Light flicker" or tag3 == "Light flicker" or tag4 == "Light flicker" or tag5 == "Light flicker" or tag6 == "Light flicker"):
                        self.click_element("Light flicker tag")
                else:
                    logger.info("No tag selected")
                    logger.info("No tag passed from the resource file")

            self.execute_javascript("window.scrollTo(0, 450)")
            # self.execute_javascript("current_prompt.scrollBy(0,450)")
            time.sleep(self.Utility_obj.SMALL)
        except:
            logger.info('Tag not verified',html=True)
        self.Utility_obj.takescreen()
        return self

    @robot_alias("verify_notes")
    def verify_notes(self,note_info):
        self.click_element("")

# these are all clases importing and utilising in our current library
from robotpageobjects import Page, robot_alias
from robot.api.deco import keyword
from robot.api import logger
from Utility import *
import time

class IncidentsPage(Page):
    """
    This class will verify Incident is present in Incident Management Queue
    """
    # These are all the selectors which are used in the current library
    selectors = {
        "incipages": "xpath=//*[@id='app']/div/div[2]/div/div/div[3]/div[2]/div/button",
        "Menu": "xpath=id('app')/div/div[1]/div[1]/div[2]/div/div[1]/div/button",
        "childmenu": "xpath=//div/p[contains(.,'Incidents')]",
        "toggle": "xpath=id('app')/div/div[2]/div/div/div[1]/div/div/button",
        "cameraid": "xpath=//input[@name='deviceId']",
        "apply": "xpath=//span[contains(.,'Apply')]",
        "incimanage": "xpath=//*[@id='app']/div/div[1]/div[2]/div/div[2]/div[2]/div[3]/span/div/div/div",
        "firstpage": "xpath=//button[contains(.,'1')]",
        "Demo":"xpath=(//p)[4]",
        "False": "xpath=//form/div/div/div[2]/div/div"
    }
    #
    def __init__(self, *args, **kwargs):
        Page.__init__(self)
        self.Utility_obj = Utility()

    @robot_alias("incident__test__page")
    def incident__test__page(self, camera_id, send_Annotation):
        self.click_element("Menu")
        time.sleep(self.Utility_obj.SMALL)
        self.click_element("childmenu")
        self.click_element("toggle")
        self.input_text("cameraid", camera_id)
        self.click_element("apply")
        time.sleep(self.Utility_obj.MEDIUM)
        names = list(self.find_elements("incipages"))
        index= len(names)-2
        size= self.get_text("//*[@id='app']/div/div[2]/div/div/div[3]/div[2]/div/button["+str(index)+"]/div")
        print "Total number of incident pages Camera contians are  "+str(size)
        while (self.Utility_obj.N<=1):
        # size
            if (self.Utility_obj.N==1):
                # size
                print "we reached at last page"
                self.execute_javascript("window.scrollTo(0, 400)")
                time.sleep(self.Utility_obj.MEDIUM)
                self.Utility_obj.takescreen()

            for i in range(1,26):
                if(self.find_element("//table/tbody//tr["+str(i)+"]/td[11]")):
                    self.click_element("//table/tbody//tr["+str(i)+"]/td[11]")
                    time.sleep(self.Utility_obj.SMALL)
                    if(self._is_element_present("//button[@label='Download Clips']")):
                        self.click_element("//button[@label='Download Clips']")
                        print "downding"
                        Anno=list(self.find_elements("//*[@name='annotations']"))
                        time.sleep(self.Utility_obj.SMALL)
                        self.Utility_obj.takescreen()
                        if (self.Utility_obj.ANNOTATION_1==send_Annotation):
                            self.click_element(Anno[1])
                            print "Annotation marked"
                        elif (self.Utility_obj.ANNOTATION_2==send_Annotation):
                            self.click_element(Anno[2])
                            print "Annotation marked"
                        elif (self.Utility_obj.ANNOTATION_3==send_Annotation):
                            self.click_element(Anno[3])
                            print "Annotation marked"
                        else:
                            print "False not visable"
                    else:
                        print "Incident not displaying cant download "
                    self.click_element("//button[.='Cancel']")
                else:
                    print "No Incidents are captured"

            time.sleep(self.Utility_obj.SMALL)
            self.click_element("//*[@id='app']/div/div[2]/div/div/div[3]/div[2]/div/button[" + str(index + 1) + "]/div")
            self.Utility_obj.N = (self.Utility_obj.N + 1)

        return self

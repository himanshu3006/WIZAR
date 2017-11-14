
# Importing classes for utilising current library
from robot.libraries.BuiltIn import BuiltIn
from robot.libraries.Screenshot import Screenshot
import os


class Utility():

    # Declaring and Initializing of Global constants
    SMALL = 5
    MEDIUM = 22
    LARGE = 60
    SIMPLE = 4

    # Global Variables
    INCIDENT = 1
    N = 1
    FLAG = "FALSE"
    FLAG1 = "TRUE"
    ANNOTATION_1 = "False Alarm"
    ANNOTATION_2 = "Correct"
    ANNOTATION_3 = "Missed"
    SIMPLE_WAIT = 4
    def takescreen(self):
        '''
           This functions help us to take screenShot curent page
           :param self:
           :param testcase_id:
           :return:
           '''
        self.testcase_id = BuiltIn().get_variable_value("${testcase_id}")
        results_path = os.path.join(os.getcwd(), "logs" + os.sep +
                                    os.environ["RESULTS_PATH"] + os.sep + "screenshots")

        if not os.path.exists(results_path):
            os.mkdir(results_path)
        else:
            pass
        #creating object of screenshot & passing the path where to store it
        screeobj = Screenshot(results_path)
        screeobj.take_screenshot(self.testcase_id)
        # return self


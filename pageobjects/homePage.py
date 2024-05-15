from selenium.webdriver.common.by import By
from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *
from pageobjects.CheckboxesPage import checkBoxesPageObject

class homePageObject(PageObject):
        
    checkbox_Href = None
    dynamic_controls = None
    heading = None

    def init_page_elements(self):
        try:
            self.checkbox_Href = Link(By.XPATH,"//ul//*[text()='Checkboxes']")
            self.dynamic_controls = Link(By.XPATH,"//ul//*[text()='Dynamic Controls']")
            self.heading = Text(By.XPATH,"//div[@id='content']//h1")
        except:
            self.logger.info("Home Page Init:")
            self.logger.info("checkbox_Href = {}".format(self.checkbox_Href))
            self.logger.info("dynamic_controls = {}".format(self.dynamic_controls))
            self.logger.info("heading = {}".format(self.heading))
            
    def get_element(self, element_name):

        switcher = {
            "checkbox_Href": self.checkbox_Href,
            "dynamic_controls": self.dynamic_controls,
            "heading": self.heading
        }

        el = switcher.get(element_name, None)

        if el is None:
            self.logger.error('Element "{}" is undefined'.format(element_name))
        else:
            return el
        
    def wait_until_elemets_loaded(self):
        """
        This method waits till all of this page's 
        elements are visable
        """
        self.checkbox_Href.wait_until_visible()
        self.dynamic_controls.wait_until_visible()
        return self

    def selectTopic(self, page_object):
        """
        Takes n the page name
        Logs and error if the page object is not found or = null
        returns: self
        """

        if str(page_object) == 'Checkbox':
            self.checkbox_Href.click()
        else:
            self.dynamic_controls.click()

        
        if page_object is None:
            self.logger.error('Element "{}" is undefined'.format(page_object))
        else:
            return page_object
        return self
    
     
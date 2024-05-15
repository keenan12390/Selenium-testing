from selenium.webdriver.common.by import By
from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *
from pageobjects.homePage import homePageObject
from pageobjects.DynamicContent import dynamicPageObject
from pageobjects.CheckboxesPage import checkBoxesPageObject

class genericPageObject(PageObject):

    def init_page_elements(self):
        return

    def open_page(self, page_name):
        """ 
        Open given page url in browser :
        returns: this page object instance 
        """
        self.driver.get('{}'.format(self.config.get(page_name, 'url')))
        
        if page_name is None:
            self.logger.error('Element "{}" is undefined/"None"'.format(page_name))
        else:
            return page_name
        
        return self
    
    def click_element(self, element: PageElement):
        """
        Take in an element
        clicks the element given
        returns self
        """
        temp = element
        temp.click()        
    
        return self
    

    def get_page(self, page_name: str):

        """ Return Page Object

       :returns: this page object instance
       """

        switcher = {
            "Home": homePageObject,
            "Dynamic": dynamicPageObject,
            "Checkboxes": checkBoxesPageObject
        }
        page = switcher.get(page_name, None)
        return page
    
    def set_current_page(self, page_name): 
        """ 
        Takes the given page :
        returns: the page object of the given page name
        """

        currentpage = ""
        if page_name == "Dynamic":
            currentpage = dynamicPageObject()
        elif page_name == "Checkboxes":
            currentpage = checkBoxesPageObject()
        else:
            currentpage = homePageObject()

        if page_name is None:
            self.logger.error('Element "{}" is undefined/"None"'.format(page_name))
        else:
            return currentpage
        
        return currentpage
    
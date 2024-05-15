from selenium.webdriver.common.by import By
from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *
from selenium.common.exceptions import NoSuchElementException
checkbox1 = None
checkbox2 = None
title = None
class checkBoxesPageObject(PageObject):
    def init_page_elements(self):

        try:
            self.checkbox1 = Checkbox(By.XPATH, '//form/input[1]')
            self.checkbox2 = Checkbox(By.XPATH, '//form/input[2]')
            self.checkbox1Visable = Checkbox(By.XPATH, "//form/input[1]//@checked")
            self.checkbox2Visable = Checkbox(By.XPATH, "//form/input[2]//@checked")
            self.title = Text(By.XPATH, "//div[@class='example']//h3")

        except NoSuchElementException:
            self.logger.info("Dynamic Page Init:")
            self.logger.info("checkbox1 = {}".format(self.checkbox1))
            self.logger.info("checkbox2 = {}".format(self.checkbox2))
            self.logger.info("checkbox1Visable = {}".format(self.checkbox1Visable))
            self.logger.info("checkbox2Visable = {}".format(self.checkbox2Visable))
            self.logger.info("title = {}".format(self.title))
        
    def get_element(self, element_name):

        switcher = {
            "checkbox1": self.checkbox1,
            "checkbox2": self.checkbox2,
            "checkbox1Visable": self.checkbox1Visable,
            "checkbox2Visable": self.checkbox2Visable,
            "title": self.title
        }

        el = switcher.get(element_name, None)

        if el is None:
            self.logger.error('Element "{}" is undefined'.format(element_name))
        else:
            return el
        

    def wait_until_elemets_loaded(self):
        self.checkbox1.wait_until_visible()
        self.checkbox2.wait_until_visible()
        self.checkbox1Visable.wait_until_visible()
        self.checkbox2Visable.wait_until_visible()
        self.title.wait_until_visible()
        return self

    def clickCheckbox(self, button):
        if button == "first":
            self.checkbox1.click()
        else:
            self.checkbox2.click()
        return self
    
    def getTitle(self):
        temp = self.title.text
        return temp

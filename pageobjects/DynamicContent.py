
from selenium.webdriver.common.by import By
from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *
from pageobjects.CheckboxesPage import checkBoxesPageObject

class dynamicPageObject(PageObject):

    inputfield = None
    btnDiable = None
    btnEnable = None
    btnRemove = None
    message = None
    title = None

    def init_page_elements(self):
        try:
            self.inputfield = InputText(By.XPATH, "//form/input[@type='text']")
            self.btnDisable = Button(By.XPATH, '{}'.format(self.config.get('Dynamic', 'button')))
            self.btnEnable = Button(By.XPATH, '{}'.format(self.config.get('Dynamic', 'button')))
            self.btnRemove = Button(By.XPATH, '//*[@id="checkbox-example"]/button')
            self.message = Text(By.XPATH,"//p[@id='message']")
            self.title = Text(By.XPATH, "//div[@class='example']//h4")

        except:
            self.logger.info("Dynamic Page Init:")
            self.logger.info("inputfield = {}".format(self.inputfield))
            self.logger.info("btnDisable = {}".format(self.btnDisable))
            self.logger.info("btnEnable = {}".format(self.btnEnable))
            self.logger.info("btnRemove = {}".format(self.btnRemove))
            self.logger.info("message = {}".format(self.message))
            self.logger.info("title = {}".format(self.title))


    def get_element(self, element_name):

        switcher = {
            "inputfield": self.inputfield,
            "btnDisable": self.btnDisable,
            "btnEnable": self.btnEnable,
            "disable": self.btnDisable,
            "enable": self.btnEnable,
            "message": self.message,
            "remove": self.btnRemove
        }

        el = switcher.get(element_name, None)

        if el is None:
            self.logger.error('Element "{}" is undefined'.format(element_name))
        else:
            return el
        
    def wait_until_loaded(self):
        """
        Waits until all elements are loaded
        """
        self.inputfield.wait_until_visible() 

        return self
    
    
    def btn_click(self, btnName):
        """
        Takes in a button name

        :clicks the button

        returns: self
        """
        try:
            if btnName == 'enable':
                self.logger.info("Attempting to click the {}".format(btnName)) 
                self.btnEnable.click()
                self.logger.info("clicked the {} element".format(btnName))
            else:
                self.logger.info("Attempting to click the {}".format(btnName)) 
                self.btnDisable.click()
                self.logger.info("clicked the {} element".format(btnName))
        except:
            print()

        return self
    
        
    
    def input_message_into_feild(self,message):
        """
        Takes in a message:
        Inserts the message into the input feild

        returns: self
        """
        self.inputfield.text = message 

        return self
    
    def check_validation_message(self, exspected_value):
        """
        Validates the exspected value
        is equal to what we exspect
        """
        actual = self.message.text
        exspected1 = "It's enabled!"
        exspected2 = "It's disabled!"
        if exspected_value == 'enable':
            assert actual == exspected1,"The exspected text lable value is not the same as the actual"
        else:
            assert actual == exspected2,"The exspected text lable value is not the same as the actual"

        return self
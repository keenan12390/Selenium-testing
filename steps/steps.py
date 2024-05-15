from behave import given, when, then
from selenium.webdriver.common.by import By
from pageobjects.homePage import homePageObject
from pageobjects.DynamicContent import dynamicPageObject
from pageobjects.CheckboxesPage import checkBoxesPageObject
from pageobjects.GenericMethods import genericPageObject

def get_element(page_name, element_name):
    el = None
    if page_name == "home":
        el = homePageObject().get_element(element_name)
    if page_name == "Checkboxes":
        el = checkBoxesPageObject().get_element(element_name)
    if page_name == "Dynamic":
        el = dynamicPageObject().get_element(element_name)

    return el

@given('the user is on the "{home}" page')
def step_impl(context, home):
    context.current_page = genericPageObject()
    context.current_page.open_page(home)
    context.current_page = context.current_page.set_current_page(home)
# asserts
    """
    asserting that the heading we get is what we exspect to see
    """ 
    actual = context.current_page.heading.text
    exspected = "Welcome to the-internet"
    assert actual == exspected, "We are on the wrong page"

@when('the user clicks the "{checkbox}" link')
def step_impl(context, checkbox):
    context.current_page = homePageObject()
    context.current_page.wait_until_elemets_loaded()
    context.current_page.selectTopic(checkbox)
    
# asserts
    assert "The Internet" in context.current_page.driver.title
    

@then('the "{checkboxes}" page opens and the user clicks the "{button}" Checkbox at the top')
def step_impl(context, checkboxes: str, button: str):
    context.current_page = genericPageObject()

    element = get_element(checkboxes, button)
    
    context.current_page.click_element(element)

# asserts
    """
    Checking that the title of the current page we take in
    is what we exspect
    &
    assert that the button taken in was pressed by checking
    if the unchecked state of the button is present
    """

    context.current_page = context.current_page.set_current_page(checkboxes)
    actualValue = context.current_page.title
    actualValue = actualValue.text

    switcher = {
            "Home": "Home",
            "Dynamic": "Dynamic Controls",
            "Checkboxes": "Checkboxes"
        }
    exspected = switcher.get(checkboxes, None)

    assert "The Internet" in context.current_page.driver.title
    assert str(exspected) == str(actualValue),"null, We are on the wrong page"



"""
###Feature 2###
"""

@given('the user is on the "{dynamic}" page clicks the "{button}" button')
def step_impl(context, dynamic, button ):
    """
    Opening the page based off the page you are taking in
    &
    Waiting until the input feild is able to accept text
    Based off wheather you can click it.
    Checks that the message that pops up when the button is clicked, state changes    
    """
    ##reuse steps                                                                                                                                                        
    context.execute_steps(
    '''Given the user is on the "Home" page
     When the user clicks the "Dynamic" link
     Then the "Dynamic" page opens and the user clicks the "remove" Checkbox at the top
     '''
    )
    context.current_page = genericPageObject()
    context.current_page.open_page(dynamic)
    
    element = get_element(dynamic, button)
    context.current_page.click_element(element)
    
    context.current_page = context.current_page.set_current_page(dynamic)
    
    context.current_page.inputfield.wait_until_clickable()

    context.current_page.check_validation_message(button)


@when('the user puts in "{message}" and clicks the "{button}" button')
def step_impl(context, message, button):
    message = message

    context.current_page = context.current_page.input_message_into_feild(message)

    context.current_page = genericPageObject()
    element = get_element("Dynamic", button)
    context.current_page.click_element(element) 

    assert "The Internet" in context.current_page.driver.title
    

@then('the user should be on the "{dynamic}" page and they cannot edit the text anymore')
def step_impl(context, dynamic):
    context.current_page = genericPageObject()
    context.current_page =  context.current_page.set_current_page(dynamic)
    context.current_page.check_validation_message('disable')
    
    assert "The Internet" in context.current_page.driver.title

Feature: selectTopic

  Scenario: Selecting the next page
  As a user I want to be able to navigate 
  to a specific page when im on the Home page

    Given the user is on the "Home" page
     When the user clicks the "Checkbox" link
     Then the "Checkboxes" page opens and the user clicks the "checkbox2" Checkbox at the top


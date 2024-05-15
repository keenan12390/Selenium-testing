Feature: The disable button should make my text uneditable

  Scenario: Disabling the user text
   As a user i want my detials 
   i fill into the text feild
   to be safe from others editing it
    Given the user is on the "Dynamic" page clicks the "enable" button 
     When the user puts in "message" and clicks the "disable" button 
     Then the user should be on the "Dynamic" page and they cannot edit the text anymore
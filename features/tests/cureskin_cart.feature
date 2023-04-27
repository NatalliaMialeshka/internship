# Created by belar at 4/27/2023
Feature: CureSkin cart tests

  Scenario: Update Cart functionality
    Given Open CURESKIN main page
    #When Close pop up window
    When Click on search icon
    When Input text SPF
    When Click on first product
    When Add product to the cart
    When Open Cart from product page
    When Reduce the quantity of the product to 0
    Then Verify the product is removed from cart
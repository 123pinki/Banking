
Feature: deposit money
  Scenario: deposit money in account

    When I click on banking
    And Click on customer login
    And Select name
    And Click on login
    And Select account number

    And Select the Deposit
    And Enter the amount 10000
    And Click on deposit/withdraw
    And Click on logout
    And Go to the home page

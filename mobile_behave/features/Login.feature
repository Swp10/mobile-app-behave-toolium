Feature:  As an existing user, I would like to login


  Scenario: With valid credential, I can login to account
    Given I select test environment
    When I am on Login page
    And I login to account
    Then I shall land on dashboard

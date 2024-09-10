@reported_test
Feature: Test Scenarios for Filter functionality

  Scenario: User can filter by sale status Future Launch.
    Given Open the main page.
    When Log in to the page.
    Then Verify the right page opens.
    And Filter by sale status of “Future Launch”.
    And Verify each product contains the Future Launch tag.
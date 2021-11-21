Feature: Retirement Age Calculator

    Scenario: User wants to calculate retirement age
        Given User inputs a valid year and valid month
        When User inputs year 1950 and month 11
        Then the calculator should return year 2016 and month 11
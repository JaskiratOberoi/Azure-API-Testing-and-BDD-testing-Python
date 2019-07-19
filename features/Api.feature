Feature: Test GET request
    Scenario: StatusValidation
        Given we have a valid url
        When data is gathered from the API
        Then we should receive response code 200
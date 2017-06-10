@Register
Feature: Register to system
    people can register to system, providing their email (as the unique user id) and password.

    Background:
        Given There are following patients in the system:
            | email          | password         | first name | last name  | gender | birth date | mobile     | address              | emergency contact number | emergency contact person |
            | bi@snzh.org.nz | LittleIssue@1234 | Big        | Issue      | Male   | 01/03/1950 | 0210230235 | Some where, Auckland | 0210230234               | Little Issue             |
        And There are following doctors in the system:
            | email          | password         | first name | last name  | gender | mobile     |
            | nd@snzh.org.nz | NiceDoctors@1234 | Nice       | Doctor     | Male   | 0210230986 |

    @Positive
    Scenario: register as patient succesfully with enough correct information
        When I register as patient with the following information:
            | email          | password         | first name | last name  | gender | birth date | mobile     | address              |emergency contact number | emergency contact person |
            | ln@snzh.org.nz | LittleIssue@1234 | Little     | Issue      | Male   | 01/03/1970 | 0210230234 | Nowhere, Auckland    | 0210230235              | Big Issue                |
        Then Register successful page should show.


    @Negative
    Scenario: cannot register existing patient
        When I register as patient with the following information:
            | email          | password         | first name | last name  | gender | birth date | mobile     | address              | emergency contact number | emergency contact person |
            | bi@snzh.org.nz | LittleIssue@1234 | Big        | Issue      | Male   | 01/03/1950 | 0210230235 | Some where, Auckland | 0210230234               | Little Issue             |
        Then An register fail message should be displayed.

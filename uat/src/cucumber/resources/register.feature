@Register
Feature: Register to system
    people can register to system, providing their email (as the unique user id) and password.

    Background:
        Given There are following users in the system:
            | user name | email                        | password        | user type |
            | Admin A   | admin@smartnzhealth.co.nz    | P@ssw0rd        | Admin     |
            | Doctor D  | doctor1@smartnzhealth.co.nz  | doctor1@UNITEC  | Doctor    |
            | Patient A | patient1@smartnzhealth.co.nz | patient1@UNITEC | Patient   |
            | Patient B | patient2@smartnzhealth.co.nz | patient2@UNITEC | Patient   |

    @Positive
    Scenario: register as patient succesfully with enough correct information
        When I register with the following information:
            | email          | password         | first name | last name  | gender | birth date | mobile     | emergency contact number | emergency contact person |
            | ln@snzh.org.nz | LittleIssue@1234 | Little     | Issue      | Male   | 01/03/1970 | 0210230234 | 02101110111              | Big Issue                |
        Then Register successful page should show.


    @Negative
    Scenario: cannot register existing user
        When I register with the following information:
            | email                        | password         | first name | last name  | gender | birth date | mobile     | emergency contact number | emergency contact person |
            | patient1@smartnzhealth.co.nz | LittleIssue@1234 | Little     | Issue      | Male   | 01/03/1970 | 0210230234 | 02101110111              | Big Issue                |
        Then An register fail message should be displayed.

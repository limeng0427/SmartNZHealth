@Register
Feature: Register to system
    people can register to system, providing their email (as the unique user id) and password.

    Background:
        Given There are following users in the system:
            | user name      | email          | password         | user type |
            | Great Doctor   | gd@snzh.org.nz | Abcd@1234        | doctor    |
            | Little Issue   | li@snzh.org.nz | LittleIssue@1234 | patient   |

    @Positive
    Scenario Outline: register succesfully with correct user and password
        When I register with email "<email>", password "<password>" and confirming password "<confirmPassword>"
        Then Register successful page should show.

        Examples:
            | user name      | email          | password         | user type | confirmPassword  |
            | Awesome Admin  | aa@snzh.org.nz | aswesome@        | adin      | aswesome@        |
            | Lazy Nobody    | ln@snzh.org.nz | LittleIssue@1234 | patient   | LittleIssue@1234 |

    @Negative
    Scenario: cannot register existing user
            When I register with email "gd@snzh.org.nz", password "Abcd@1234" and confirming password "Abcd@1234"
            Then An register fail message should be displayed.

    @Negative
    Scenario: cannot register if password does not match confirming password
            When I register with email "new@snzh.org.nz", password "Abcd@1234" and confirming password "notTheSame"
            Then An register fail message should be displayed.

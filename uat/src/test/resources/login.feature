Feature: Login to system
    There are three types of users: doctors, patients and admins. All of them need to login to the system to be able to use it.
To login, you need an account id and a password. Account id is in the form of valid eamil address.
    If correct password is supplied, the user should be redirected to his/her profile page. If incorrect password is supplied, the user should be shown an error message.

    Background:
        Given There are following users in the system:
            | user name      | email          | password         | user type |
            | Unknown User   | 1@1.com        | Abcd@1234        | patient   |
            | Little Issue   | li@snzh.org.nz | LittleIssue@1234 | patient   |
        And Login page is opened in browser.

    Scenario Outline: login succesfully with correct user and password
        When In input "Email" <email> is entered.
        And In input "Password" <password> is entered.
        And Button "Log in" is clicked.
        Then The profile of user <email> of type <user type> should be displayed.

        Examples:
            | user name      | email          | password         | user type |
            | Unknown User   | 1@1.com        | Abcd@1234        | patient   |
            | Little Issue   | li@snzh.org.nz | LittleIssue@1234 | patient   |

    Scenario: cannot login with incorrect password
        When In input "Email" 1@1.com is entered.
        And In input "Password" Wrong@5678 is entered.
        And Button "Log in" is clicked.
        Then An login fail message should be displayed.

    Scenario: cannot login with inexistent user
        When In input "Email" no_such_user@snzh.org.nz is entered.
        And In input "Password" "li123" is entered.
        And Button "Log in" is clicked.
        Then An login fail message should be displayed.
#

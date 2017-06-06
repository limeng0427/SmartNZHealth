Feature: Login to system
    There are three types of users: doctors, patients and admins. All of them need to login to the system to be able to use it.
To login, you need an account id and a password. Account id is in the form of valid eamil address.
    If correct password is supplied, the user should be redirected to his/her profile page. If incorrect password is supplied, the user should be shown an error message.

    Background:
        Given There are following users in the system:
            | user name      | email          | password         | user type |
            | Great Doctor   | gd@snzh.org.nz | Abcd@1234        | doctor    |
            | Little Issue   | li@snzh.org.nz | LittleIssue@1234 | patient   |

    Scenario Outline: login succesfully with correct user and password
        When I login with email "<email>" and password "<password>"
        Then all the current users should show.

        Examples:
            | user name      | email          | password         | user type |
            | Great Doctor   | gd@snzh.org.nz | Abcd@1234        | doctor    |
            | Little Issue   | li@snzh.org.nz | LittleIssue@1234 | patient   |

    Scenario: cannot login with wrong password
            When I login with email "gd@snzh.org.nz" and password "wrong_password"
            Then An login fail message should be displayed.

    Scenario: cannot login with inexistent user
            When I login with email "no_such_user@nznh.com" and password "any"
            Then An login fail message should be displayed.

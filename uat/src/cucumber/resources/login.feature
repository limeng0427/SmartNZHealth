@Login
Feature: Login to system
    There are three types of users: doctors, patients and admins. All of them need to login to the system to be able to use it.
To login, you need an account id and a password. Account id is in the form of valid eamil address.
    If correct password is supplied, the user should be redirected to his/her profile page. If incorrect password is supplied, the user should be shown an error message.

     Background:
        Given There are following patients in the system:
            | email          | password         | first name | last name  | gender | birth date | mobile     | address              | emergency contact number | emergency contact person |
            | bi@snzh.org.nz | LittleIssue@1234 | Big        | Issue      | Male   | 01/03/1950 | 0210230235 | Some where, Auckland | 0210230234               | Little Issue             |
        And There are following doctors in the system:
            | email          | password         | first name | last name  | gender | mobile     |
            | nd@snzh.org.nz | NiceDoctors@1234 | Nice       | Doctor     | Male   | 0210230986 |

    @Positive
    Scenario Outline: login succesfully with correct user and password
        When I login with email "<email>" and password "<password>"
        Then I should see a login greeting as "Welcome  <email>".
        Examples:
            | email          | password         |
            | ln@snzh.org.nz | LittleIssue@1234 |

    @Negative
    Scenario: cannot login with wrong password
            When I login with email "ln@snzh.org.nz" and password "wrong_password"
            Then An login fail message should be displayed.

    @Negative
    Scenario: cannot login with inexistent user
            When I login with email "no_such_user@nznh.com" and password "P@ssw0rd"
            Then An login fail message should be displayed.

    @New
    Scenario: cannot login with disabled account
            When I login with email "doctor1@smartnzhealth.co.nz" and password "doctor1@UNITEC"
            Then An accoutnt disable message should be displayed.

@Login
Feature: Login to system
    There are three types of users: doctors, patients and admins. All of them need to login to the system to be able to use it.
To login, you need an account id and a password. Account id is in the form of valid eamil address.
    If correct password is supplied, the user should be redirected to his/her profile page. If incorrect password is supplied, the user should be shown an error message.

    Background:
        Given There are following users in the system:
            | user name | email                        | password        | user type |
            | Admin A   | admin@smartnzhealth.co.nz    | P@ssw0rd        | Admin     |
            | Doctor D  | doctor1@smartnzhealth.co.nz  | doctor1@UNITEC  | Doctor    |
            | Patient A | patient1@smartnzhealth.co.nz | patient1@UNITEC | Patient   |
            | Patient B | patient2@smartnzhealth.co.nz | patient2@UNITEC | Patient   |

    @Positive
    Scenario Outline: login succesfully with correct user and password
        When I login with email "<email>" and password "<password>"
        Then I should see a login greeting as "Hello <email>!".
        Examples:
            | user name | email                        | password        | user type |
            | Admin A   | admin@smartnzhealth.co.nz    | P@ssw0rd        | Admin     |
            | Patient A | patient1@smartnzhealth.co.nz | patient1@UNITEC | Patient   |
            | Patient B | patient2@smartnzhealth.co.nz | patient2@UNITEC | Patient   |

    @Negative
    Scenario: cannot login with wrong password
            When I login with email "admin@smartnzhealth.co.nz" and password "wrong_password"
            Then An login fail message should be displayed.

    @Negative
    Scenario: cannot login with inexistent user
            When I login with email "no_such_user@nznh.com" and password "P@ssw0rd"
            Then An login fail message should be displayed.

    @New
    Scenario: cannot login with disabled account
            When I login with email "doctor1@smartnzhealth.co.nz" and password "doctor1@UNITEC"
            Then An accoutnt disable message should be displayed.

package steps;

import cucumber.api.DataTable;
import cucumber.api.java.en.Given;
import domain.RegisterInfo;
import service.DBUserDAO;
import service.UserService;

public class PredefinedUserSteps {
    @Given("^There are following users in the system:$")
    public void thereAreFollowingUsersInTheSystem(DataTable arg1) throws Throwable {
        UserService userService = new UserService(new DBUserDAO());

        RegisterInfo user1 = new RegisterInfo();
        user1.setEmail("gd@snzh.org.nz");
        user1.setPassword("Abcd@1234");
        user1.setConfirmPassword(user1.getPassword());

        userService.register(user1);

        RegisterInfo user2 = new RegisterInfo();
        user2.setEmail("li@snzh.org.nz");
        user2.setPassword("LittleIssue@1234");
        user2.setConfirmPassword(user2.getPassword());

        userService.register(user2);
    }

}

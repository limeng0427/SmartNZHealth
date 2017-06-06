package hooks;

import org.openqa.selenium.OutputType;
import org.openqa.selenium.WebDriverException;

import cucumber.api.Scenario;
import cucumber.api.java.After;
import cucumber.api.java.Before;
import service.DBUserDAO;
import service.UserService;
import support.KnowsTheDomain;

public class DBHooks {
    @Before
    public void reset() {
        UserService userService = new UserService(new DBUserDAO());
        userService.deleteAllUsers();
    }

}

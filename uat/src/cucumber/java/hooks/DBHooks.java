package hooks;

import cucumber.api.java.Before;
import service.DBUserDAO;
import service.UserService;

public class DBHooks {
    @Before
    public void reset() {
//        UserService userService = new UserService(new DBUserDAO());
//        userService.deleteAllUsers();
    }

}

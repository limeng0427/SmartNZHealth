package hooks;

import cucumber.api.java.Before;
import service.InMemoryUserDAO;
import service.UserService;

public class DBHooks {
    @Before
    public void reset() {
    }

}

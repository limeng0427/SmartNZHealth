package steps;

import org.openqa.selenium.By;
import org.openqa.selenium.support.events.EventFiringWebDriver;
import cucumber.api.java.en.Then;
import cucumber.api.java.en.When;
import pages.LoginPage;
import support.KnowsTheDomain;

import static org.junit.Assert.*;

public class LoginSteps {
    KnowsTheDomain helper;
    private final EventFiringWebDriver webDriver;
    private LoginPage loginPage;

    public LoginSteps(KnowsTheDomain helper) {
        System.setProperty("webdriver.gecko.driver",
                "C:\\ws\\SeleniumCookbook\\geckodriver.exe");
        webDriver = helper.getWebDriver();
        loginPage = new LoginPage(webDriver);
    }

    @Then("^The profile of user (.*) of type (.*) should be displayed\\.$")
    public void theProfileOfUserOfTypeShouldBeDisplayed(String email,
            String userType) throws Throwable {
    }

    @Then("^An login fail message should be displayed\\.$")
    public void anLoginFailMessageShouldBeDisplayed() throws Throwable {
        assertTrue(loginPage.errorMessageExists());
    }

    @When("^I login with email \"(.*?)\" and password \"(.*?)\"$")
    public void i_login_with_email_and_password(String email, String password) throws Throwable {
        loginPage.login(email, password);
    }

    @Then("^all the current users should show\\.$")
    public void all_the_current_users_should_show() throws Throwable {
        // Write code here that turns the phrase above into concrete actions
        assertTrue(loginPage.allUsersPageShows());
    }



}

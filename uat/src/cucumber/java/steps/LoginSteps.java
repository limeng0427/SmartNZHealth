package steps;

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

    @Then("^An login fail message should be displayed\\.$")
    public void anLoginFailMessageShouldBeDisplayed() throws Throwable {
        assertTrue(loginPage.errorMessageExists());
    }

    @When("^I login with email \"(.*?)\" and password \"(.*?)\"$")
    public void i_login_with_email_and_password(String email, String password) throws Throwable {
        loginPage.login(email, password);
    }

    @Then("^I should see a login greeting as \"(.*?)\"\\.$")
    public void i_should_see_a_login_greeting_as(String greetings) throws Throwable {
        assertTrue("Cannot find greeting: " + greetings, loginPage.greetingMessageIsDisplayed(greetings));
    }

    @Then("^An accoutnt disable message should be displayed\\.$")
    public void an_accoutnt_disable_message_should_be_displayed() throws Throwable {
        // Write code here that turns the phrase above into concrete actions
        assertTrue(loginPage.errorMessageExists());
    }

}

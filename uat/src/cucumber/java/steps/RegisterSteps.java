package steps;

import org.openqa.selenium.support.events.EventFiringWebDriver;
import cucumber.api.java.en.Then;
import cucumber.api.java.en.When;
import pages.RegisterPage;
import support.KnowsTheDomain;

import static org.junit.Assert.*;

public class RegisterSteps {
    KnowsTheDomain helper;
    private final EventFiringWebDriver webDriver;
    private RegisterPage registerPage;

    public RegisterSteps(KnowsTheDomain helper) {
        webDriver = helper.getWebDriver();
        registerPage = new RegisterPage(webDriver);
    }

    @Then("^An register fail message should be displayed\\.$")
    public void an_register_fail_message_should_be_displayed() throws Throwable {
        assertTrue(registerPage.errorMessageExists());
    }

    @When("^I register with email \"(.*?)\", password \"(.*?)\" and confirming password \"(.*?)\"$")

    public void i_register_with_email_password_and_confirming_password(String email, String password, String confirmPassword) throws Throwable {
        registerPage.register(email, password, confirmPassword);
    }

    @Then("^Register successful page should show\\.$")
    public void register_successful_page_should_show() throws Throwable {
        // Write code here that turns the phrase above into concrete actions
        assertTrue(registerPage.registerSucceeds());
    }

}

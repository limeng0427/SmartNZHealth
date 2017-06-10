package steps;

import org.openqa.selenium.support.events.EventFiringWebDriver;

import cucumber.api.DataTable;
import cucumber.api.java.en.Given;
import cucumber.api.java.en.Then;
import cucumber.api.java.en.When;
import domain.PatientRegisterInfo;
import pages.PatientRegisterPage;
import support.KnowsTheDomain;

import static org.junit.Assert.*;

import java.util.List;

public class RegisterSteps {
    KnowsTheDomain helper;
    private final EventFiringWebDriver webDriver;
    private PatientRegisterPage registerPage;

    public RegisterSteps(KnowsTheDomain helper) {
        webDriver = helper.getWebDriver();
        registerPage = new PatientRegisterPage(webDriver);
    }

    @Then("^An register fail message should be displayed\\.$")
    public void an_register_fail_message_should_be_displayed() throws Throwable {
        assertTrue(registerPage.errorMessageExists());
    }

    @Then("^Register successful page should show\\.$")
    public void register_successful_page_should_show() throws Throwable {
        // Write code here that turns the phrase above into concrete actions
        assertTrue(registerPage.registerSucceeds());
    }

    @When("^I register as patient with the following information:$")
    public void i_register_with_the_following_information(DataTable registerInfoTable) throws Throwable {
        PatientRegisterInfo registerInfo = getRegisterInfoFromStringList(registerInfoTable.raw().get(1));

        registerPage.register(registerInfo);
    }

    private PatientRegisterInfo getRegisterInfoFromStringList(List<String> list) {
        return new PatientRegisterInfo(list.get(0), // email
                                list.get(1), // password
                                list.get(1), // confirm password
                                list.get(2), // frist name
                                list.get(3), // last name
                                list.get(4), // gender
                                list.get(5), // birth date
                                list.get(6), // mobile
                                list.get(7), // address
                                list.get(8), // emergency contact number
                                list.get(9)); // emergency contact person
    }

    @Given("^There are following doctors in the system:$")
    public void there_are_following_doctors_in_the_system(DataTable arg1) throws Throwable {

    }


}

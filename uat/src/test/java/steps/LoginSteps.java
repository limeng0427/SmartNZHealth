package steps;

import org.openqa.selenium.By;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.events.EventFiringWebDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import cucumber.api.java.en.Given;
import cucumber.api.java.en.Then;
import cucumber.api.java.en.When;
import support.KnowsTheDomain;

public class LoginSteps {
    KnowsTheDomain helper;
    private final EventFiringWebDriver webDriver;

    public LoginSteps(KnowsTheDomain helper) {
        System.setProperty("webdriver.gecko.driver",
                "C:\\ws\\SeleniumCookbook\\geckodriver.exe");
        webDriver = helper.getWebDriver();
    }

    @Given("^Login page is opened in browser\\.$")
    public void loginPageIsOpenedInBrowser() throws Throwable {
        webDriver.get("http://localhost:51184/Account/Login");
    }

    @When("^In input \"Email\" (.+@.+) is entered\\.$")
    public void inInputEmailAccountIdIsEntered(String email) throws Throwable {
        System.out.println("email: "  + email);
        webDriver.findElement(By.id("Email")).sendKeys(email);
    }

    @When("^In input \"Password\" (.*) is entered\\.$")
    public void inInputPasswordPasswordIsEntered(String password) throws Throwable {
        System.out.println("password: "  + password);
        webDriver.findElement(By.id("Password")).sendKeys(password);
    }

    @When("^Button \"Log in\" is clicked\\.$")
    public void buttonLoginIsClicked() throws Throwable {
        webDriver.findElement(By.id("Password")).submit();
    }

    @Then("^The profile of user (.*) of type (.*) should be displayed\\.$")
    public void theProfileOfUserOfTypeShouldBeDisplayed(String email, String userType) throws Throwable {
        WebDriverWait wait = new WebDriverWait(webDriver, 5);
        wait.until(ExpectedConditions.presenceOfElementLocated(By.linkText("Hello " + email + "!")));
    }

    @Then("^An login fail message should be displayed\\.$")
    public void anLoginFailMessageShouldBeDisplayed() throws Throwable {
        WebDriverWait wait = new WebDriverWait(webDriver, 5);
        wait.until(ExpectedConditions.presenceOfElementLocated(By.className("validation-summary-errors")));
    }



}

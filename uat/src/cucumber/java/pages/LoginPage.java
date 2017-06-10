package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.TimeoutException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import static org.junit.Assert.*;

public class LoginPage {
    @FindBy(id = "Email")
    public WebElement emailElement;

    @FindBy(id = "Password")
    public WebElement passwordElement;

    private final WebDriver driver;

    public LoginPage(WebDriver driver) {
        this.driver = driver;
        PageFactory.initElements(driver, this);
    }

    public void login(String email, String password) {
        driver.get("http://127.0.0.1:15133/userprofile/login/");
        emailElement.sendKeys(email);
        passwordElement.sendKeys(password);
        passwordElement.submit();
    }

    public boolean errorMessageExists() {
        WebDriverWait wait = new WebDriverWait(driver, 5);
        try {
            assertEquals("Invalid username or password",
                    wait.until(ExpectedConditions.visibilityOfElementLocated(By.className("error"))).getText()
                    );
            return true;
        } catch (TimeoutException e) {
            return false;
        }
    }

    public boolean greetingMessageIsDisplayed(String gteetings) {
        WebDriverWait wait = new WebDriverWait(driver, 5);
        try {
            wait.until(ExpectedConditions.visibilityOfElementLocated(By.linkText(gteetings)));
            return true;
        } catch (TimeoutException e) {
            return false;
        }
    }
}

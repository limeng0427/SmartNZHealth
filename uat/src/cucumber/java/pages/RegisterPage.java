package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.TimeoutException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class RegisterPage {
    @FindBy(id = "email")
    public WebElement emailElement;

    @FindBy(id = "password")
    public WebElement passwordElement;

    @FindBy(id = "confirmPassword")
    public WebElement confirmPasswordElement;

    private final WebDriver driver;

    public RegisterPage(WebDriver driver) {
        this.driver = driver;
        PageFactory.initElements(driver, this);
    }

    public void register(String email, String password, String confirmPassword) {
        driver.get("http://localhost:8080/cloudproject/register");
        emailElement.sendKeys(email);
        passwordElement.sendKeys(password);
        confirmPasswordElement.sendKeys(confirmPassword);
        passwordElement.submit();
    }

    public boolean errorMessageExists() {
        WebDriverWait wait = new WebDriverWait(driver, 5);
        try {
            wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("register_error")));
            return true;
        } catch (TimeoutException e) {
            return false;
        }
    }

    public boolean registerSucceeds() {
        WebDriverWait wait = new WebDriverWait(driver, 5);
        try {
            wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("register_successful_message")));
            return true;
        } catch (TimeoutException e) {
            return false;
        }
    }
}

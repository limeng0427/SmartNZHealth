package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.TimeoutException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

public class LoginPage {
    @FindBy(id = "email")
    public WebElement emailElement;

    @FindBy(id = "password")
    public WebElement passwordElement;

    private final WebDriver driver;

    public LoginPage(WebDriver driver) {
        this.driver = driver;
        PageFactory.initElements(driver, this);
    }

    public void login(String email, String password) {
        driver.get("http://localhost:8080/cloudproject/login");
        emailElement.sendKeys(email);
        passwordElement.sendKeys(password);
        passwordElement.submit();
    }

    public boolean errorMessageExists() {
        WebDriverWait wait = new WebDriverWait(driver, 5);
        try {
            wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("error")));
            return true;
        } catch (TimeoutException e) {
            return false;
        }
    }

    public boolean allUsersPageShows() {
        WebDriverWait wait = new WebDriverWait(driver, 5);
        try {
            wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("all_users_table")));
            return true;
        } catch (TimeoutException e) {
            return false;
        }
    }
}

package pages;

import org.openqa.selenium.By;
import org.openqa.selenium.TimeoutException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.Select;
import org.openqa.selenium.support.ui.WebDriverWait;

import domain.PatientRegisterInfo;

public class PatientRegisterPage {
    @FindBy(id = "Email")
    public WebElement emailElement;

    @FindBy(id = "Password")
    public WebElement passwordElement;

    @FindBy(id = "ConfirmPassword")
    public WebElement confirmPasswordElement;

    @FindBy(id = "FirstName")
    public WebElement firstNameElement;

    @FindBy(id = "LastName")
    public WebElement lastNameElement;

    @FindBy(id = "Gender")
    public WebElement genderElement;

    @FindBy(id = "Birthday")
    public WebElement birthDateElement;

    @FindBy(id = "Mobile")
    public WebElement mobileElement;

    @FindBy(id = "Address")
    public WebElement addressElement;

    @FindBy(id = "EmergencyContactName")
    public WebElement emergencyContactNameElement;

    @FindBy(id = "EmergencyContactPhone")
    public WebElement emergencyContactPhoneElement;

    private final WebDriver driver;

    public PatientRegisterPage(WebDriver driver) {
        this.driver = driver;
        PageFactory.initElements(driver, this);
    }

    public boolean errorMessageExists() {
        WebDriverWait wait = new WebDriverWait(driver, 5);
        try {
            wait.until(ExpectedConditions.visibilityOfElementLocated(By.className("error")));
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

    public void register(PatientRegisterInfo registerInfo) {
        driver.get("http://127.0.0.1:15133/userprofile/register_patient/");

        emailElement.clear();
        emailElement.sendKeys(registerInfo.getEmail());

        passwordElement.clear();
        passwordElement.sendKeys(registerInfo.getPassword());

        confirmPasswordElement.clear();
        confirmPasswordElement.sendKeys(registerInfo.getConfirmPassword());

        firstNameElement.clear();
        firstNameElement.sendKeys(registerInfo.getFirstName());

        lastNameElement.clear();
        lastNameElement.sendKeys(registerInfo.getLastName());

        new Select(genderElement).selectByVisibleText(registerInfo.getGender());

        birthDateElement.clear();
        birthDateElement.sendKeys(registerInfo.getBirthDate());

        mobileElement.clear();
        mobileElement.sendKeys(registerInfo.getMobile());

        addressElement.clear();
        addressElement.sendKeys(registerInfo.getAddress());

        emergencyContactNameElement.clear();
        emergencyContactNameElement.sendKeys(registerInfo.getEmergencyContactPerson());

        emergencyContactPhoneElement.clear();
        emergencyContactPhoneElement.sendKeys(registerInfo.getEmergencyContactNumber());


        passwordElement.submit();
    }
}

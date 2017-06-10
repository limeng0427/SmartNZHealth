package support;

import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.events.EventFiringWebDriver;

public class KnowsTheDomain {
    private EventFiringWebDriver webDriver;

    public EventFiringWebDriver getWebDriver() {
        if (webDriver == null) {
            System.setProperty("webdriver.gecko.driver",
                    "src\\selenium\\geckodriver-v0.16.1-win32\\geckodriver.exe");
            // C:\\Users\\stephenhu\\Source\\Repos\\SmartNZHealth\\uat\\
           webDriver = new EventFiringWebDriver(new FirefoxDriver());
           webDriver.manage().window().maximize();
        }
        return webDriver;
    }
}

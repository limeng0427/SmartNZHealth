package support;

import java.util.concurrent.TimeUnit;

import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.events.EventFiringWebDriver;

public class KnowsTheDomain {
    private EventFiringWebDriver webDriver;

    public EventFiringWebDriver getWebDriver() {
        if (webDriver == null) {
            System.setProperty("webdriver.gecko.driver",
                    "C:\\ws\\SeleniumCookbook\\geckodriver.exe");
           webDriver = new EventFiringWebDriver(new FirefoxDriver());
           webDriver.manage().window().maximize();
        }
        return webDriver;
    }
}

package hooks;

import org.openqa.selenium.OutputType;
import org.openqa.selenium.WebDriverException;

import cucumber.api.Scenario;
import cucumber.api.java.After;
import support.KnowsTheDomain;

public class WebDriverHooks {
    private KnowsTheDomain helper;

    public WebDriverHooks(KnowsTheDomain helper) {
        this.helper = helper;
    }

    @After
    public void finish(Scenario scenario) {
        try {
            byte[] screenshot =
                    helper.getWebDriver().getScreenshotAs(OutputType.BYTES);
            scenario.embed(screenshot, "image/png");
        } catch (WebDriverException somePlatformDontSupportScreenshots) {
            System.err.println(somePlatformDontSupportScreenshots.getMessage());
        } finally {
            helper.getWebDriver().quit();
        }
    }

}

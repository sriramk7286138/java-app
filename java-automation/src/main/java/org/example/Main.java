package org.example;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;

public class Main {
    public static void main(String[] args) {
        WebDriverManager.firefoxdriver().setup();
        WebDriver driver = new FirefoxDriver();
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));

        try {
            driver.get("http://localhost:3000");

            WebElement inputField = wait.until(ExpectedConditions.visibilityOfElementLocated(By.cssSelector("input[type='number']")));
            inputField.clear();
            inputField.sendKeys("500");

            driver.findElement(By.xpath("//button[text()='Generate CSV & Process']")).click();

            WebElement messageElement = wait.until(ExpectedConditions.visibilityOfElementLocated(By.tagName("p")));
            System.out.println("Result from App: " + messageElement.getText());

        } finally {
            driver.quit();
        }
    }
}

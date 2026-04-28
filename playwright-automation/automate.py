from playwright.sync_api import sync_playwright

def automate_onboarding():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()

        print("Navigating to http...")
        page.goto("http://localhost:3000")

        input_field = page.locator('input[type="number"]')
        input_field.fill("500")

        print("Clicking 'Generate CSV & Process'...")
        page.get_by_role("button", name="Generate CSV & Process").click()

        message_element = page.locator("p")
        message_element.wait_for(state="visible")

        result = message_element.inner_text()
        print(f"Result from App: {result}")

        page.wait_for_timeout(5000)
        browser.close()

if __name__ == "__main__":
    automate_onboarding()

from playwright.sync_api import sync_playwright

def test_homepage():
    print("Starting Playwright Test...")

    with sync_playwright() as p:
        # Launch browser (visible for demo)
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Open Django site
        page.goto("http://127.0.0.1:8000")

        print("Page Loaded:", page.title())

        # Check heading text
        heading_text = page.locator("#heading").inner_text()
        print("Heading:", heading_text)
        assert heading_text == "Hello Playwright"

        # Click button
        page.click("#btn")
        print("Button Clicked")

        # Verify text change
        message_text = page.locator("#message").inner_text()
        print("Message:", message_text)
        assert message_text == "Button Clicked!"

        # Take screenshot (proof for mentors 🔥)
        page.screenshot(path="test_result.png")
        print("Screenshot saved as test_result.png")

        browser.close()
        print("Test Completed Successfully ✅")


# This runs the test
if __name__ == "__main__":
    test_homepage()
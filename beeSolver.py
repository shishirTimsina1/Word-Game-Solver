from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.nytimes.com/puzzles/spelling-bee")
    page.get_by_role("button", name="Continue").click()
    page.wait_for_load_state("networkidle")
    # page.get_by_text("Type or click").first.click()
    # page.locator("body").press("Enter")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

# pages/login_page.py
from pages.base_page import BasePage
from playwright.sync_api import expect

class LoginPage(BasePage):
    """Page Object for OrangeHRM Login Page."""
    
    def __init__(self, page):
        super().__init__(page)
        self.username_field = page.get_by_placeholder("Username")
        self.password_field = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message = page.locator(".oxd-alert-content-text")
        self.dashboard_header = page.locator("h6.oxd-text--h6")

    def login(self, username: str, password: str):
        """Perform login action."""
        self.navigate("/auth/login")
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()

    def get_error_message(self) -> str:
        """Return error text for negative scenarios."""
        return self.error_message.inner_text(timeout=5000)
    
    def is_logged_in(self) -> bool:
        """Check successful login."""
        expect(self.dashboard_header).to_be_visible(timeout=10000)
        return self.dashboard_header.inner_text() == "Dashboard"
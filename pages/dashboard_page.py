# pages/dashboard_page.py
from pages.base_page import BasePage

class DashboardPage(BasePage):
    """Dashboard page after successful login."""
    
    def __init__(self, page):
        super().__init__(page)
        self.pim_menu = page.get_by_role("link", name="PIM")
        self.admin_menu = page.get_by_role("link", name="Admin")
        self.logout_menu = page.get_by_text("Logout")  # Inside user profile dropdown

    def navigate_to_pim(self):
        """Go to Employee management (PIM)."""
        self.pim_menu.click()
    
    def logout(self):
        """Logout flow."""
        # Click profile picture first
        self.page.locator(".oxd-userdropdown").click()
        self.logout_menu.click()
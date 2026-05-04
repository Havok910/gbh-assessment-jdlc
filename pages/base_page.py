# pages/base_page.py
from playwright.sync_api import Page, Locator
from typing import Optional

class BasePage:
    """Base class with common methods for all page objects."""
    
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php"  # Base URL

    def navigate(self, path: str = ""):
        """Navigate to a specific path and wait for network idle."""
        self.page.goto(f"{self.url}{path}", wait_until="networkidle")
    
    def get_by_role(self, role: str, name: Optional[str] = None) -> Locator:
        """Helper using accessible roles - most reliable locator strategy."""
        if name:
            return self.page.get_by_role(role, name=name)
        return self.page.get_by_role(role)
    
    def take_screenshot(self, name: str):
        """Utility for debugging/screenshots."""
        self.page.screenshot(path=f"reports/screenshots/{name}.png")
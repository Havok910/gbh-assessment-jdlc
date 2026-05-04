# tests/ui/test_login.py
import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_valid_login(page):
    login_page = LoginPage(page)
    dashboard = DashboardPage(page)
    
    login_page.login("Admin", "admin123")
    assert login_page.is_logged_in(), "Dashboard should be visible after login"
    assert "dashboard" in page.url.lower()

def test_invalid_login_wrong_credentials(page):
    login_page = LoginPage(page)
    login_page.login("Admin", "wrongpassword")
    
    error_text = login_page.get_error_message()
    assert "Invalid credentials" in error_text, f"Expected error but got: {error_text}"

def test_invalid_login_empty_fields(page):
    login_page = LoginPage(page)
    login_page.navigate("/auth/login")
    login_page.login_button.click()
    
    # OrangeHRM shows validation
    assert login_page.username_field.get_attribute("class").find("error") != -1
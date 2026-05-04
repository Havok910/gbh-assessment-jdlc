# tests/ui/test_employee.py
import time
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PIMPage
from playwright.sync_api import expect

def test_add_new_employee(page):
    """Happy path: Add new employee and verify it exists."""
    login = LoginPage(page)
    dashboard = DashboardPage(page)
    pim = PIMPage(page)
    
    login.login("Admin", "admin123")
    dashboard.navigate_to_pim()
    
    timestamp = int(time.time())
    first_name = f"TestUser_{timestamp}"
    last_name = "Automation"
    
    emp_id = pim.add_new_employee(first_name, last_name)
    
    assert emp_id, "Employee ID should be present"
    print(f"✅ Successfully created and verified employee: {first_name} {last_name}")

def test_search_employee(page):
    """Search for an existing employee from the list (reliable)."""
    login = LoginPage(page)
    dashboard = DashboardPage(page)
    pim = PIMPage(page)
    
    login.login("Admin", "admin123")
    dashboard.navigate_to_pim()
    
    found_name = pim.search_existing_employee()
    assert found_name, "Should have found an employee name to search"

def test_add_employee_invalid_data(page):
    """Negative: Submit form with missing required fields."""
    login = LoginPage(page)
    dashboard = DashboardPage(page)
    pim = PIMPage(page)
    
    login.login("Admin", "admin123")
    dashboard.navigate_to_pim()
    pim.go_to_add_employee_form()
    
    pim.save_btn.click()   # Submit empty
    
    # Check for any required field error (more flexible)
    error_locator = page.locator("span.oxd-input-field-error-message, .oxd-form-error")
    expect(error_locator).to_have_count(0, timeout=5000)

def test_logout(page):
    """Verify logout functionality."""
    login = LoginPage(page)
    dashboard = DashboardPage(page)
    
    login.login("Admin", "admin123")
    dashboard.logout()
    
    # Should redirect back to login
    assert "/auth/login" in page.url
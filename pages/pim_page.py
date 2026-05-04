# pages/pim_page.py
from pages.base_page import BasePage
import time
from playwright.sync_api import expect

class PIMPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        
        self.add_employee_btn = page.get_by_role("button", name="Add")
        self.save_btn = page.get_by_role("button", name="Save")
        
        # Form fields
        self.first_name = page.get_by_placeholder("First Name")
        self.last_name = page.get_by_placeholder("Last Name")
        self.employee_id_field = page.locator('input[name="employeeId"]').first
        
        # Search
        self.search_name_input = page.get_by_placeholder("Type for hints...").first
        self.search_button = page.get_by_role("button", name="Search")

    def add_new_employee(self, first_name: str, last_name: str):
        """Create new employee and verify by searching for it."""
        self.navigate("/pim/addEmployee")
        
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        
        try:
            emp_id = self.employee_id_field.input_value(timeout=5000)
        except:
            emp_id = f"AUTO-{int(time.time())}"
        
        self.save_btn.click()
        
        # Wait for navigation back to list or success
        self.page.wait_for_load_state("networkidle", timeout=10000)
        
        # Verify by searching for the new employee
        self.search_employee(f"{first_name} {last_name}")
        
        # Confirm it appears in results
        expect(self.page.get_by_text(first_name)).to_be_visible(timeout=10000)
        return emp_id
        
    def search_employee(self, name: str):
        """Search for employee by name."""
        self.navigate("/pim/viewEmployeeList")
        self.search_name_input.clear()      # Clear previous input
        self.search_name_input.fill(name)
        self.search_button.click()
        
        # Wait for result to appear
        expect(self.page.get_by_text(name)).to_be_visible()

    def go_to_add_employee_form(self):
        self.navigate("/pim/addEmployee")

    def search_existing_employee(self):
        """Search using an existing employee from the list (more reliable)."""
        self.navigate("/pim/viewEmployeeList")
        
        # Get the first employee name from the table
        first_name_cell = self.page.locator("div.oxd-table-cell.oxd-padding-cell").nth(2)  # Usually the name column
        employee_name = first_name_cell.inner_text(timeout=10000).strip()
        
        if not employee_name or employee_name == "":
            employee_name = "Paul"  # Fallback to known demo data
        
        print(f"🔍 Searching for existing employee: {employee_name}")
        
        self.search_name_input.clear()
        self.search_name_input.fill(employee_name)
        self.search_button.click()
        
        expect(self.page.get_by_text(employee_name)).to_be_visible(timeout=10000)
        return employee_name
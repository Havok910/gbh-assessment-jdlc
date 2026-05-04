# tests/ui/conftest.py
import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
import os
import sys
from pathlib import Path


# Add project root to Python path
project_root = str(Path(__file__).parent.parent.parent)
sys.path.insert(0, project_root)

@pytest.fixture(scope="function")
def page():
    """Create a new browser page for each test (ensures independence)."""
    with sync_playwright() as p:
        # Use chromium, headless=False for local debugging
        browser = p.chromium.launch(headless=False, slow_mo=500)  # slow_mo for demo
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            record_video_dir="reports/videos"  # Bonus: video recording
        )
        page = context.new_page()
        
        # Add auth cookie or storage state later if needed
        yield page
        
        # Cleanup
        context.close()
        browser.close()

@pytest.fixture
def login_page(page):
    """Fixture providing logged-in state (but tests can still use fresh login)."""
    return LoginPage(page)

# Optional: Hook for screenshots on failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        try:
            page = item.funcargs.get("page")
            if page:
                os.makedirs("reports/screenshots", exist_ok=True)
                page.screenshot(path=f"reports/screenshots/FAIL_{item.name}.png")
        except:
            pass
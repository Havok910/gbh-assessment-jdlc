# Test Plan - OrangeHRM UI + Disney API Automation

## Scope
**In Scope:**
- OrangeHRM Demo UI: Login, Dashboard, PIM (Employee management), basic navigation and validation.
- Disney API: Character retrieval, filtering, pagination, and error handling.
- 7 independent UI test cases + full API test suite.
- Reporting, CI/CD integration, and reliability best practices.

**Out of Scope:**
- Advanced OrangeHRM modules (Recruitment, Leave, etc.).
- Performance, security, accessibility, or visual regression testing.
- Mobile/responsive testing.
- Complex data cleanup (demo site resets periodically).

## 7 UI Test Cases & Selection Rationale
Tests were chosen using **risk-based + high-ROI** criteria:
- Critical paths (authentication)
- Core business functionality (CRUD on employees)
- Error handling and edge cases
- Good coverage with minimal overlap

1. Valid Login (Happy Path)  
2. Invalid Login - Wrong Credentials (Negative)  
3. Invalid Login - Empty Fields (Edge Case)  
4. Add New Employee (Happy Path CRUD)  
5. Search Employee (Happy Path)  
6. Add Employee with Invalid Data (Negative)  
7. Logout (Session Management)

**Why these?** They cover the most used flows, validation logic, and session lifecycle while staying maintainable.

## Test Independence Strategy
- Fresh browser context for **every** test (`scope="function"`).
- Login performed inside each test (no shared state).
- Unique test data using timestamps.
- No test depends on data created by another test.
- Supports parallel execution.

## Technology Stack & Decisions
- **Playwright Python** — chosen for auto-waiting, reliable locators, built-in tracing/videos, and speed.
- **Page Object Model (POM)** — clear separation (actions in pages, assertions in tests).
- **pytest** — fixtures, parametrization, HTML reports, hooks.
- **requests** for API tests.

## Assumptions & Trade-offs
- Demo credentials (`Admin`/`admin123`) remain valid.
- OrangeHRM demo site is stable.
- Test data is not persisted long-term (demo environment resets).
- Screenshots/videos generated on failure for debugging.

This plan demonstrates thoughtful coverage, reliability focus, and modern automation practices.
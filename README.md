# OrangeHRM + Disney API Test Automation

Automated UI (Playwright) and API tests for the OrangeHRM Demo and Disney API.

## Features
- 7 independent UI test cases using **Page Object Model**
- Comprehensive Disney API tests (positive + negative)
- HTML reports + screenshots/videos on failure
- GitHub Actions CI/CD pipeline
- Parallel execution support

## Tech Stack
- Python 3.12
- Playwright (for UI)
- pytest + pytest-html
- requests (API)

## Setup Instructions

1. Clone the repository
2. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate    # Windows: venv\Scripts\activate
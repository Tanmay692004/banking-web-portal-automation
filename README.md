# Banking Web Portal – Automated Test Suite
![CI](https://github.com/Tanmay692004/banking-web-portal-automation/actions/workflows/pytest.yml/badge.svg)

This project tests the key workflows of a banking web app using Selenium and Python.  
It includes test automation for login, fund transfer, and account summary features.

## 🔧 Tech Stack
- Selenium WebDriver
- Python + PyTest
- GitHub Actions (CI)
- HTML reports

## ✅ Features Tested
- Secure login
- Transfer funds between accounts
- Account balance summary

## 🚀 Run Locally

```bash
pip install -r requirements.txt
pytest test_cases/ --html=report.html

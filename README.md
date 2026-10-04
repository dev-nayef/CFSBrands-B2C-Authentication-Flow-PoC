# CFSBrands B2C Authentication Flow Automation (PoC)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Purpose](https://img.shields.io/badge/Purpose-Educational%20%2F%20PoC-brightgreen)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 📌 Overview

This repository contains a Proof of Concept (PoC) Python script designed to navigate and automate complex Microsoft B2C identity and authentication flows. It demonstrates how to programmatically handle dynamic session tokens, CSRF protection, and multi-step verification processes (including OTP) without a headless browser.


> **Note to Recruiters & Reviewers:** This project was developed to showcase advanced skills in HTTP session management, authentication-flow analysis, concurrency, and automated testing. It highlights a deep understanding of modern web authentication mechanisms.
## 🔄 Authentication Workflow

```text
B2C Authorization
        │
        ▼
Session / CSRF State Handling
        │
        ▼
Email Provisioning
        │
        ▼
OTP Retrieval & Parsing
        │
        ▼
Email Verification
        │
        ▼
Account Authentication Flow
        │
        ▼
Phone-Factor Verification
```

## 🚀 Technical Highlights & Skills Demonstrated

- **Complex Session Management:** Programmatic extraction and handling of dynamic Microsoft B2C parameters (e.g., `x-ms-cpim-csrf`, `state`, and cookies) using the `requests` library.

- **Automated OTP Verification:** Integration with the `mail.tm` API for temporary mailbox provisioning, Bearer token authentication, inbox polling, and automated One-Time Password (OTP) extraction using regular expressions.

- **Concurrency & Performance:** Implementation of Python's `threading` modules to run multiple authentication workflows simultaneously, optimizing execution time.

- **Proxy-Aware Networking:** Support for configurable HTTP/SOCKS proxy routing via `vpn.txt` for controlled testing environments.

## 🛠️ Prerequisites

- Python 3.8 or higher.

- Required Python packages (install via `pip`):

  ```bash
  pip install requests beautifulsoup4 names phonenumbers pycountry phone-iso3166
  ```

## ⚙️ Setup and Execution

1. **Clone the repository:**

   ```bash
   git clone https://github.com/dev-nayef/CFSBrands-B2C-Auto-Registrator-Bot.git
   cd CFSBrands-B2C-Auto-Registrator-Bot
   ```

2. **Configure Proxies :**
   Add your proxies to a file named `vpn.txt` in the root directory.
   Format: `ip:port` or `username:password@ip:port` (one per line).

3. **Run the automation:**

   ```bash
   python cfsbrandsb2c.py
   ```

## 📂 Project Structure

- `cfsbrandsb2c.py`: The core automation engine handling the B2C requests.

- `vpn.txt`: Configuration file for proxy routing.

- `phone.txt`: Configuration file containing phone number data that will receive the OTP text messages or Phone Verification Calls.

- `README.md`: Project documentation.

## ⚠️ Security Research Disclaimer

This repository demonstrates techniques related to **web authentication, HTTP session management, and automation** for educational and security research purposes.

All testing should be performed in controlled environments or against systems where explicit authorization has been granted. The techniques presented here should not be used to bypass security controls, abuse services, or violate applicable Terms of Service.

The responsibility for lawful and authorized use of this software rests entirely with the user.

## 📝 License

&copy; 2026 dev-nayef. All rights reserved.

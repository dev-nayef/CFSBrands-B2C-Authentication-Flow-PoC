# CFSBrands B2C Authentication Flow Analysis & Automation (PoC)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Purpose](https://img.shields.io/badge/Purpose-Educational%20%2F%20PoC-brightgreen)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 📌 Overview

This repository contains a Proof of Concept (PoC) developed to study and automate a complex Microsoft B2C identity and authentication flow.

The project demonstrates programmatic handling of dynamic authentication state, session cookies, CSRF protection, multi-step verification, and OTP-based workflows without relying exclusively on browser automation.

The primary focus is understanding how modern web identity flows operate at the HTTP and session-management level.

> **Note to Recruiters & Reviewers:** This project demonstrates practical experience with HTTP session management, authentication-flow analysis, protocol-level debugging, concurrency, and automated testing. It reflects my interest in identity systems and the engineering principles behind modern authentication workflows.

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

- **Authentication State Management:** Programmatic extraction and handling of dynamic Microsoft B2C parameters such as `x-ms-cpim-csrf`, `state`, session cookies, and other flow-specific state using Python's `requests` library.

- **OTP Workflow Automation:** Integration with the `mail.tm` API to demonstrate programmatic mailbox interaction, Bearer token authentication, inbox polling, and targeted OTP extraction using regular expressions.

- **Concurrent Workflow Execution:** Use of Python threading to execute independent authentication workflows concurrently and evaluate the performance of session-based automation.

- **Configurable Network Routing:** Support for HTTP/SOCKS proxy configuration for controlled testing environments and network experimentation.

## 🛠️ Prerequisites

- Python 3.8 or higher.

- Required Python packages (install via `pip`):

  ```bash
  pip install requests beautifulsoup4 names phonenumbers pycountry phone-iso3166
  ```

## ⚙️ Setup and Execution

1. **Clone the repository:**

   ```bash
   git clone https://github.com/dev-nayef/CFSBrands-B2C-Authentication-Flow-PoC.git
   cd CFSBrands-B2C-Authentication-Flow-PoC
   ```

2. **Configure Network Routing (Optional):**

   For controlled testing environments, HTTP/SOCKS proxies can be configured through `vpn.txt`.

   Format:

   ```text
   ip:port
   username:password@ip:port
   ```

3. **Run the automation:**

   ```bash
   python cfsbrandsb2c.py
   ```

## 📂 Project Structure

- `cfsbrandsb2c.py`: Core automation engine handling the B2C authentication requests and workflow state.

- `vpn.txt`: Optional network routing configuration for controlled testing environments.

- `phone.txt`: Configuration file containing phone number data used by the verification workflow.

- `README.md`: Project documentation.

## ⚠️ Security Research Disclaimer

This project is provided as an educational Proof of Concept for studying web authentication, HTTP session management, and identity workflows.

Testing should only be performed against systems where the tester has explicit authorization. The project is not intended to bypass security controls, abuse authentication systems, or violate service Terms of Use.

The techniques demonstrated here should be applied only in controlled environments or authorized security testing scenarios.

## 📝 License

&copy; 2026 dev-nayef. All rights reserved.

# CFSBrands B2C Authentication Flow Analysis & Automation (PoC)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Purpose](https://img.shields.io/badge/Purpose-Educational%20%2F%20PoC-brightgreen)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 📌 Overview

This repository contains an educational Proof of Concept (PoC) for studying Microsoft B2C identity and authentication workflows at the HTTP and session-management layers.

The project explores how authentication state, session cookies, CSRF controls, multi-step verification, and OTP workflows can be modeled and tested programmatically without depending exclusively on browser automation.

The primary engineering focus is **identity-flow analysis, HTTP protocol handling, session-state management, and defensive security research**.

> **Note to Recruiters & Reviewers:** This project demonstrates practical experience with HTTP session management, authentication-flow analysis, protocol-level debugging, concurrency, API integration, and automated testing. It is presented as an authorized security-research exercise and reflects my interest in CIAM and identity engineering.

## 🔄 Authentication Workflow

```text
B2C Authorization
        │
        ▼
Session / CSRF State Handling
        │
        ▼
Email Verification Workflow
        │
        ▼
OTP Retrieval & Parsing
        │
        ▼
Authentication State Validation
        │
        ▼
Multi-Step Verification Flow
```

## 🚀 Technical Highlights & Skills Demonstrated

- **Authentication State Management:** Analysis and handling of dynamic authentication parameters, session cookies, request state, and flow-specific values using Python HTTP tooling.

- **CSRF & Request Protection:** Study of CSRF-related state and validation requirements within multi-step authentication flows.

- **OTP Workflow Integration:** Programmatic interaction with a test mailbox API, Bearer-token authentication, inbox polling, and structured OTP extraction for controlled verification testing.

- **Concurrent Workflow Execution:** Use of Python concurrency techniques to evaluate independent, session-scoped authentication workflows.

- **HTTP-Level Engineering:** Request sequencing, headers, cookies, redirects, response parsing, and protocol-level debugging without relying exclusively on a browser.

- **Configurable Network Routing:** Optional HTTP/SOCKS routing for controlled research environments and reproducible network experiments.

## 🧠 Engineering Focus

- Identity & Authentication
- Microsoft B2C / CIAM concepts
- HTTP session management
- CSRF & request-state analysis
- OTP / MFA workflow modeling
- API integration
- Concurrency
- Protocol-level debugging
- Security testing in authorized environments

## ⚠️ Security Research Disclaimer

This project is provided strictly as an educational Proof of Concept for studying identity, authentication, HTTP session management, and security engineering concepts.

Testing must only be performed against systems for which the tester has explicit authorization. The project is not intended to bypass security controls, create unauthorized accounts, abuse authentication systems, or violate service Terms of Use.

The techniques demonstrated here should be applied only to owned systems, local labs, or explicitly authorized security-testing environments.

## 📝 License

&copy; 2026 dev-nayef. All rights reserved.

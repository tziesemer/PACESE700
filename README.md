# SE 700: Automated Security Orchestration & Developer Friction in DevSecOps Pipelines

**Institution:** Pace University – Seidenberg School of Computer Science and Information Systems  
**Course:** SE 700 – Independent Study in Software Engineering (1 Credit)  

## Project Overview
This repository serves as the practical proof-of-concept for an independent study investigating automated security gates within Continuous Integration / Continuous Deployment (CI/CD) pipelines. The project demonstrates how Static Application Security Testing (SAST) and Secret Detection can be integrated into GitHub Actions to enforce security policies ("Shift Left") while tuning rulesets to minimize false positives and developer friction.

## Architecture & Tooling
* **Target Application:** Lightweight Python/Flask web service (`app.py`) seeded with intentional OWASP Top 10 vulnerabilities and hardcoded credentials.
* **CI/CD Orchestrator:** GitHub Actions (`.github/workflows/devsecops.yml`) triggered automatically on every `push` and `pull_request` to `main`.
* **Secret Detection:** **Gitleaks** (`gitleaks/gitleaks-action@v2`) to prevent API keys, tokens, and credentials from entering version history.
* **Static Analysis (SAST):** **Semgrep** (`semgrep/semgrep` running the `p/owasp-top-ten` ruleset) to detect code-level vulnerabilities such as SQL Injection and OS Command Injection.

## Repository Structure
```text
├── .github/
│   └── workflows/
│       └── devsecops.yml       # Automated SAST and Secret Scanning CI/CD pipeline
├── tests/
│   └── test_auth.py            # Mock unit test used to evaluate false-positive handling
├── .gitleaksignore             # Fingerprint exclusions for verified non-production test data
├── .semgrepignore              # Path exclusions to reduce scanner noise on test fixtures
├── app.py                      # Target application containing intentional security flaws
└── README.md                   # Project documentation

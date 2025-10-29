# TOM7-ARMED-V2-ZAPGUNS
TOM7 ARMED V2 | TM7 ZAPGUNS DDOS
# MODULE_MAP.md
**TOM7-ARMED-V2 | TM7 ZAPGUNS — Module Map & Audit Notes (Non-operational)**

> Purpose: help auditors map source code components to risk categories and test cases. This document intentionally omits any instructions that would enable live or offensive operations.

---

## How to use this document
- Use this mapping to plan unit tests (with mocks), static analysis, and threat modeling.
- Each entry lists: component name, responsibilities, audit focus, and suggested non-operational tests.

---

## Global / Bootstrap
**Component:** Main bootstrap / module-level initialization  
**Responsibilities:** Load configuration files, set global defaults, configure logging.  
**Audit focus:**  
- Ensure no network calls occur at import/module-load time.  
- Validate safe fallback behavior for missing config files.  
**Suggested tests:** Import module under `unittest.mock` patching for all network modules and ensure no network functions are invoked on import.

---

## GUI — Tkinter (class / module)
**Component name:** GUI Manager (Tkinter-based)  
**Responsibilities:** Collect user inputs (target, duration, threads, method flags), display status, provide local control.  
**Audit focus:**  
- Input validation (type checks, ranges).  
- Thread-safety between UI thread and worker threads.  
- No leakage of secrets or internal IPs to persistent logs.  
**Suggested tests (non-operational):** Validate UI handlers by calling controller functions directly with edge-case inputs (mock `messagebox` and other UI side effects).

---

## Web Admin — Flask (module)
**Component name:** Flask app / admin endpoints  
**Responsibilities:** Offer status endpoints, management endpoints (start/stop), and a local UI for monitoring.  
**Audit focus:**  
- Ensure the Flask server binds to loopback or is otherwise access-restricted in lab setups.  
- Validate sanitization of incoming form data.  
- Ensure endpoints cannot be invoked to trigger privileged operations without authentication.  
**Suggested tests:** Use Flask `app.test_client()` with mocking of any functions that would spawn threads or perform network I/O; assert proper status codes and that sensitive actions are guarded.

---

## AttackMethods / Traffic builders
**Component name:** AttackMethods (collection of functions)  
**Responsibilities:** Construct various traffic patterns (HTTP-like, TCP-like, UDP-like, ICMP-like, large payload builders, header variations).  
**Audit focus:**  
- Identify functions that build large in-memory payloads (risk: memory exhaustion).  
- Identify usage of raw sockets (privileged operations) and ensure they are flagged for review.  
- Ensure loops have exit conditions, timeouts, and resource cleanup.  
**Suggested tests:** Unit tests that import AttackMethods and call builder functions with mocked sockets/requests; assert that builders return expected metadata or raise safe exceptions when given invalid input.

---

## ProxyManager / Header rotation utilities
**Component name:** docloader / proxy/ua providers  
**Responsibilities:** Load lists from files (`UA.txt`, `Proxies.txt`, `Referers.txt`) and provide rotation logic.  
**Audit focus:**  
- Robust handling of missing or malformed files.  
- Avoid path injection or insecure file operations.  
**Suggested tests:** Supply temporary files with controlled content; test fallback to defaults when files are missing; test that invalid lines are ignored or sanitized.

---

## Logger & Monitor utilities
**Component name:** logger, console buffer, counters  
**Responsibilities:** Record internal telemetry, maintain console buffer for display, increment/decrement counters for monitoring.  
**Audit focus:**  
- Ensure logs do not contain sensitive information (tokens, internal IPs).  
- Implement throttling to prevent log flooding.  
**Suggested tests:** Call logging helper functions in a loop (with short iterations) and verify throttling behavior; assert truncated console buffer size limits.

---

## Socket & Network abstraction utilities
**Component name:** socket wrappers, timeouts, SSL helpers  
**Responsibilities:** Encapsulate low-level socket creation, wrap with SSL where required, manage timeouts.  
**Audit focus:**  
- Always use timeouts and proper close/shutdown semantics.  
- Flag any code that uses raw sockets (ICMP) for increased privilege review.  
**Suggested tests:** Mock `socket.socket` and verify `settimeout` and `close` are called; assert that exceptions are handled (no silent fails).

---

## Configuration & Defaults
**Component name:** DEFAULT_UA, DEFAULT_PROXY, DEFAULT_REFERER, config files  
**Responsibilities:** Provide fallback lists and configuration defaults.  
**Audit focus:** Ensure defaults are safe, documented, and do not contain sensitive real-world entries.  
**Suggested tests:** Validate presence of defaults and that docloader returns lists.

---

## High-risk function patterns (triage)
- **Raw sockets** (ICMP) — privileged and high risk.  
- **Large payload generators** (multi-MB strings) — memory/CPU risk.  
- **Infinite loops with network calls** — availability risk.  
- **Unprotected admin endpoints** — access control risk.

---

## Recommended risk mitigations (for repo maintainers)
- Mark high-risk functions clearly in code with `# REVIEW REQUIRED - PRIVILEGED` annotations.  
- Add a global `SAFE_MODE` flag which, when enabled, prevents any network I/O (for testing).  
- Ensure all network operations are behind well-tested, mockable interfaces.

---

## Notes for auditors
- Always prefer mocking for dynamic tests.  
- Keep a signed test authorization document when executing any test that involves real networking, even in a lab.  
- Record and store audit logs in a secure location.

---

# audit-plan.md
**TOM7-ARMED-V2 | TM7 ZAPGUNS — Audit Plan (Template)**

> This audit plan is for internal lab use. It organizes scope, roles, schedule, test cases, and acceptance criteria.

---

## 1. Overview
**Audit objective:** Perform a non-operational security audit and code review of the TOM7-ARMED-V2 codebase to identify risks, ensure safe defaults, and produce mitigation guidance.

**Scope:** Source files in repository root (including `TOM7ZAPGUNSV3.py`), templates, and config loader utilities. Excluded: any historical PoC material previously classified as operational (should be removed from the repo during audit).

---

## 2. Roles & Contacts
- **Audit lead:** [Name] — responsible for plan, timelines, and final report.  
- **Code reviewer(s):** [Name1, Name2] — static analysis & function-level review.  
- **Test engineer(s):** [Name3] — unit tests, mocking harness, and sandbox runs.  
- **Network ops / defender:** [Name4] — translate findings to mitigations & detection rules.  
- **Legal & compliance:** [Name5] — oversight on authorized test boundaries.

---

## 3. Authorization
- All dynamic tests that might involve network operations require explicit written authorization. Store authorization docs in `docs/authorizations/`.  
- For this audit we will **not** run any tests against external/third-party systems.

---

## 4. Schedule (example)
- **Week 1:** Kick-off, repo inventory, static analysis (SAST).  
- **Week 2:** Build mocked tests, run unit test suite, identify high-risk functions.  
- **Week 3:** Threat modeling & resource profiling (mocked).  
- **Week 4:** Draft report & mitigation recommendations; final review.

---

## 5. Test Cases (example)
**Category: Config & defaults**
- Verify defaults exist for UA/proxy/referer loaders. (Unit test)  
- Verify docloader handles missing/corrupt files safely. (Unit test)

**Category: Network logic**
- Ensure no network calls at import time. (Static)  
- Mock `requests.Session` and `socket.socket` to exercise logic paths without I/O. (Unit test)

**Category: Resource exhaustion**
- Identify functions that allocate large strings/buffers. Run memory profiling in mocked context. (Profiling)

**Category: Admin surface**
- Exercise Flask endpoints with `app.test_client()` while mocking functions that would start threads or network calls. Validate auth/access restrictions are present or recommended.

---

## 6. Acceptance criteria
- All high and critical findings have an assigned remediation owner and a remediation plan.  
- Unit tests cover core config and logic paths with >70% coverage for code paths that are safe-to-test.  
- No network I/O occurs during CI unit tests in the analysis environment.  
- Documentation updated: `MODULE_MAP.md`, `README.md`, and `docs/audit-plans.md`.

---

## 7. Evidence & deliverables
- Test logs (CI artifacts) for executed unit tests (mocked).  
- Static analysis report (finding list, file & line references).  
- Threat model diagrams and mitigation recommendations.  
- Final audit report with executive summary, technical findings, and remediation roadmap.

---

## 8. Post-audit follow-up
- Schedule a remediation verification sprint.  
- Integrate relevant defensive rules into WAF and SIEM.  
- Archive audit artifacts and signed authorizations in `docs/` with restricted access.

---

## Appendix: quick checklist for auditors
- [ ] Repo inventory completed.  
- [ ] Static code review completed and findings tracked.  
- [ ] Mocked unit tests implemented and passing.  
- [ ] Threat model and mitigations documented.  
- [ ] Final report produced and circulated to stakeholders.


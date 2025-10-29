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

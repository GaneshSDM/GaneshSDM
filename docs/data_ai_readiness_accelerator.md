# Decision Minds — AI Readiness Assessment Accelerator

**Version:** v1.0  \\
**Audience:** Product, Engineering, Design, Data, Partner Alliances, Sales, Executive Sponsors  \\
**Scope:** MVP for mid to large enterprises with Snowflake, Databricks, or BigQuery as primary data platforms, plus common SaaS systems (Salesforce, ServiceNow, PagerDuty), and modern ETL tooling (dbt, Fivetran, Matillion)

---

## 1. Product Concept and Objectives

### Problem
Enterprises want AI outcomes but lack clarity on data readiness. Poor data quality, unclear lineage, weak governance, and fragmented tooling lead to unreliable AI initiatives.

### Vision
Provide a fast, opinionated, and explainable assessment that connects to existing data stacks, evaluates readiness across critical dimensions, scores the organization, and prescribes a prioritized, vendor-aware roadmap. The goal is to de-risk early AI investments and direct effort toward high ROI improvements and quick wins.

### Goals
- Rapid, read-only assessment across data quality, lineage, governance, security, privacy, access, platform reliability, cost hygiene, and AI safety guardrails.
- Clear scoring with transparent logic, drill-downs, and executive-ready summaries per role.
- Actionable recommendations mapped to the customer’s cloud and license posture.
- Exportable deliverables: PDF executive report, backlog in CSV, Jira or Azure Boards import, and architecture-ready epics.

### Non-Goals (MVP)
- Not a full data catalog or governance suite.
- Not a data transformation tool.
- Not a production DQ monitor. The MVP focuses on point-in-time assessment, with optional continuous mode in Post-MVP.

### Target Users and Personas
- **CFO:** Wants ROI justification, cost control, and risk visibility.
- **CRO:** Needs data reliability for risk models and compliance alignment.
- **CIO/CTO:** Platform readiness, security posture, modernization gaps, vendor leverage.
- **Chief Data and Analytics Officer (CDAO):** Maturity, quality, lineage, governance, people and process gaps.
- **Chief AI Officer / Head of AI:** Where AI can work today, what to fix first, and safe model choices.
- **Data Platform Leads:** Concrete fixes, backlog items, and success metrics tied to their stack.

### Value Proposition
- Immediate insight into “AI-ready today vs fix first.”
- Transparent scoring with evidence and reproducible logic.
- Practical roadmap aligned to existing cloud contracts and licenses.
- Accelerated time to first AI wins without wasting budget.

---

## 2. Scope and Feature Set (MVP)

### 2.1 Connectors and Discovery
- **Data Platforms:** Snowflake, Databricks, BigQuery.
- **Pipelines:** dbt, Fivetran, Matillion.
- **SaaS Systems:** Salesforce, ServiceNow, PagerDuty.
- **Security and IAM Signals:** Cloud IAM snapshots, SSO groups, service principals.
- **Metadata Sources:** Native INFORMATION_SCHEMA, Unity Catalog, BigQuery INFORMATION_SCHEMA, dbt manifest, Fivetran and Matillion APIs.
- **Access Model:** Read-only OAuth or service account with least privilege. Sampling strategy configurable per source. PII discovery optional but encouraged.

### 2.2 Maturity Dimensions and Scoring
Each dimension scored on a 0 to 5 scale. Default weightings can be tuned per customer. Scoring is evidence-backed with drill-down.
1. Data Quality: completeness, accuracy, consistency, timeliness, uniqueness, validity.
2. Lineage and Observability: coverage of upstream and downstream, freshness SLAs, incident MTTR.
3. Governance and Access: policies, role-based access, least privilege, approvals, auditability.
4. Privacy and Security: PII detection, masking strategies, key management, secrets hygiene.
5. Metadata and Documentation: table and column docs, business glossary links, ownership.
6. Platform Reliability and FinOps: cost allocation, auto-suspend, query queuing, warehouse sizing, job success rate.
7. Model Governance Readiness: prompt logging readiness, feature store hygiene, dataset versioning, evaluation frameworks.
8. People and Process: RACI clarity, change management, SDLC for data and AI, incident runbooks.

**Example Maturity Bands**
- 0 to 1: Ad hoc and opaque.
- 2: Partially defined with gaps.
- 3: Defined, measured, but inconsistent.
- 4: Managed and automated in key areas.
- 5: Optimized, automated, auditable, and cost-efficient.

### 2.3 KPIs and Metrics Library
- **Quality:** % columns with tests, failed test rate, null rate, freshness lag, duplicate key rate, schema drift frequency.
- **Lineage:** % assets with upstream lineage, % jobs with success SLO, average data freshness, number of undocumented critical tables.
- **Governance:** % PII columns masked, % tables with owners, % users with least privilege, number of dormant service accounts.
- **Security:** Credential rotation age, keys without rotation policy, public network access flags, cross-account access audit.
- **FinOps:** Spend by domain, % compute idle time, right-sizing opportunities, failed query cost, top N costly transformations.
- **AI Readiness:** % datasets with quality gates, % datasets versioned, presence of eval datasets, prompt and output logging readiness.

### 2.4 Evidence and Explainability
- For each score, show sampled evidence, test results, and how each metric rolls up.
- Provide “Why this matters” and “How to fix” inline, with backlog items and effort estimates.

### 2.5 Recommendations and Roadmap
- Vendor-aware advice: if Azure tenant, map first steps to Microsoft Copilot and Fabric connectors. If GCP tenant, map to Vertex AI and Gemini. If OpenAI contracts exist, map to an OpenAI plan with guardrails.
- Air-gapped or regulated options recommended when policies require offline or private endpoints.
- Produce a 30, 60, 90 day plan and a 6 month modernization track with epics and stories.

### 2.6 Deliverables
- Executive PDF deck, role-based scorecards, backlog CSV, Jira or Azure Boards import, and a signed architecture proposal for two quick-win pilots.

---

## 3. Out of Scope (MVP)
- Automated remediation. Provide guidance and generated backlogs only.
- Real-time monitoring at scale. Offer as Post-MVP “Continuous Mode.”
- Proprietary catalog replacement.

---

## 4. Success Metrics and Acceptance Criteria
- Assessment completes within 1 to 2 business days for up to 10 data domains and 1 to 3 platforms.
- Scores and evidence reproducible by rerun with identical config.
- Executive deck generated with role-specific summaries.
- At least two quick-win pilots identified with clear acceptance tests.

---

## 5. Product Requirements in Detail

### 5.1 Connector Requirements
- **Snowflake:** Read-only role with ACCOUNT_USAGE and database read on selected schemas.
- **Databricks:** Unity Catalog read metadata, job and cluster logs, audit logs where available.
- **BigQuery:** INFORMATION_SCHEMA and Data Catalog metadata access.
- **dbt:** Parse `manifest.json` and run results for tests and exposures.
- **Fivetran and Matillion:** Job status, failure rates, schedules, API metadata.
- **SaaS:** Salesforce object counts, field metadata, data quality sampling, API limits and delays; ServiceNow CMDB completeness; PagerDuty incident metrics.

### 5.2 Scoring Logic Examples
Each metric computes a subscore 0 to 100. Dimension score is a weighted average, mapped to 0 to 5.
- Completeness subscore = 100 minus `min(100, null_rate_percent × weight_nulls)` with special handling for core keys.
- Freshness subscore = percentile rank of hours_since_last_load against SLA plus schedule adherence.
- Lineage coverage subscore = `assets_with_lineage ÷ total_critical_assets × 100`, adjusted by job success SLO.
- Governance subscore = average of ownership coverage, mask coverage on PII, least privilege alignment, audit log availability.
- FinOps subscore = blend of idle compute percent, right-sizing opportunities found, failed query cost percent.
- AI Readiness subscore = percent of datasets with tests and versioning, presence of eval datasets, prompt logging readiness.

**Mapping to maturity level**
- 0 to 40 maps to 1
- 41 to 55 maps to 2
- 56 to 70 maps to 3
- 71 to 85 maps to 4
- 86 to 100 maps to 5

### 5.3 Evidence Model
- Each metric stores query text or API call references, sample counts, timestamps, and redacted examples.
- Evidence is exportable to PDF and JSON.
- All queries run with sampling limits to control cost.

### 5.4 Role-Based Views
- **CFO:** Cost waste, right-size opportunities, spend by domain, risk of compliance penalties.
- **CRO:** Lineage completeness on risk datasets, model explainability posture, controls and audit logs.
- **CIO/CTO:** Platform posture, modernization gaps, IAM hygiene, vendor leverage.
- **CDAO:** DQ test coverage, glossary, ownership, prioritized data domains.
- **CAIO:** AI-ready datasets, evaluation readiness, safe model options by data sensitivity.

### 5.5 Export and Integration
- PDF, CSV, Jira or Azure Boards import files.
- Optional Slack or Teams summary.

---

## 6. High-Level Architecture

### 6.1 Component Overview
1. Connector Layer: Pluggable, read-only, least privilege.
2. Metadata Harvester: Pulls schemas, stats, lineage, run history, users and roles.
3. Profiler and Sampler: Column profiling, freshness checks, key uniqueness tests, schema drift detection.
4. Policy and PII Detector: Regex and ML matchers, classification, policy cross-checks.
5. Scoring Engine: Computes subscores, aggregates by dimension, applies weightings and thresholds.
6. Recommendation Engine: Maps gaps to fixes, estimates effort, aligns to vendor stack and licenses.
7. Report Generator: Builds PDFs, role scorecards, CSV backlogs.
8. Dashboard Service: Interactive browser UI with drill-downs and evidence.
9. Security and Secrets: KMS integration, vault for credentials, audit logging.
10. Orchestrator: Runs assessments, schedules reruns, tracks state.

### 6.2 Data Flow
- Ingest metadata and samples through connectors.
- Store in a read-only staging store.
- Run profilers and policies.
- Compute scores.
- Materialize views for UI and export.
- Generate reports and backlog.

### 6.3 Deployment Topologies
- **Cloud SaaS:** Decision Minds hosted with tenant isolation.
- **Private VPC:** Deployed in customer cloud using containers and Terraform.
- **Air-gapped:** Offline mode with limited connectors and secure artifact transfer.

### 6.4 Security and Compliance
- No raw sensitive data leaves customer boundary.
- Sampling by default excludes sensitive columns unless customer opts in with masking.
- Full audit log of every query and API call.
- Encryption in transit and at rest.

---

## 7. UI and UX Wireframes

### 7.1 Pages
1. **Welcome and Connection Setup**
   - Tiles for Snowflake, Databricks, BigQuery, dbt, Fivetran, Matillion, Salesforce, ServiceNow, PagerDuty.
   - Minimal config and permissions test.
2. **Assessment Run Configuration**
   - Pick data domains, sampling policy, PII detection level, SLA targets.
3. **Run Progress**
   - Status, estimated remaining time, cost estimate.
4. **Results Overview**
   - Overall readiness gauge, dimension scores, top 5 risks, top 5 quick wins.
5. **Dimension Drill-down**
   - Metric cards with scores, evidence, and “why it matters.”
6. **Recommendations and Roadmap**
   - 30, 60, 90 day plan, 6 month track, effort vs impact matrix, vendor-aware options.
7. **Role-Based Summaries**
   - CFO, CRO, CIO, CDAO, CAIO, CTO tabs with tailored narratives.
8. **Exports**
   - PDF, CSV, Jira, Azure Boards.

### 7.2 Low-Fidelity Wireframe Sketches (ASCII)
```
Results Overview
+---------------------------------------------------------------+
| AI Readiness: 3.2 of 5    Trend: N/A (first run)             |
| [Data Quality 2.9] [Lineage 2.4] [Governance 3.1] [Security 3.6]
| [FinOps 3.0] [AI Governance 2.7] [Metadata 3.2] [People 2.8]  |
+---------------------------------------------------------------+
| Top Risks                                                     |
| 1) 24 percent of critical tables lack owners                  |
| 2) 31 percent PII unmasked in sandbox schemas                 |
| 3) Freshness SLA misses in 3 domains                          |
| 4) Idle compute waste approx 14 percent                        |
| 5) No eval datasets for 2 proposed AI use cases               |
+---------------------------------------------------------------+
| Quick Wins                                                    |
| A) Enforce ownership policy on top 50 tables                  |
| B) Add dbt tests for key uniqueness in 12 models              |
| C) Right-size Snowflake warehouses after business hours       |
| D) Turn on prompt logging in staging environment              |
| E) Create eval datasets with golden labels for 1 use case     |
+---------------------------------------------------------------+
Dimension Drill-down Card
+--------------------- Data Quality ----------------------------+
| Score: 2.9   Coverage: 78 percent schemas sampled            |
| Subscores: Completeness 65, Freshness 58, Uniqueness 72, ...  |
| Evidence: 24 queries, 3 API calls, last run 2025-11-11        |
| Why it matters:                                               |
|  High null rates in keys will break feature stores and evals. |
| How to fix:                                                   |
|  Add dbt tests to 12 models. Enforce SLA in Fivetran jobs.    |
+----------------------------------------------------------------
Recommendations Matrix
Impact ↑
 |        [A] Ownership policy
 |        [B] dbt uniqueness tests
 |  [C] Right-size compute
 |                   [D] Prompt logging
 |                               [E] Eval datasets
 +--------------------------------------------------> Effort →
```

---

## 8. Technical Design Notes

### 8.1 Implementation Stack
- **Backend:** Python or TypeScript services, FastAPI or Express, gRPC between services.
- **Data Store:** Postgres for metadata and results, object storage for artifacts, Parquet for large evidence sets.
- **Compute:** Containerized jobs on Kubernetes. Batch workers for profilers.
- **UI:** React with server or client side rendering, d3 for charts, Tailwind for layout.
- **Security:** Vault for secrets, cloud KMS, SSO via OIDC.
- **Orchestration:** Temporal or Argo Workflows for runs and retries.

### 8.2 Extensibility
- Connector SDK with clear interfaces.
- Metric DSL for adding new tests without code changes.
- Weighting profiles per industry compliance needs.

### 8.3 Cost and Performance Controls
- Sampling caps and query timeouts.
- Staggered scans outside business hours.
- Evidence retention policy with redaction.

### 8.4 Offline and Air-gapped Mode
- Ship a container bundle.
- Export reports to a secure file share.
- No outbound calls.

---

## 9. Risk Register and Mitigations
- **Data sensitivity:** Strict read-only access and masking by default.
- **API rate limits:** Queue and backoff, respect SaaS quotas.
- **Vendor differences:** Feature flags per platform to handle capability gaps.
- **False positives in PII:** Use ensemble of regex and ML, require human confirmation for high impact actions.

---

## 10. GTM, Packaging, and Pricing Hints
- **Entry package:** Fixed fee assessment for up to X assets and Y connectors including an executive report and two workshops.
- **Plus package:** Adds continuous mode for 90 days and guided remediation sprints.
- **Outcome:** Two AI pilot candidates with clean datasets and guardrails.

---

## 11. Roadmap and Timeline

### Phase 0 (0 to 2 weeks)
- Requirements finalization, connector stubs, metric DSL skeleton, initial UI frames.

### Phase 1 (2 to 6 weeks)
- Snowflake, dbt, Salesforce connectors. Core DQ metrics. Scoring engine v1. Results overview UI. PDF export v1.

### Phase 2 (6 to 10 weeks)
- Databricks, BigQuery, Fivetran, Matillion. Lineage coverage. Governance and security checks. Role-based summaries.

### Phase 3 (10 to 14 weeks)
- Recommendations engine with vendor awareness. Jira export, Azure Boards export. Effort vs impact matrix. FinOps metrics.

### Phase 4 (14 to 18 weeks)
- Private VPC deployment templates. Air-gapped build. Continuous mode preview.

### Milestone Gates
- **M1:** First complete end-to-end run on a pilot dataset.
- **M2:** Executive deck sign-off with one design partner.
- **M3:** Two quick-win pilots launched.

---

## 12. Sample Backlog
- Connector SDK and auth abstractions.
- Snowflake metadata harvester and sampling profiler.
- dbt manifest parser and test summarizer.
- Scoring engine with weight profiles and threshold mapping.
- PDF generator with templating and brand assets.
- Recommendations engine rules: Azure tenant, GCP tenant, OpenAI contract present, air-gapped.
- Role dashboards with drill-downs and evidence viewer.

---

## 13. What to Add Next
- **Data Contracts:** Optional detection of brittle interfaces and contract violations.
- **Feature Store Readiness:** Checks for versioning and documentation quality.
- **AI Risk:** Red teaming posture, evaluation harness readiness, hallucination guardrails.
- **Benchmark Library:** Side-by-side industry maturity baselines by sector.
- **Partner Motion:** Prebuilt offers with Snowflake, Databricks, and GCP to leverage credits.
- **Managed Option:** 90 day continuous mode with weekly guidance and a standing triage call.

---

## 14. Appendices

### 14.1 Sample SQL and Rules
- Completeness example: `SELECT COUNT(*) FROM table WHERE key IS NULL` to surface nulls.
- Freshness example: `SELECT MAX(ingest_timestamp) FROM table` compared to SLA hours.
- Uniqueness example: `SELECT COUNT(DISTINCT business_key) / COUNT(*)` on critical keys.
- Ownership coverage: Tables without entries in owner mapping tables.

### 14.2 Example Jira Epics
- Establish ownership policies.
- Implement dbt test coverage to 90 percent on critical models.
- FinOps right-sizing and idle compute reduction.

### 14.3 Example Executive Slide Outline
1. Current readiness gauge and dimension scores.
2. Why you score here.
3. Top five risks and quick wins.
4. 30-60-90 day plan.
5. Investment options by vendor and licensing posture.

---

## 15. Naming Options
- ReadyAI Data Assessment
- Aegis Data Readiness
- Prism AI Readiness by Decision Minds
- DM Aurora Readiness

---

## 16. Ownership and RACI (MVP)
- **Product:** Decision Minds Product Lead.
- **Engineering:** Connector Lead, Scoring Lead, UI Lead.
- **Design:** UX Lead.
- **Data Science:** PII and policy heuristics.
- **Alliances:** Cloud partner motions and credits.
- **Delivery:** Pilot customer engagement and report readouts.

---

## 17. Acceptance Test Scenarios
- Run against a demo Snowflake with 50 schemas, produce scores within 2 hours.
- Inject nulls and confirm completeness score drops with clear evidence.
- Remove owners and confirm governance score reflects the gap.
- Change SLA and confirm freshness logic updates scores.

---

## 18. Communication Templates
- Kickoff email to customer explaining data access, timeline, and deliverables.
- Executive summary template with role-specific highlights.
- Remediation backlog handover checklist.

---

## Streamlit Demo
A reference Streamlit application is available at `docs/data_ai_readiness_streamlit_demo.py`. The demo highlights readiness scores, remediation themes, and cross-platform benchmarking for Snowflake, Databricks, BigQuery, Looker, Power BI, Tableau, and other supported data connection platforms. Additional tabs visualize feature coverage, detailed check telemetry, persona-specific narratives, and an embedded accelerator specification that mirrors the MVP blueprint so stakeholders can validate progress in real time.

Launch it locally with:

```bash
streamlit run docs/data_ai_readiness_streamlit_demo.py
```

End of v1.0

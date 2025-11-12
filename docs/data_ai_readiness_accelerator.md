# Data & AI Readiness Accelerator

## Purpose
The Data & AI Readiness Accelerator helps organizations determine whether their existing data landscape is prepared to support upcoming AI workloads. The accelerator assesses the maturity of data sources, integration practices, and analytics tooling to provide a readiness score and a prioritized roadmap for remediation.

## Key Themes
- **Garbage in, garbage out:** AI outcomes depend on trustworthy, high-quality data. The accelerator emphasizes profiling and cleansing activities to reduce noise before model development.
- **Business intelligence as a lens:** Tableau, Power BI, and Looker models provide a rich view into how the organization currently consumes data. Their structure and usage patterns offer critical clues about downstream AI readiness across every analytics platform.
- **Data quality as the foundation:** Automated and manual checks focus on timeliness, completeness, consistency, and lineage so that AI teams inherit reliable datasets.

## Accelerator Workflow
1. **Discovery & Context**
   - Identify strategic AI initiatives and expected workloads.
   - Catalog critical data domains, owners, and integration points.
   - Review existing governance artifacts, including data dictionaries and catalog entries.
2. **Model & Pipeline Assessment**
   - Inspect Tableau, Power BI, and Looker semantic models, calculated fields, and refresh cadence.
   - Trace source systems feeding reporting models (e.g., Snowflake, Databricks, other cloud data warehouses) to evaluate schema stability and data freshness.
   - Evaluate existing ETL/ELT pipelines for observability coverage (logging, alerting, SLAs).
3. **Profiling & Quality Scoring**
   - Run automated data profiling to surface anomalies (null rates, duplicates, drift).
   - Measure data quality dimensions against defined KPIs (accuracy, completeness, conformity, integrity, timeliness).
   - Summarize findings in a readiness dashboard with actionable insights.
4. **Cleansing & Remediation Plan**
   - Prioritize remediation tasks based on business impact and implementation effort.
   - Recommend tooling or process changes for data cleansing (e.g., validation rules, deduplication strategies, stewardship workflows).
   - Define checkpoints to monitor improvements and prevent regression.
5. **Readiness Scoring & Roadmap**
   - Compute an overall readiness score with weighted metrics covering data, process, and governance.
   - Deliver an executive-ready report summarizing current posture, remediation roadmap, and investment guidance.

## Ten-Step Implementation Approach
1. **Executive Alignment & Value Framing**
   - Define the business outcomes each AI initiative must unlock and how readiness metrics will be consumed by sponsors.
   - Establish success criteria, reporting cadence, and escalation paths for risks uncovered during the assessment.
2. **Enterprise Data Inventory & Prioritization**
   - Compile a consolidated inventory of Snowflake databases, Databricks catalogs, and connected BI semantic models.
   - Classify assets by criticality, data domain, sensitivity, and downstream AI consumer to focus remediation on the most impactful datasets.
3. **Connectivity & Access Validation**
   - Confirm service accounts, network routes, and secret storage are configured for Snowflake, Databricks, Looker, Power BI, Tableau, and adjacent data connection platforms.
   - Execute smoke tests that validate authentication flows, query execution, and metadata harvesting across each source.
4. **Profiling Automation Setup**
   - Deploy automated profiling jobs that collect freshness, completeness, schema drift, and anomaly metrics at the table, dashboard, and AI feature level.
   - Parameterize frequency and thresholds so the same playbook can scale to new data products without manual intervention.
5. **Pipeline Observability & Incident Review**
   - Integrate pipeline metadata (Airflow, dbt, Delta Live Tables, etc.) to expose SLA breaches, failed jobs, and alert coverage.
   - Conduct a post-incident review to catalogue recurring failure modes and align them with remediation backlog items.
6. **Semantic Model Deep Dive**
   - Analyze LookML explores, Power BI datasets, and Tableau data sources for calculation accuracy, join cardinality, and refresh dependencies.
   - Flag BI elements that break AI readiness principles (e.g., manual extracts, unmanaged local files, or non-certified datasets).
7. **Governance & Compliance Assessment**
   - Evaluate ownership assignments, data classification tags, PII handling procedures, and approval workflows in catalog and BI governance layers.
   - Document regulatory obligations (GDPR, HIPAA, financial reporting) and map controls to readiness scoring.
8. **Remediation Sprint Planning**
   - Sequence cleansing, lineage enrichment, schema hardening, and access remediation tasks into 2–3 sprint waves with clear acceptance criteria.
   - Identify cross-team dependencies (security, platform engineering, analytics) and align capacity to sustain remediation momentum.
9. **AI Feature & Model Enablement**
   - Validate that curated datasets meet the statistical stability and latency requirements for downstream model training and inference.
   - Capture feature documentation, drift monitoring strategies, and retraining triggers that will consume cleansed data.
10. **Continuous Monitoring & Feedback Loop**
    - Configure dashboards, alerts, and service-level objectives that keep readiness metrics evergreen.
    - Host monthly operating reviews to adapt scoring weights, recalibrate remediation priorities, and showcase value delivered.

## Extended Features and Checks
- **Automated Freshness Validation:** Hourly freshness probes for priority Snowflake and Databricks tables with alert thresholds tied to AI retraining windows.
- **Schema Drift Monitoring:** Version-controlled snapshots of schemas and semantic layer definitions to detect breaking changes before models fail.
- **PII & Security Guardrails:** Integration with data classification services to confirm sensitive fields remain masked in BI tools and downstream feature stores.
- **Observability Coverage Scoring:** Weighted scoring of logging, tracing, and alerting coverage across ingestion, transformation, and serving layers.
- **Bias & Fairness Screen:** Optional statistical checks that surface representation gaps within training datasets prior to AI deployment.
- **Self-Service Lineage Explorer:** Interactive lineage visualizations that stitch together Snowflake objects, dbt nodes, and Tableau/Power BI/Looker assets.
- **Remediation Backlog Analytics:** Burn-up charts that quantify throughput, age, and impact of outstanding data quality tasks.
- **Readiness Scenario Modeling:** Sensitivity analysis that demonstrates how improving a single metric (e.g., governance coverage) influences the composite AI Readiness Score.
- **Platform Health Scorecards:** Standardized reports for Snowflake, Databricks, Looker, Power BI, Tableau, and other connectors summarizing SLA adherence and incident trends.
- **Adoption & Enablement Tracking:** Insight into steward training completion, certified dataset adoption, and BI feature usage to verify operational uptake.

## Metrics & KPIs
- **Data Quality Index (DQI):** Composite score aggregating accuracy, completeness, and timeliness metrics.
- **Model Trustworthiness:** Percentage of critical Tableau/Power BI dashboards backed by certified datasets.
- **Pipeline Reliability:** Success rate and mean time to recovery (MTTR) for production data pipelines.
- **Governance Coverage:** Portion of priority datasets with documented owners, lineage, and access controls.
- **AI Readiness Score:** Weighted rating (0-100) that captures data quality, operational maturity, and governance alignment.

## Professional Services Offering
- **Readiness Assessment Sprint (2-4 weeks):** Rapid evaluation leveraging the accelerator toolkit to score current-state readiness.
- **Remediation Implementation:** Hands-on support to execute cleansing, pipeline hardening, and governance enhancements.
- **Change Management & Enablement:** Workshops for data stewards and analytics teams to maintain AI-ready data practices.
- **Ongoing Health Monitoring:** Optional managed service to track KPIs, refresh readiness scores, and surface emerging risks.

## Deliverables
- Executive summary highlighting AI readiness posture and key risks.
- Detailed findings report with data quality metrics, dashboard model review, and remediation backlog.
- Tableau/Power BI/Looker model lineage diagrams and dependency mapping.
- Prioritized roadmap with effort estimates, sequencing, and success criteria.

## Benefits
- Accelerated path to launching AI workloads with confidence in data reliability.
- Clear visibility into BI model dependencies and potential technical debt.
- Quantifiable metrics that help align stakeholders on investment priorities.
- Sustainable data quality practices that reduce rework and improve analytics outcomes.

## Platform Coverage
- Native connectivity to Snowflake, Databricks, and other leading cloud data platforms ensures profiling and quality scoring run against production-grade datasets.
- Accelerator playbooks extend to Tableau, Power BI, Looker, and additional BI tools and data connection platforms that support SQL or semantic-layer integrations.
- Flexible ingestion patterns support REST APIs, flat files, on-premises databases, and emerging data sources to future-proof AI readiness assessments.

## Connecting to Core Analytics Platforms
### Snowflake
1. Configure a Snowflake warehouse and service user with the `USAGE` and `SELECT` privileges on the databases and schemas you plan to profile.
2. Store Snowflake connection secrets (account, user, password/private key, role, warehouse, database, schema) in your secret manager or Streamlit `secrets.toml` file.
3. Use the native Snowflake Python connector (`snowflake-connector-python`) or your preferred orchestration tool to execute profiling queries and materialize accelerator metrics.
4. Register the connection in the accelerator’s configuration so downstream Tableau, Power BI, and Looker lineage jobs can trace Snowflake objects back to their AI readiness scores.
5. Optional: Enable Snowflake Object Tagging and Access History to enrich governance lineage, sensitivity classifications, and anomaly detection within the accelerator.

### Databricks
1. Generate a Databricks personal access token (PAT) scoped to the workspace hosting Delta Lake tables that feed AI workloads.
2. Capture the workspace URL, cluster or SQL warehouse identifier, and PAT inside secure configuration storage.
3. For notebook-driven pipelines, leverage the Databricks REST API or `databricks-sql-connector` to query Delta tables and collect quality statistics.
4. When using Unity Catalog, enable lineage exports so the accelerator can map Delta Live Tables to Tableau, Power BI, and Looker semantic layers.
5. Configure Delta Expectations or Great Expectations suites to enforce validation rules before curated tables are consumed by AI workloads.

### Looker (Looker Studio / LookML Models)
1. Create a Looker API3 client ID and secret with read-only permissions to explore metadata, model files, and dashboards.
2. Populate the accelerator configuration with the Looker host, port, API credentials, and target LookML repositories.
3. Utilize the Looker SDK (`looker-sdk`) to enumerate explores, join paths, and field usage metrics that inform readiness scoring.
4. Schedule accelerator sync jobs to align Looker model refresh cycles with Snowflake/Databricks data quality snapshots.
5. Capture LookML Git repository references and deploy webhook triggers to surface unreviewed changes or validation failures that could impact AI KPIs.

### Power BI
1. Register an Azure AD application with delegated permissions for the Power BI Service (Dataset.Read.All, Capacity.Read.All, Workspace.Read.All at minimum).
2. Capture the tenant ID, client ID, and client secret/certificate in the accelerator secrets store.
3. Authenticate via the `msal` library and call the Power BI REST APIs to extract dataset refresh history, lineage links, and workspace governance metadata.
4. For on-premises data gateways, coordinate with gateway admins to retrieve source connection details and incorporate them into readiness profiling.
5. Enable Fabric Monitoring or Azure Log Analytics connectors to unify refresh failures, gateway latency, and capacity utilization metrics within the accelerator.

### Tableau
1. Provision a Tableau Server or Tableau Cloud service account with Explorer or higher permissions for the relevant sites and projects.
2. Store Tableau credentials or personal access tokens securely; include the server URL, site ID, and token name/secret in configuration.
3. Use the Tableau REST API or Metadata API (GraphQL) via the `tableauserverclient` package to inventory workbooks, data sources, and refresh schedules.
4. Enable Tableau Bridge or direct connections so accelerator profiling can trace workbook dependencies back to Snowflake, Databricks, and other upstream systems.
5. Activate Data Quality Warnings and virtual connections to publish readiness flags directly into business-critical workbooks and data catalogs.

## Next Steps if Adopted
1. Secure executive sponsorship and data access approvals.
2. Schedule discovery sessions with data owners and analytics leads.
3. Provision environments for profiling, quality scoring, and dashboard analysis.
4. Launch the assessment sprint and socialize preliminary findings.
5. Iterate on remediation plan with cross-functional stakeholders.

## Streamlit Demo
A reference Streamlit application is available at `docs/data_ai_readiness_streamlit_demo.py`. The demo highlights readiness scores, remediation themes, and cross-platform benchmarking for Snowflake, Databricks, Looker, Power BI, Tableau, and other supported data connection platforms. Additional tabs visualize feature coverage, detailed check telemetry, and the ten-step delivery plan so stakeholders can validate progress in real time. Launch it locally with:
A reference Streamlit application is available at `docs/data_ai_readiness_streamlit_demo.py`. The demo highlights readiness scores, remediation themes, and cross-platform benchmarking for Snowflake, Databricks, Looker, Power BI, Tableau, and other supported data connection platforms. Launch it locally with:

```bash
streamlit run docs/data_ai_readiness_streamlit_demo.py
```

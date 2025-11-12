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

## Next Steps if Adopted
1. Secure executive sponsorship and data access approvals.
2. Schedule discovery sessions with data owners and analytics leads.
3. Provision environments for profiling, quality scoring, and dashboard analysis.
4. Launch the assessment sprint and socialize preliminary findings.
5. Iterate on remediation plan with cross-functional stakeholders.

## Streamlit Demo
A reference Streamlit application is available at `docs/data_ai_readiness_streamlit_demo.py`. The demo highlights readiness scores, remediation themes, and cross-platform benchmarking for Snowflake, Databricks, Looker, Power BI, Tableau, and other supported data connection platforms. Launch it locally with:

```bash
streamlit run docs/data_ai_readiness_streamlit_demo.py
```

"""Streamlit demo for the Decision Minds AI Readiness Assessment Accelerator."""
from __future__ import annotations

import textwrap
from dataclasses import dataclass
from typing import Dict, List, Tuple

import pandas as pd
import streamlit as st


@dataclass(frozen=True)
class PlatformReadiness:
    """Represents readiness insight for a single analytics platform."""

    name: str
    overall_score: float
    dimension_scores: Dict[str, float]
    metrics_100: Dict[str, int]
    top_risks: List[str]
    quick_wins: List[str]
    feature_adoption: Dict[str, bool]
    observability_checks: Dict[str, str]
    persona_notes: Dict[str, str]
    connectors: List[str]
    success_metrics: Dict[str, str]

    def dimension_frame(self) -> pd.DataFrame:
        """Return a dataframe summarizing dimension scores."""

        rows = []
        for dimension, score in self.dimension_scores.items():
            rows.append(
                {
                    "Dimension": dimension,
                    "Score (0-5)": round(score, 2),
                    "Percent": round(score / 5 * 100, 1),
                }
            )
        return pd.DataFrame(rows).sort_values("Score (0-5)", ascending=False).reset_index(drop=True)

    def metric_frame(self) -> pd.DataFrame:
        """Return KPI metrics normalised on a 0-100 scale."""

        return (
            pd.DataFrame(
                [
                    {
                        "Metric": metric,
                        "Score (0-100)": value,
                    }
                    for metric, value in self.metrics_100.items()
                ]
            )
            .set_index("Metric")
            .sort_values("Score (0-100)", ascending=False)
        )


DIMENSIONS: Tuple[str, ...] = (
    "Data Quality",
    "Lineage & Observability",
    "Governance & Access",
    "Privacy & Security",
    "Metadata & Documentation",
    "Platform Reliability & FinOps",
    "Model Governance Readiness",
    "People & Process",
)


INDUSTRY_BASELINE = {
    "Data Quality": 2.6,
    "Lineage & Observability": 2.3,
    "Governance & Access": 2.8,
    "Privacy & Security": 2.9,
    "Metadata & Documentation": 2.7,
    "Platform Reliability & FinOps": 2.5,
    "Model Governance Readiness": 2.4,
    "People & Process": 2.6,
}


PLATFORM_PROFILES: Dict[str, PlatformReadiness] = {
    "Snowflake": PlatformReadiness(
        name="Snowflake",
        overall_score=4.1,
        dimension_scores={
            "Data Quality": 4.4,
            "Lineage & Observability": 4.0,
            "Governance & Access": 3.9,
            "Privacy & Security": 4.2,
            "Metadata & Documentation": 3.8,
            "Platform Reliability & FinOps": 4.3,
            "Model Governance Readiness": 3.7,
            "People & Process": 3.6,
        },
        metrics_100={
            "Data Quality Index": 88,
            "Pipeline Reliability": 92,
            "Governance Coverage": 82,
            "AI Readiness Score": 84,
            "FinOps Efficiency": 79,
        },
        top_risks=[
            "Long-tail schemas missing stewardship assignments.",
            "Data quality incident runbooks not yet automated for after-hours response.",
            "Prompt logging for advanced analytics limited to pilot environments.",
        ],
        quick_wins=[
            "Expand Great Expectations suites to partner zones.",
            "Automate Object Tagging to flag PII and lineage gaps.",
            "Bundle idle warehouse suspension with FinOps alerts.",
        ],
        feature_adoption={
            "Automated Freshness Monitoring": True,
            "Schema Drift Protection": True,
            "PII Guardrails": True,
            "Self-Service Lineage": True,
            "Bias & Fairness Screening": False,
            "Policy Evidence Archive": True,
        },
        observability_checks={
            "Freshness Lag (hrs)": "0.4",
            "Schema Drift Alerts (30d)": "0",
            "Critical DQ Tests": "58/60",
            "Warehouse Idle %": "11",
            "Open Remediation Items": "2",
        },
        persona_notes={
            "CFO": "Spend is governed by auto-suspend and chargeback to domains; highlight 11% idle capacity recovery.",
            "CRO": "Lineage completeness supports regulatory stress testing with evidence for mission-critical tables.",
            "CIO/CTO": "Platform SLAs exceed 99.9% with unified IAM via SCIM; keep investing in drift automation.",
            "CDAO": "DQ coverage above 85% across curated marts; expand stewardship to long-tail schemas.",
            "CAIO": "Model governance pack ready for low-risk pilots; accelerate prompt logging rollout to prod teams.",
        },
        connectors=[
            "Snowflake ACCOUNT_USAGE",
            "dbt Cloud",
            "Fivetran",
            "Power BI lineage API",
            "Tableau Metadata API",
        ],
        success_metrics={
            "Run Duration": "96 minutes for 120 schemas",
            "Evidence Samples": "12k rows profiled",
            "Quick Wins Identified": "14",
        },
    ),
    "Databricks": PlatformReadiness(
        name="Databricks",
        overall_score=3.9,
        dimension_scores={
            "Data Quality": 4.0,
            "Lineage & Observability": 3.8,
            "Governance & Access": 3.6,
            "Privacy & Security": 3.7,
            "Metadata & Documentation": 3.5,
            "Platform Reliability & FinOps": 4.1,
            "Model Governance Readiness": 3.9,
            "People & Process": 3.4,
        },
        metrics_100={
            "Data Quality Index": 81,
            "Pipeline Reliability": 88,
            "Governance Coverage": 77,
            "AI Readiness Score": 80,
            "FinOps Efficiency": 83,
        },
        top_risks=[
            "Alert runbooks for Delta Live Tables require on-call rotation updates.",
            "Unity Catalog tagging incomplete for gold layer assets.",
            "Great Expectations suites not standardized for partner notebooks.",
        ],
        quick_wins=[
            "Deploy catalog tagging automation via Unity Catalog APIs.",
            "Bundle pipeline alerts into PagerDuty service map.",
            "Publish MLflow evaluation templates for shared feature store usage.",
        ],
        feature_adoption={
            "Automated Freshness Monitoring": True,
            "Schema Drift Protection": True,
            "PII Guardrails": False,
            "Self-Service Lineage": True,
            "Bias & Fairness Screening": True,
            "Policy Evidence Archive": True,
        },
        observability_checks={
            "Freshness Lag (hrs)": "1.2",
            "Schema Drift Alerts (30d)": "3",
            "Critical DQ Tests": "46/55",
            "Warehouse Idle %": "9",
            "Open Remediation Items": "5",
        },
        persona_notes={
            "CFO": "FinOps dashboard exposes right-size opportunities on interactive clusters.",
            "CRO": "Audit logs aggregated but 18% partner notebooks bypass review workflow.",
            "CIO/CTO": "Medallion architecture locked in; unify PAT rotation through Secrets scope.",
            "CDAO": "Shared feature store fosters reuse; tighten documentation for gold tables.",
            "CAIO": "MLflow evaluations and prompt guardrails available for four pilot models.",
        },
        connectors=[
            "Databricks REST API",
            "Unity Catalog",
            "Delta Live Tables",
            "ServiceNow",
            "PagerDuty",
        ],
        success_metrics={
            "Run Duration": "118 minutes for 95 workspaces",
            "Evidence Samples": "9.4k tables profiled",
            "Quick Wins Identified": "17",
        },
    ),
    "BigQuery": PlatformReadiness(
        name="BigQuery",
        overall_score=3.7,
        dimension_scores={
            "Data Quality": 3.6,
            "Lineage & Observability": 3.5,
            "Governance & Access": 3.8,
            "Privacy & Security": 3.9,
            "Metadata & Documentation": 3.4,
            "Platform Reliability & FinOps": 3.7,
            "Model Governance Readiness": 3.5,
            "People & Process": 3.2,
        },
        metrics_100={
            "Data Quality Index": 78,
            "Pipeline Reliability": 82,
            "Governance Coverage": 80,
            "AI Readiness Score": 76,
            "FinOps Efficiency": 74,
        },
        top_risks=[
            "Limited lineage coverage for Looker Studio dashboards.",
            "Manual approvals required for data classification updates.",
            "Spend spikes when ad-hoc analysts bypass slot reservations.",
        ],
        quick_wins=[
            "Enable Data Catalog automatic tagging rules for sensitive fields.",
            "Roll out column-level access policies to sandbox projects.",
            "Automate slot scaling policies with demand forecasting.",
        ],
        feature_adoption={
            "Automated Freshness Monitoring": True,
            "Schema Drift Protection": False,
            "PII Guardrails": True,
            "Self-Service Lineage": True,
            "Bias & Fairness Screening": False,
            "Policy Evidence Archive": True,
        },
        observability_checks={
            "Freshness Lag (hrs)": "2.3",
            "Schema Drift Alerts (30d)": "4",
            "Critical DQ Tests": "41/54",
            "Warehouse Idle %": "14",
            "Open Remediation Items": "8",
        },
        persona_notes={
            "CFO": "Slot utilization trending 14% idle; feed into chargeback to recover credits.",
            "CRO": "Access transparency logs captured; expand lineage for regulated dashboards.",
            "CIO/CTO": "Project guardrails in place; accelerate policy automation via Terraform.",
            "CDAO": "Data Catalog adoption growing; invest in glossary stewardship circles.",
            "CAIO": "Vertex AI integration ready for curated features; add fairness checks to high-risk models.",
        },
        connectors=[
            "BigQuery INFORMATION_SCHEMA",
            "Data Catalog",
            "Looker Studio",
            "Matillion",
            "Salesforce",
        ],
        success_metrics={
            "Run Duration": "84 minutes across 18 projects",
            "Evidence Samples": "7.1k tables profiled",
            "Quick Wins Identified": "12",
        },
    ),
    "Looker": PlatformReadiness(
        name="Looker",
        overall_score=3.4,
        dimension_scores={
            "Data Quality": 3.2,
            "Lineage & Observability": 3.5,
            "Governance & Access": 3.9,
            "Privacy & Security": 3.7,
            "Metadata & Documentation": 4.0,
            "Platform Reliability & FinOps": 3.3,
            "Model Governance Readiness": 3.1,
            "People & Process": 3.0,
        },
        metrics_100={
            "Data Quality Index": 74,
            "Pipeline Reliability": 79,
            "Governance Coverage": 82,
            "AI Readiness Score": 76,
            "FinOps Efficiency": 70,
        },
        top_risks=[
            "Visual regression testing not automated for key dashboards.",
            "Manual explores maintain separate definitions for the same KPI.",
            "Deploy pipeline lacks security review sign-off gates.",
        ],
        quick_wins=[
            "Implement Spectacles for automated LookML validation.",
            "Rationalize duplicate explores into governed models.",
            "Add peer review requirements before production deploys.",
        ],
        feature_adoption={
            "Automated Freshness Monitoring": False,
            "Schema Drift Protection": True,
            "PII Guardrails": True,
            "Self-Service Lineage": True,
            "Bias & Fairness Screening": False,
            "Policy Evidence Archive": False,
        },
        observability_checks={
            "Freshness Lag (hrs)": "3.5",
            "Schema Drift Alerts (30d)": "4",
            "Critical DQ Tests": "38/50",
            "Warehouse Idle %": "18",
            "Open Remediation Items": "7",
        },
        persona_notes={
            "CFO": "Dashboard trust hinges on aligning KPI logic; note backlog of duplicate explores.",
            "CRO": "Access is least-privilege but add evidence archiving for compliance.",
            "CIO/CTO": "GitOps pipeline exists; enforce review automation for production merges.",
            "CDAO": "Documentation strong; focus on automated testing to raise DQ.",
            "CAIO": "AI-ready extracts rely on manual refresh; connect to orchestrated pipelines.",
        },
        connectors=[
            "Looker SDK",
            "GitHub Webhooks",
            "BigQuery",
            "Snowflake",
            "dbt manifest",
        ],
        success_metrics={
            "Run Duration": "42 minutes for 210 explores",
            "Evidence Samples": "4.5k fields assessed",
            "Quick Wins Identified": "10",
        },
    ),
    "Power BI": PlatformReadiness(
        name="Power BI",
        overall_score=3.2,
        dimension_scores={
            "Data Quality": 3.0,
            "Lineage & Observability": 3.1,
            "Governance & Access": 3.3,
            "Privacy & Security": 3.4,
            "Metadata & Documentation": 3.2,
            "Platform Reliability & FinOps": 2.9,
            "Model Governance Readiness": 3.1,
            "People & Process": 2.8,
        },
        metrics_100={
            "Data Quality Index": 77,
            "Pipeline Reliability": 75,
            "Governance Coverage": 69,
            "AI Readiness Score": 72,
            "FinOps Efficiency": 68,
        },
        top_risks=[
            "Premium capacity utilization spikes without alerting.",
            "Manually refreshed data sources feeding executive reports.",
            "Certified dataset adoption below 45% of consumption.",
        ],
        quick_wins=[
            "Automate gateway health checks via Azure Monitor.",
            "Enable deployment pipelines for governed workspaces.",
            "Publish dataset endorsement playbook with stewardship SLAs.",
        ],
        feature_adoption={
            "Automated Freshness Monitoring": True,
            "Schema Drift Protection": False,
            "PII Guardrails": True,
            "Self-Service Lineage": False,
            "Bias & Fairness Screening": True,
            "Policy Evidence Archive": False,
        },
        observability_checks={
            "Freshness Lag (hrs)": "5.0",
            "Schema Drift Alerts (30d)": "6",
            "Critical DQ Tests": "29/45",
            "Warehouse Idle %": "21",
            "Open Remediation Items": "11",
        },
        persona_notes={
            "CFO": "Fabric licensing allows cost attribution; need alerts for 21% idle premium capacity.",
            "CRO": "Compliance guardrails in place but manual refresh introduces audit gaps.",
            "CIO/CTO": "Deployment pipelines exist; expand automation for dataset refresh.",
            "CDAO": "Certified dataset adoption low; intensify stewardship office hours.",
            "CAIO": "Prompt logging ready on pilot chatbots; dataset freshness still a blocker.",
        },
        connectors=[
            "Power BI REST API",
            "Azure Log Analytics",
            "Azure AD",
            "Snowflake",
            "Databricks",
        ],
        success_metrics={
            "Run Duration": "56 minutes across 48 workspaces",
            "Evidence Samples": "3.8k datasets analyzed",
            "Quick Wins Identified": "15",
        },
    ),
    "Tableau": PlatformReadiness(
        name="Tableau",
        overall_score=3.6,
        dimension_scores={
            "Data Quality": 3.8,
            "Lineage & Observability": 3.7,
            "Governance & Access": 3.4,
            "Privacy & Security": 3.5,
            "Metadata & Documentation": 3.6,
            "Platform Reliability & FinOps": 3.2,
            "Model Governance Readiness": 3.4,
            "People & Process": 3.3,
        },
        metrics_100={
            "Data Quality Index": 83,
            "Pipeline Reliability": 85,
            "Governance Coverage": 71,
            "AI Readiness Score": 79,
            "FinOps Efficiency": 72,
        },
        top_risks=[
            "Hyper extracts rely on manual dedupe scripts before publishing.",
            "Data Management add-on adoption incomplete for finance domain.",
            "Quality flags not consistently surfaced to downstream dashboards.",
        ],
        quick_wins=[
            "Enable virtual connections with centralized policies.",
            "Automate deduplication via dbt seeds before Hyper refresh.",
            "Push quality warnings into certified dashboards via REST API.",
        ],
        feature_adoption={
            "Automated Freshness Monitoring": True,
            "Schema Drift Protection": False,
            "PII Guardrails": True,
            "Self-Service Lineage": True,
            "Bias & Fairness Screening": False,
            "Policy Evidence Archive": True,
        },
        observability_checks={
            "Freshness Lag (hrs)": "2.1",
            "Schema Drift Alerts (30d)": "2",
            "Critical DQ Tests": "41/52",
            "Warehouse Idle %": "16",
            "Open Remediation Items": "6",
        },
        persona_notes={
            "CFO": "Executive scorecards depend on Hyper extracts; highlight dedupe automation ROI.",
            "CRO": "Quality warnings available; embed them in regulated dashboards.",
            "CIO/CTO": "Server stable but upgrade SSO integration for future scale.",
            "CDAO": "Stewardship improving; accelerate adoption of Data Management add-on.",
            "CAIO": "Tableau Pulse pilots can surface AI readiness gaps to analysts in context.",
        },
        connectors=[
            "Tableau REST API",
            "Metadata API",
            "Snowflake",
            "Databricks",
            "ServiceNow",
        ],
        success_metrics={
            "Run Duration": "64 minutes across 32 sites",
            "Evidence Samples": "5.6k workbooks analyzed",
            "Quick Wins Identified": "13",
        },
    ),
}


PERSONA_ORDER = ["CFO", "CRO", "CIO/CTO", "CDAO", "CAIO"]


CONNECTOR_SCOPE: List[Tuple[str, List[str]]] = [
    (
        "Data Platforms",
        ["Snowflake", "Databricks", "BigQuery"],
    ),
    (
        "Pipelines",
        ["dbt", "Fivetran", "Matillion"],
    ),
    (
        "SaaS Systems",
        ["Salesforce", "ServiceNow", "PagerDuty"],
    ),
    (
        "Security & IAM Signals",
        ["Cloud IAM snapshots", "SSO groups", "Service principals"],
    ),
    (
        "Metadata Sources",
        [
            "Native INFORMATION_SCHEMA",
            "Unity Catalog",
            "BigQuery INFORMATION_SCHEMA",
            "dbt manifest",
            "Fivetran APIs",
            "Matillion APIs",
        ],
    ),
]

ACCESS_MODEL_NOTES = (
    "Read-only OAuth or service account credentials are used with least privilege. Sampling strategies are configurable per "
    "source, and PII discovery is optional but encouraged."
)

MATURITY_DESCRIPTIONS: Dict[str, str] = {
    "Data Quality": "Completeness, accuracy, consistency, timeliness, uniqueness, validity.",
    "Lineage & Observability": "Coverage of upstream/downstream dependencies, freshness SLAs, incident MTTR.",
    "Governance & Access": "Policies, role-based access, least privilege alignment, approvals, auditability.",
    "Privacy & Security": "PII detection, masking strategies, key management, secrets hygiene.",
    "Metadata & Documentation": "Table/column documentation, glossary links, ownership clarity.",
    "Platform Reliability & FinOps": "Cost allocation, auto-suspend, query queuing, warehouse sizing, job success rate.",
    "Model Governance Readiness": "Prompt logging readiness, feature store hygiene, dataset versioning, evaluation frameworks.",
    "People & Process": "RACI clarity, change management, SDLC for data/AI, incident runbooks.",
}

MATURITY_BANDS = [
    {"Score": "0 to 1", "Description": "Ad hoc and opaque"},
    {"Score": "2", "Description": "Partially defined with gaps"},
    {"Score": "3", "Description": "Defined, measured, but inconsistent"},
    {"Score": "4", "Description": "Managed and automated in key areas"},
    {"Score": "5", "Description": "Optimized, automated, auditable, cost-efficient"},
]

METRIC_LIBRARY: Dict[str, List[str]] = {
    "Quality": [
        "% columns with tests",
        "Failed test rate",
        "Null rate",
        "Freshness lag",
        "Duplicate key rate",
        "Schema drift frequency",
    ],
    "Lineage": [
        "% assets with upstream lineage",
        "% jobs with success SLO",
        "Average data freshness",
        "Number of undocumented critical tables",
    ],
    "Governance": [
        "% PII columns masked",
        "% tables with owners",
        "% users with least privilege",
        "Number of dormant service accounts",
    ],
    "Security": [
        "Credential rotation age",
        "Keys without rotation policy",
        "Public network access flags",
        "Cross-account access audit",
    ],
    "FinOps": [
        "Spend by domain",
        "% compute idle time",
        "Right-sizing opportunities",
        "Failed query cost",
        "Top N costly transformations",
    ],
    "AI Readiness": [
        "% datasets with quality gates",
        "% datasets versioned",
        "Presence of eval datasets",
        "Prompt and output logging readiness",
    ],
}

EVIDENCE_PRACTICES = [
    "For each score, show sampled evidence, test results, and how every metric rolls up.",
    "Provide 'Why this matters' and 'How to fix' inline with backlog items and effort estimates.",
]

RECOMMENDATION_NOTES = [
    "Vendor-aware advice aligns to Microsoft Copilot & Fabric for Azure tenants, Vertex AI & Gemini for GCP, and OpenAI options when contracts exist.",
    "Air-gapped or regulated deployments recommend offline or private endpoints when policies require it.",
    "Outputs include a 30/60/90-day plan plus a 6-month modernization track with epics and stories.",
]

DELIVERABLES = [
    "Executive PDF deck",
    "Role-based scorecards",
    "Backlog CSV",
    "Jira or Azure Boards import",
    "Signed architecture proposal for two quick-win pilots",
]

OUT_OF_SCOPE = [
    "Automated remediation—guidance and backlogs only",
    "Real-time monitoring at scale (post-MVP continuous mode)",
    "Proprietary catalog replacement",
]

SUCCESS_CRITERIA = [
    "Assessment completes within 1-2 business days for up to 10 data domains and up to 3 platforms.",
    "Scores and evidence are reproducible with an identical configuration rerun.",
    "Executive deck generates role-specific summaries automatically.",
    "At least two quick-win pilots are identified with clear acceptance tests.",
]

CONNECTOR_REQUIREMENTS: Dict[str, str] = {
    "Snowflake": "Read-only role with ACCOUNT_USAGE plus database read on selected schemas.",
    "Databricks": "Unity Catalog metadata, job & cluster logs, audit logs where available.",
    "BigQuery": "Access to INFORMATION_SCHEMA and Data Catalog metadata.",
    "dbt": "Parse manifest.json and run results for tests and exposures.",
    "Fivetran & Matillion": "Ingest job status, failure rates, schedules, API metadata.",
    "SaaS": "Salesforce object counts, field metadata, DQ sampling, API limits; ServiceNow CMDB completeness; PagerDuty incident metrics.",
}

SCORING_LOGIC = [
    "Completeness subscore = 100 - min(100, null_rate_percent × weight_nulls) with special handling for core keys.",
    "Freshness subscore = percentile rank of hours_since_last_load versus SLA plus schedule adherence.",
    "Lineage coverage subscore = assets_with_lineage ÷ total_critical_assets × 100, adjusted by job success SLO.",
    "Governance subscore = average of ownership coverage, mask coverage on PII, least privilege alignment, audit log availability.",
    "FinOps subscore = blend of idle compute percent, right-sizing opportunities found, failed query cost percent.",
    "AI Readiness subscore = percent of datasets with tests/versioning, presence of eval datasets, prompt logging readiness.",
]

MATURITY_MAPPING = [
    {"Score": "0-40", "Maturity": 1},
    {"Score": "41-55", "Maturity": 2},
    {"Score": "56-70", "Maturity": 3},
    {"Score": "71-85", "Maturity": 4},
    {"Score": "86-100", "Maturity": 5},
]

EVIDENCE_MODEL = [
    "Each metric stores query text or API references, sample counts, timestamps, and redacted examples.",
    "Evidence exports to PDF and JSON for audit trails.",
    "All queries run with sampling limits to manage cost.",
]

ROLE_VIEWS: Dict[str, List[str]] = {
    "CFO": ["Cost waste", "Right-sizing opportunities", "Spend by domain", "Risk of compliance penalties"],
    "CRO": ["Lineage completeness on risk datasets", "Model explainability posture", "Controls and audit logs"],
    "CIO/CTO": ["Platform posture", "Modernization gaps", "IAM hygiene", "Vendor leverage"],
    "CDAO": ["DQ test coverage", "Glossary & ownership", "Prioritized data domains"],
    "CAIO": ["AI-ready datasets", "Evaluation readiness", "Safe model options by data sensitivity"],
}

EXPORT_OPTIONS = ["PDF", "CSV", "Jira import", "Azure Boards import", "Optional Slack or Teams summary"]

ARCH_COMPONENTS = [
    "Connector Layer — pluggable, read-only, least privilege",
    "Metadata Harvester — schemas, stats, lineage, run history, users, roles",
    "Profiler & Sampler — column profiling, freshness checks, uniqueness tests, schema drift",
    "Policy & PII Detector — regex/ML matchers, classification, policy cross-checks",
    "Scoring Engine — compute subscores, apply weightings & thresholds",
    "Recommendation Engine — map gaps to fixes, estimate effort, align to vendor stack",
    "Report Generator — build PDFs, role scorecards, CSV backlogs",
    "Dashboard Service — interactive UI with drill-downs and evidence",
    "Security & Secrets — KMS integration, vault for credentials, audit logging",
    "Orchestrator — run assessments, schedule reruns, track state",
]

DATA_FLOW = [
    "Ingest metadata and samples via connectors",
    "Store results in a read-only staging store",
    "Run profilers and policy engines",
    "Compute scores",
    "Materialize views for UI and exports",
    "Generate reports and remediation backlog",
]

DEPLOYMENT_OPTIONS = [
    "Cloud SaaS — Decision Minds hosted with tenant isolation",
    "Private VPC — customer cloud via containers and Terraform",
    "Air-gapped — offline mode with limited connectors and secure artifact transfer",
]

SECURITY_COMPLIANCE = [
    "No raw sensitive data leaves the customer boundary.",
    "Sampling excludes sensitive columns unless masked opt-in.",
    "Full audit log of every query and API call.",
    "Encryption enforced in transit and at rest.",
]

UI_PAGES = [
    "Welcome & Connection Setup — tiles for Snowflake, Databricks, BigQuery, dbt, Fivetran, Matillion, SFDC, ServiceNow, PagerDuty with minimal config and permissions tests.",
    "Assessment Run Configuration — choose data domains, sampling policy, PII detection level, SLA targets.",
    "Run Progress — status, estimated remaining time, cost estimate.",
    "Results Overview — readiness gauge, dimension scores, top 5 risks, top 5 quick wins.",
    "Dimension Drill-down — metric cards with scores, evidence, and why it matters.",
    "Recommendations & Roadmap — 30/60/90-day plan, 6-month track, effort vs impact matrix, vendor-aware options.",
    "Role-Based Summaries — CFO, CRO, CIO, CDAO, CAIO, CTO narratives.",
    "Exports — PDF, CSV, Jira, Azure Boards.",
]

WIREFRAME_ASCII = textwrap.dedent(
    """
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
    """
).strip()

IMPLEMENTATION_STACK = {
    "Backend": "Python or TypeScript services, FastAPI or Express, gRPC between services",
    "Data Store": "Postgres for metadata/results, object storage for artifacts, Parquet for large evidence sets",
    "Compute": "Containerized jobs on Kubernetes with batch profilers",
    "UI": "React with server/client rendering, d3 visualizations, Tailwind layout",
    "Security": "Vault for secrets, cloud KMS, SSO via OIDC",
    "Orchestration": "Temporal or Argo Workflows for runs and retries",
}

EXTENSIBILITY = [
    "Connector SDK with clear interfaces",
    "Metric DSL for adding new tests without code changes",
    "Weighting profiles tuned per industry/compliance",
]

PERFORMANCE_CONTROLS = [
    "Sampling caps and query timeouts",
    "Staggered scans outside business hours",
    "Evidence retention policy with redaction",
]

OFFLINE_MODE = [
    "Ship a container bundle",
    "Export reports to a secure file share",
    "No outbound calls",
]

RISK_REGISTER = [
    ("Data sensitivity", "Strict read-only access and masking by default"),
    ("API rate limits", "Queue/backoff patterns respecting SaaS quotas"),
    ("Vendor differences", "Feature flags per platform to handle capability gaps"),
    ("False positives in PII", "Ensemble regex + ML with human confirmation for high-impact actions"),
]

PACKAGING = [
    "Entry package: Fixed-fee assessment for up to X assets/Y connectors with executive report & 2 workshops",
    "Plus package: Adds continuous mode for 90 days and guided remediation sprints",
    "Outcome: Two AI pilot candidates with clean datasets and guardrails",
]

ROADMAP = [
    ("Phase 0 (0-2 weeks)", "Requirements finalization, connector stubs, metric DSL skeleton, initial UI frames"),
    ("Phase 1 (2-6 weeks)", "Snowflake, dbt, Salesforce connectors; core DQ metrics; scoring engine v1; results UI; PDF export v1"),
    ("Phase 2 (6-10 weeks)", "Databricks, BigQuery, Fivetran, Matillion; lineage coverage; governance/security checks; role summaries"),
    ("Phase 3 (10-14 weeks)", "Recommendation engine vendor-awareness; Jira & Azure exports; effort/impact matrix; FinOps metrics"),
    ("Phase 4 (14-18 weeks)", "Private VPC templates; air-gapped build; continuous mode preview"),
]

MILESTONES = [
    "M1: First complete end-to-end run on a pilot dataset",
    "M2: Executive deck sign-off with one design partner",
    "M3: Two quick-win pilots launched",
]

SAMPLE_BACKLOG = [
    "Connector SDK and auth abstractions",
    "Snowflake metadata harvester and sampling profiler",
    "dbt manifest parser and test summarizer",
    "Scoring engine with weight profiles and threshold mapping",
    "PDF generator with templating and brand assets",
    "Recommendation engine rules for Azure, GCP, OpenAI contracts, air-gapped scenarios",
    "Role dashboards with drill-downs and evidence viewer",
]

FUTURE_ENHANCEMENTS = [
    "Data Contracts — detect brittle interfaces and contract violations",
    "Feature Store Readiness — versioning and documentation quality checks",
    "AI Risk — red teaming posture, evaluation harness readiness, hallucination guardrails",
    "Benchmark Library — industry maturity baselines by sector",
    "Partner Motion — offers with Snowflake, Databricks, GCP leveraging credits",
    "Managed Option — 90-day continuous mode with weekly guidance and triage call",
]

APPENDIX_SQL = [
    "Completeness example: SELECT COUNT(*) FROM table WHERE key IS NULL",
    "Freshness example: SELECT MAX(ingest_timestamp) FROM table compared to SLA hours",
    "Uniqueness example: SELECT COUNT(DISTINCT business_key) / COUNT(*)",
    "Ownership coverage: tables missing entries in owner mapping tables",
]

APPENDIX_EPICS = [
    "Establish ownership policies",
    "Implement dbt test coverage to 90 percent on critical models",
    "FinOps right-sizing and idle compute reduction",
]

EXECUTIVE_SLIDE = [
    "Current readiness gauge and dimension scores",
    "Why you score here",
    "Top five risks and quick wins",
    "30-60-90 day plan",
    "Investment options by vendor and licensing posture",
]

NAMING_OPTIONS = [
    "ReadyAI Data Assessment",
    "Aegis Data Readiness",
    "Prism AI Readiness by Decision Minds",
    "DM Aurora Readiness",
]

RACI = [
    ("Product", "Decision Minds Product Lead"),
    ("Engineering", "Connector Lead, Scoring Lead, UI Lead"),
    ("Design", "UX Lead"),
    ("Data Science", "PII and policy heuristics"),
    ("Alliances", "Cloud partner motions and credits"),
    ("Delivery", "Pilot engagement and report readouts"),
]

ACCEPTANCE_TESTS = [
    "Run against demo Snowflake with 50 schemas, produce scores within 2 hours",
    "Inject nulls and confirm completeness score drops with clear evidence",
    "Remove owners and confirm governance score reflects the gap",
    "Change SLA and confirm freshness logic updates scores",
]

COMMUNICATION_TEMPLATES = [
    "Kickoff email covering data access, timeline, deliverables",
    "Executive summary template with role-specific highlights",
    "Remediation backlog handover checklist",
]


def configure_page() -> None:
    """Configure Streamlit page defaults."""

    st.set_page_config(
        page_title="AI Readiness Assessment Accelerator",
        page_icon="🚀",
        layout="wide",
    )


def render_sidebar() -> Tuple[PlatformReadiness, str]:
    """Render sidebar filters and return user selections."""

    st.sidebar.header("Platform Explorer")
    platform_name = st.sidebar.selectbox(
        "Select a platform",
        options=list(PLATFORM_PROFILES.keys()),
        index=0,
    )
    persona = st.sidebar.selectbox(
        "Persona Lens",
        options=PERSONA_ORDER,
        index=0,
    )

    selected = PLATFORM_PROFILES[platform_name]

    st.sidebar.markdown("### Connectors in Scope")
    for connector in selected.connectors:
        st.sidebar.write(f"- {connector}")

    st.sidebar.divider()
    st.sidebar.caption(
        "Scores follow the accelerator's 0-5 maturity model. Metrics show normalized 0-100 readiness values."
    )

    return selected, persona


def render_header(selected: PlatformReadiness) -> None:
    """Render the hero section for the selected platform."""

    st.title("Decision Minds — AI Readiness Assessment Demo")
    st.caption(
        "Preview how the accelerator synthesizes Snowflake, Databricks, BigQuery, Looker, Power BI, and Tableau signals into a readiness narrative."
    )

    col1, col2, col3 = st.columns(3)
    col1.metric("Overall Readiness", f"{selected.overall_score:.1f} / 5")
    col1.progress(min(1.0, selected.overall_score / 5))

    col2.metric("AI Readiness Score", f"{selected.metrics_100['AI Readiness Score']}/100")
    col3.metric("Run Duration", selected.success_metrics["Run Duration"])

    st.info(
        textwrap.dedent(
            """
            The accelerator ingests metadata, observability signals, and governance evidence via read-only connectors. 
            Use the tabs below to inspect dimension scores, evidence samples, and prioritized remediation plans for the selected platform.
            """
        ).strip()
    )


def render_executive_snapshot(selected: PlatformReadiness) -> None:
    """Display KPIs, quick wins, and risks."""

    st.subheader("Executive Snapshot")
    st.write(
        "This view mirrors the executive PDF deck delivered after each accelerator run, highlighting the most impactful signals and immediate actions."
    )

    metrics_cols = st.columns(2)
    metrics_cols[0].dataframe(selected.metric_frame(), use_container_width=True)

    quick_win_col, risk_col = st.columns(2)
    with quick_win_col:
        st.markdown("#### Top Quick Wins")
        for win in selected.quick_wins:
            st.success(f"✅ {win}")
    with risk_col:
        st.markdown("#### Top Risks")
        for risk in selected.top_risks:
            st.error(f"⚠️ {risk}")

    st.markdown("#### Success Metrics")
    success_cols = st.columns(len(selected.success_metrics))
    for idx, (label, value) in enumerate(selected.success_metrics.items()):
        success_cols[idx].metric(label, value)


def render_dimension_drilldown(selected: PlatformReadiness) -> None:
    """Show dimension scoring and comparison to industry baseline."""

    st.subheader("Dimension Drill-down")
    dimension_frame = selected.dimension_frame()
    st.dataframe(dimension_frame, use_container_width=True)

    comparison_rows = []
    for dimension in DIMENSIONS:
        platform_score = selected.dimension_scores[dimension]
        baseline_score = INDUSTRY_BASELINE.get(dimension, 0)
        comparison_rows.append(
            {
                "Dimension": dimension,
                "Platform Score": round(platform_score, 2),
                "Industry Baseline": round(baseline_score, 2),
                "Delta": round(platform_score - baseline_score, 2),
            }
        )
    comparison_frame = pd.DataFrame(comparison_rows).set_index("Dimension")

    st.write(
        "Comparing platform scores to the Decision Minds benchmark library highlights where the organization leads or lags industry peers."
    )
    st.dataframe(
        comparison_frame.style.background_gradient(axis=0, cmap="Greens").format({"Delta": "{:+}"}),
        use_container_width=True,
    )


def render_cross_platform_matrix() -> None:
    """Display readiness metrics across every platform profile."""

    st.subheader("Cross-Platform Benchmarks")
    frame = pd.DataFrame(
        [
            {
                "Platform": profile.name,
                **{dim: round(score, 2) for dim, score in profile.dimension_scores.items()},
            }
            for profile in PLATFORM_PROFILES.values()
        ]
    ).set_index("Platform")
    st.write(
        "Use this matrix during portfolio planning to decide where to run the accelerator first, and to track uplift across successive assessments."
    )
    st.dataframe(frame, use_container_width=True)


def render_feature_coverage() -> None:
    """Visualise feature adoption across platforms."""

    st.subheader("Accelerator Feature Coverage")
    st.write(
        "Each check represents optional accelerator modules. ⚠️ indicates an opportunity to deploy the module for the corresponding platform."
    )
    features = sorted({feature for profile in PLATFORM_PROFILES.values() for feature in profile.feature_adoption})
    matrix_rows = []
    for feature in features:
        row = {"Feature": feature}
        for name, profile in PLATFORM_PROFILES.items():
            row[name] = "✅" if profile.feature_adoption.get(feature, False) else "⚠️"
        matrix_rows.append(row)
    feature_frame = pd.DataFrame(matrix_rows).set_index("Feature")
    st.dataframe(feature_frame, use_container_width=True)


def render_observability(selected: PlatformReadiness) -> None:
    """Surface recent telemetry collected by the accelerator."""

    st.subheader("Latest Observability Checks")
    check_frame = pd.DataFrame(
        {
            "Check": list(selected.observability_checks.keys()),
            "Latest Result": list(selected.observability_checks.values()),
        }
    )
    st.table(check_frame)


def render_accelerator_spec() -> None:
    """Show the full MVP specification inside the demo."""

    st.subheader("Scope and Feature Set")
    st.markdown("### Connectors and Discovery")
    for title, items in CONNECTOR_SCOPE:
        st.markdown(f"**{title}**")
        for item in items:
            st.write(f"- {item}")
    st.info(ACCESS_MODEL_NOTES)

    st.markdown("### Maturity Dimensions and Scoring")
    maturity_frame = (
        pd.DataFrame(
            [
                {"Dimension": dimension, "Description": description}
                for dimension, description in MATURITY_DESCRIPTIONS.items()
            ]
        )
        .set_index("Dimension")
        .loc[DIMENSIONS]
    )
    st.dataframe(maturity_frame, use_container_width=True)
    st.table(pd.DataFrame(MATURITY_BANDS))

    st.markdown("### KPIs and Metrics Library")
    metric_cols = st.columns(3)
    for idx, (category, metrics) in enumerate(METRIC_LIBRARY.items()):
        with metric_cols[idx % 3]:
            st.markdown(f"**{category}**")
            for metric in metrics:
                st.write(f"- {metric}")

    st.markdown("### Evidence and Explainability")
    for item in EVIDENCE_PRACTICES:
        st.write(f"- {item}")

    st.markdown("### Recommendations and Roadmap")
    for note in RECOMMENDATION_NOTES:
        st.write(f"- {note}")

    st.markdown("### Deliverables")
    for deliverable in DELIVERABLES:
        st.write(f"- {deliverable}")

    st.markdown("### Out of Scope (MVP)")
    for item in OUT_OF_SCOPE:
        st.write(f"- {item}")

    st.markdown("### Success Metrics and Acceptance Criteria")
    for criterion in SUCCESS_CRITERIA:
        st.write(f"- {criterion}")

    st.subheader("Product Requirements in Detail")
    st.markdown("#### Connector Requirements")
    for connector, requirement in CONNECTOR_REQUIREMENTS.items():
        st.write(f"- **{connector}:** {requirement}")

    st.markdown("#### Scoring Logic Examples")
    for rule in SCORING_LOGIC:
        st.write(f"- {rule}")
    st.table(pd.DataFrame(MATURITY_MAPPING))

    st.markdown("#### Evidence Model")
    for item in EVIDENCE_MODEL:
        st.write(f"- {item}")

    st.markdown("#### Role-Based Views")
    role_cols = st.columns(3)
    for idx, (role, focus) in enumerate(ROLE_VIEWS.items()):
        with role_cols[idx % 3]:
            st.markdown(f"**{role}**")
            for bullet in focus:
                st.write(f"- {bullet}")

    st.markdown("#### Export and Integration")
    for option in EXPORT_OPTIONS:
        st.write(f"- {option}")

    st.subheader("High-Level Architecture")
    st.markdown("#### Component Overview")
    for component in ARCH_COMPONENTS:
        st.write(f"- {component}")

    st.markdown("#### Data Flow")
    for idx, step in enumerate(DATA_FLOW, start=1):
        st.write(f"{idx}. {step}")

    st.markdown("#### Deployment Topologies")
    for topology in DEPLOYMENT_OPTIONS:
        st.write(f"- {topology}")

    st.markdown("#### Security and Compliance")
    for control in SECURITY_COMPLIANCE:
        st.write(f"- {control}")

    st.subheader("UI and UX Wireframes")
    for page in UI_PAGES:
        st.write(f"- {page}")
    st.code(WIREFRAME_ASCII)

    st.subheader("Technical Design Notes")
    st.markdown("#### Implementation Stack")
    stack_cols = st.columns(3)
    for idx, (layer, detail) in enumerate(IMPLEMENTATION_STACK.items()):
        with stack_cols[idx % 3]:
            st.markdown(f"**{layer}**")
            st.write(detail)

    st.markdown("#### Extensibility")
    for item in EXTENSIBILITY:
        st.write(f"- {item}")

    st.markdown("#### Cost and Performance Controls")
    for item in PERFORMANCE_CONTROLS:
        st.write(f"- {item}")

    st.markdown("#### Offline and Air-gapped Mode")
    for item in OFFLINE_MODE:
        st.write(f"- {item}")

    st.subheader("Risk Register and Mitigations")
    risk_frame = pd.DataFrame(RISK_REGISTER, columns=["Risk", "Mitigation"])
    st.table(risk_frame)

    st.subheader("GTM, Packaging, and Pricing Hints")
    for item in PACKAGING:
        st.write(f"- {item}")

    st.subheader("Roadmap and Timeline")
    roadmap_frame = pd.DataFrame(ROADMAP, columns=["Phase", "Focus"])
    st.table(roadmap_frame)
    st.markdown("**Milestone Gates**")
    for milestone in MILESTONES:
        st.write(f"- {milestone}")

    st.subheader("Sample Backlog")
    for item in SAMPLE_BACKLOG:
        st.write(f"- {item}")

    st.subheader("What to Add Next")
    for item in FUTURE_ENHANCEMENTS:
        st.write(f"- {item}")

    st.subheader("Appendices")
    st.markdown("**Sample SQL and Rules**")
    for item in APPENDIX_SQL:
        st.write(f"- {item}")
    st.markdown("**Example Jira Epics**")
    for item in APPENDIX_EPICS:
        st.write(f"- {item}")
    st.markdown("**Executive Slide Outline**")
    for item in EXECUTIVE_SLIDE:
        st.write(f"- {item}")

    st.subheader("Naming Options")
    for item in NAMING_OPTIONS:
        st.write(f"- {item}")

    st.subheader("Ownership and RACI (MVP)")
    raci_frame = pd.DataFrame(RACI, columns=["Role", "Owner"])
    st.table(raci_frame)

    st.subheader("Acceptance Test Scenarios")
    for item in ACCEPTANCE_TESTS:
        st.write(f"- {item}")

    st.subheader("Communication Templates")
    for item in COMMUNICATION_TEMPLATES:
        st.write(f"- {item}")


def render_persona_view(selected: PlatformReadiness, persona: str) -> None:
    """Provide persona-focused narrative."""

    st.subheader(f"Persona Narrative — {persona}")
    st.write(selected.persona_notes.get(persona, "Persona guidance not captured."))

    st.markdown("#### Enablement Checklist")
    checklist_items = {
        "CFO": [
            "Validate chargeback model uses accelerator FinOps metrics.",
            "Confirm idle capacity remediation actions are tracked in backlog.",
        ],
        "CRO": [
            "Review evidence archive for compliance sign-off.",
            "Map lineage coverage to regulatory data sets.",
        ],
        "CIO/CTO": [
            "Align IAM and secret rotation cadence with accelerator findings.",
            "Prioritize modernization epics in quarterly roadmap.",
        ],
        "CDAO": [
            "Expand stewardship office hours using accelerator backlog.",
            "Ensure glossary updates feed into BI semantic layers.",
        ],
        "CAIO": [
            "Map AI pilots to datasets scoring >=3.5 readiness.",
            "Instrument prompt logging guardrails before production launch.",
        ],
    }
    for item in checklist_items.get(persona, []):
        st.write(f"- {item}")


def main() -> None:
    configure_page()
    selected_platform, persona = render_sidebar()
    render_header(selected_platform)

    tab_exec, tab_dimensions, tab_platforms, tab_spec, tab_persona = st.tabs(
        [
            "Executive Snapshot",
            "Dimension Drill-down",
            "Cross-Platform Insights",
            "Accelerator Specification",
            "Persona Narrative",
        ]
    )

    with tab_exec:
        render_executive_snapshot(selected_platform)
        render_observability(selected_platform)
    with tab_dimensions:
        render_dimension_drilldown(selected_platform)
    with tab_platforms:
        render_cross_platform_matrix()
        render_feature_coverage()
    with tab_spec:
        render_accelerator_spec()
    with tab_persona:
        render_persona_view(selected_platform, persona)


if __name__ == "__main__":
    main()

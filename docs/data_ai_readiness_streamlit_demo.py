"""Streamlit demo for the Data & AI Readiness Accelerator."""
from __future__ import annotations

import textwrap
from dataclasses import dataclass
from typing import Dict, List

import pandas as pd
import streamlit as st


@dataclass(frozen=True)
class PlatformReadiness:
    name: str
    data_quality: int
    pipeline_reliability: int
    governance_coverage: int
    ai_readiness: int
    notes: List[str]
    feature_adoption: Dict[str, bool]
    observability_checks: Dict[str, str]

    def to_metric_frame(self) -> pd.DataFrame:
        return pd.DataFrame(
            {
                "Metric": [
                    "Data Quality Index",
                    "Pipeline Reliability",
                    "Governance Coverage",
                    "AI Readiness Score",
                ],
                "Score": [
                    self.data_quality,
                    self.pipeline_reliability,
                    self.governance_coverage,
                    self.ai_readiness,
                ],
            }
        )


PLATFORM_PROFILES: Dict[str, PlatformReadiness] = {
    "Snowflake": PlatformReadiness(
        name="Snowflake",
        data_quality=86,
        pipeline_reliability=92,
        governance_coverage=78,
        ai_readiness=84,
        notes=[
            "Strong automated profiling coverage across curated data products.",
            "Incremental data refresh patterns deliver sub-hour freshness for AI workloads.",
            "Need to expand stewardship assignments for long-tail schemas.",
        ],
        feature_adoption={
            "Automated Freshness Monitoring": True,
            "Schema Drift Protection": True,
            "PII Guardrails": True,
            "Lineage Explorer": True,
            "Bias & Fairness Screening": False,
        },
        observability_checks={
            "Freshness Lag (hrs)": "0.4",
            "Schema Drift Alerts (30d)": "0",
            "Critical Data Quality Tests": "58/60",
            "Open Remediation Items": "2",
        },
    ),
    "Databricks": PlatformReadiness(
        name="Databricks",
        data_quality=81,
        pipeline_reliability=88,
        governance_coverage=73,
        ai_readiness=80,
        notes=[
            "Medallion architecture provides clear lineage from raw to gold layers.",
            "Delta Live Tables deliver strong observability but alert runbooks require updates.",
            "Opportunity to standardize data quality checks for partner-contributed notebooks.",
        ],
        feature_adoption={
            "Automated Freshness Monitoring": True,
            "Schema Drift Protection": True,
            "PII Guardrails": False,
            "Lineage Explorer": True,
            "Bias & Fairness Screening": True,
        },
        observability_checks={
            "Freshness Lag (hrs)": "1.2",
            "Schema Drift Alerts (30d)": "3",
            "Critical Data Quality Tests": "46/55",
            "Open Remediation Items": "5",
        },
    ),
    "Looker": PlatformReadiness(
        name="Looker",
        data_quality=74,
        pipeline_reliability=79,
        governance_coverage=82,
        ai_readiness=76,
        notes=[
            "Semantic model captures reusable business logic for AI feature teams.",
            "Visual regression testing needed to protect mission-critical dashboards.",
            "Adopt deployment review board to reduce ad-hoc production changes.",
        ],
        feature_adoption={
            "Automated Freshness Monitoring": False,
            "Schema Drift Protection": True,
            "PII Guardrails": True,
            "Lineage Explorer": True,
            "Bias & Fairness Screening": False,
        },
        observability_checks={
            "Freshness Lag (hrs)": "3.5",
            "Schema Drift Alerts (30d)": "4",
            "Critical Data Quality Tests": "38/50",
            "Open Remediation Items": "7",
        },
    ),
    "Power BI": PlatformReadiness(
        name="Power BI",
        data_quality=77,
        pipeline_reliability=75,
        governance_coverage=69,
        ai_readiness=72,
        notes=[
            "High-value executive dashboards depend on manually refreshed data sources.",
            "Fabric workspaces ready for automated lineage once premium capacity is activated.",
            "Improve certified dataset adoption to reduce redundant semantic models.",
        ],
        feature_adoption={
            "Automated Freshness Monitoring": True,
            "Schema Drift Protection": False,
            "PII Guardrails": True,
            "Lineage Explorer": False,
            "Bias & Fairness Screening": True,
        },
        observability_checks={
            "Freshness Lag (hrs)": "5.0",
            "Schema Drift Alerts (30d)": "6",
            "Critical Data Quality Tests": "29/45",
            "Open Remediation Items": "11",
        },
    ),
    "Tableau": PlatformReadiness(
        name="Tableau",
        data_quality=83,
        pipeline_reliability=85,
        governance_coverage=71,
        ai_readiness=79,
        notes=[
            "Hyper extracts align with AI training cadence but require deduplication rules.",
            "Adopt Data Management add-on to scale cataloging and data discovery.",
            "Embed quality flags within dashboards to surface readiness gaps to analysts.",
        ],
        feature_adoption={
            "Automated Freshness Monitoring": True,
            "Schema Drift Protection": False,
            "PII Guardrails": True,
            "Lineage Explorer": True,
            "Bias & Fairness Screening": False,
        },
        observability_checks={
            "Freshness Lag (hrs)": "2.1",
            "Schema Drift Alerts (30d)": "2",
            "Critical Data Quality Tests": "41/52",
            "Open Remediation Items": "6",
        },
    ),
}

TEN_STEP_PLAN = [
    {
        "Step": "1. Executive Alignment",
        "Outcome": "Sponsor-approved success metrics and scope",
        "Owner": "Data Strategy",
        "Status": "Complete",
        "Target": "Week 1",
    },
    {
        "Step": "2. Data Inventory",
        "Outcome": "Catalogued Snowflake/Databricks sources and BI assets",
        "Owner": "Data Governance",
        "Status": "Complete",
        "Target": "Week 1",
    },
    {
        "Step": "3. Connectivity Validation",
        "Outcome": "Credential and network checks across all platforms",
        "Owner": "Platform Engineering",
        "Status": "In Progress",
        "Target": "Week 2",
    },
    {
        "Step": "4. Profiling Automation",
        "Outcome": "Freshness and anomaly jobs running on schedule",
        "Owner": "Data Engineering",
        "Status": "In Progress",
        "Target": "Week 3",
    },
    {
        "Step": "5. Pipeline Observability",
        "Outcome": "SLA breaches and incidents triaged with owners",
        "Owner": "Analytics Ops",
        "Status": "Planned",
        "Target": "Week 4",
    },
    {
        "Step": "6. Semantic Diagnostics",
        "Outcome": "BI semantic layer checks executed and scored",
        "Owner": "BI Center of Excellence",
        "Status": "Planned",
        "Target": "Week 5",
    },
    {
        "Step": "7. Governance Review",
        "Outcome": "Controls mapped to regulatory requirements",
        "Owner": "Risk & Compliance",
        "Status": "Planned",
        "Target": "Week 6",
    },
    {
        "Step": "8. Remediation Sprinting",
        "Outcome": "Backlog prioritized with committed owners",
        "Owner": "Data PMO",
        "Status": "Planned",
        "Target": "Week 7",
    },
    {
        "Step": "9. AI Feature Enablement",
        "Outcome": "Ready datasets mapped to AI features and models",
        "Owner": "ML Engineering",
        "Status": "Planned",
        "Target": "Week 8",
    },
    {
        "Step": "10. Continuous Monitoring",
        "Outcome": "Runbook for recurring score refresh approved",
        "Owner": "Data Stewardship",
        "Status": "Planned",
        "Target": "Week 9",
    },
]


def render_sidebar() -> PlatformReadiness:
    st.sidebar.header("Configuration")
    platform_name = st.sidebar.selectbox(
        "Select a platform to inspect",
        options=list(PLATFORM_PROFILES.keys()),
        index=0,
    )
    return PLATFORM_PROFILES[platform_name]


def render_overview(selected: PlatformReadiness) -> None:
    st.title("Data & AI Readiness Accelerator Demo")
    st.caption(
        "Explore how accelerator metrics highlight platform readiness for AI workloads."
    )

    st.write(
        textwrap.dedent(
            f"""
            This Streamlit experience mirrors the accelerator's executive dashboard and summarizes
            key readiness metrics, governance posture, and remediation recommendations for
            **{selected.name}**. Use the sidebar to explore how scores shift across Snowflake,
            Databricks, Looker, Power BI, Tableau, and other connected analytics platforms.
            """
        )
    )

    cols = st.columns(4)
    cols[0].metric("Data Quality Index", f"{selected.data_quality}/100")
    cols[1].metric("Pipeline Reliability", f"{selected.pipeline_reliability}/100")
    cols[2].metric("Governance Coverage", f"{selected.governance_coverage}/100")
    cols[3].metric("AI Readiness Score", f"{selected.ai_readiness}/100")


def render_charts(selected: PlatformReadiness) -> None:
    st.subheader("Metric Breakdown")
    metric_frame = selected.to_metric_frame().set_index("Metric")
    st.bar_chart(metric_frame)

    st.subheader("Remediation Focus")
    st.write(
        "Prioritize the highest-impact remediation themes to accelerate AI readiness maturity."
    )
    for note in selected.notes:
        st.write(f"- {note}")


def render_quality_gap_analysis() -> None:
    st.subheader("Cross-Platform Quality Gaps")
    comparison_frame = pd.DataFrame(
        [
            {
                "Platform": profile.name,
                "Data Quality": profile.data_quality,
                "Pipeline Reliability": profile.pipeline_reliability,
                "Governance": profile.governance_coverage,
                "AI Readiness": profile.ai_readiness,
            }
            for profile in PLATFORM_PROFILES.values()
        ]
    ).set_index("Platform")

    st.write(
        "This view highlights how Snowflake, Databricks, Looker, Power BI, Tableau, and similar data connection platforms benchmark against each other."
    )
    st.dataframe(comparison_frame.style.background_gradient(axis=0, cmap="Blues"))


def render_feature_matrix() -> None:
    st.subheader("Platform Feature Coverage")
    st.write(
        "Compare accelerator feature adoption across data platforms to identify where additional enablement or tooling is required."
    )
    features = sorted(
        {feature for profile in PLATFORM_PROFILES.values() for feature in profile.feature_adoption}
    )
    matrix_rows = []
    for feature in features:
        row = {"Feature": feature}
        for name, profile in PLATFORM_PROFILES.items():
            row[name] = "✅" if profile.feature_adoption.get(feature, False) else "⚠️"
        matrix_rows.append(row)

    feature_frame = pd.DataFrame(matrix_rows).set_index("Feature")
    st.dataframe(feature_frame)


def render_check_catalog(selected: PlatformReadiness) -> None:
    st.subheader("Key Checks & Thresholds")
    st.write(
        "Detailed telemetry summarizing the latest readiness checks for the selected platform. Values represent the most recent accelerator run."
    )
    check_frame = pd.DataFrame(
        {
            "Check": list(selected.observability_checks.keys()),
            "Latest Result": list(selected.observability_checks.values()),
        }
    )
    st.table(check_frame)


def render_ten_step_plan() -> None:
    st.subheader("Ten-Step Readiness Plan Tracker")
    st.write(
        "Monitor delivery status across the accelerator's ten-step methodology, aligning directly with the implementation approach described in the guide."
    )
    plan_frame = pd.DataFrame(TEN_STEP_PLAN)

    status_colors = {
        "Complete": "background-color: #2ca02c; color: white;",
        "In Progress": "background-color: #ff7f0e; color: white;",
        "Planned": "background-color: #1f77b4; color: white;",
    }

    def style_status(value: str) -> str:
        return status_colors.get(value, "")

    st.dataframe(plan_frame.style.applymap(style_status, subset=["Status"]))


def render_action_plan(selected: PlatformReadiness) -> None:
    st.subheader("90-Day Action Plan")
    plan_items = {
        "Data Quality": selected.data_quality,
        "Pipeline Reliability": selected.pipeline_reliability,
        "Governance": selected.governance_coverage,
    }

    for theme, score in plan_items.items():
        st.write(f"### {theme}")
        st.progress(score / 100)
        st.write(
            "Next milestone: raise score to {target}/100 through targeted remediation sprints.".format(
                target=min(100, score + 8)
            )
        )


def main() -> None:
    selected_platform = render_sidebar()
    render_overview(selected_platform)
    render_charts(selected_platform)
    render_quality_gap_analysis()
    render_feature_matrix()
    render_check_catalog(selected_platform)
    render_ten_step_plan()
    render_action_plan(selected_platform)


if __name__ == "__main__":
    main()

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
    ),
}


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
    render_action_plan(selected_platform)


if __name__ == "__main__":
    main()

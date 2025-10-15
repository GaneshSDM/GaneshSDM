"""Demonstrate the working skeleton of the AI CloudOps platform."""

from __future__ import annotations

from pprint import pprint

from .connectors.aws import AWSConnector
from .connectors.azure import AzureConnector
from .connectors.gcp import GCPConnector
from .platform import CloudOpsPlatform


def main() -> None:
    platform = CloudOpsPlatform(
        connectors=[AWSConnector(), AzureConnector(), GCPConnector()]
    )
    snapshot = platform.collect_posture_snapshot()
    costs = platform.summarize_costs(snapshot)

    print("=== Resources ===")
    for resource in snapshot.resources:
        print(
            f"[{resource.provider.upper()}] {resource.name} — {resource.resource_type} "
            f"(${resource.cost_per_month():,.2f}/month, utilization {resource.utilization:.0%})"
        )

    print("\n=== Metrics ===")
    pprint(snapshot.metrics)

    print("\n=== Security Findings ===")
    for provider, findings in snapshot.security_findings.items():
        print(f"{provider.upper()}:")
        for finding in findings:
            print(f"  - {finding}")

    print("\n=== Advisor Recommendations ===")
    for rec in snapshot.advisor_recommendations:
        print(f"- {rec}")

    print("\n=== Monthly Cost Summary ===")
    for provider, cost in costs.items():
        label = provider.upper() if provider != "total" else "TOTAL"
        print(f"{label}: ${cost:,.2f}")


if __name__ == "__main__":
    main()

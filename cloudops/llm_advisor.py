"""Heuristic substitute for the AI assistant referenced in the blueprint."""

from __future__ import annotations

from typing import Dict, Iterable, List

from .connectors.base import CloudResource


class LLMAdvisor:
    """Generate narrative recommendations based on telemetry snapshots."""

    def recommend(self, resources: Iterable[CloudResource], metrics: Dict[str, Dict[str, float]]) -> List[str]:
        recommendations: List[str] = []
        underutilized = [r for r in resources if r.utilization < 0.35]
        if underutilized:
            names = ", ".join(sorted(r.name for r in underutilized))
            recommendations.append(
                f"Rightsize or schedule downtime for low-utilization services: {names}."
            )

        for provider, provider_metrics in metrics.items():
            spend = provider_metrics.get("spend_month_to_date", 0.0)
            if spend > 4000:
                recommendations.append(
                    f"Review committed-use discounts for {provider.upper()} — projected monthly spend is ${spend:,.0f}."
                )
            error_rate = provider_metrics.get("error_rate", 0.0)
            if error_rate > 0.003:
                recommendations.append(
                    f"Investigate elevated error rate ({error_rate:.2%}) detected in {provider.upper()} workloads."
                )
        if not recommendations:
            recommendations.append("No notable optimizations detected during this snapshot.")
        return recommendations


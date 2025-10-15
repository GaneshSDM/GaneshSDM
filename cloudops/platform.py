"""Composable façade that orchestrates connectors and the advisor."""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, Iterable, List

from .connectors.base import CloudConnector, CloudResource
from .llm_advisor import LLMAdvisor


@dataclass
class PostureSnapshot:
    resources: List[CloudResource]
    metrics: Dict[str, Dict[str, float]]
    security_findings: Dict[str, List[str]]
    advisor_recommendations: List[str]


class CloudOpsPlatform:
    """Minimal orchestration layer to make the blueprint tangible."""

    def __init__(self, connectors: Iterable[CloudConnector], advisor: LLMAdvisor | None = None) -> None:
        self._connectors = list(connectors)
        if not self._connectors:
            raise ValueError("At least one connector is required to build the platform.")
        self._advisor = advisor or LLMAdvisor()

    def collect_posture_snapshot(self) -> PostureSnapshot:
        resources: List[CloudResource] = []
        metrics: Dict[str, Dict[str, float]] = {}
        security: Dict[str, List[str]] = defaultdict(list)

        for connector in self._connectors:
            provider_resources = list(connector.discover_resources())
            resources.extend(provider_resources)
            metrics[connector.provider] = dict(connector.collect_operational_metrics())
            security[connector.provider].extend(connector.describe_security_findings())

        recommendations = self._advisor.recommend(resources, metrics)
        return PostureSnapshot(
            resources=sorted(resources, key=lambda r: (r.provider, r.name)),
            metrics=metrics,
            security_findings=dict(security),
            advisor_recommendations=recommendations,
        )

    def summarize_costs(self, snapshot: PostureSnapshot | None = None) -> Dict[str, float]:
        snapshot = snapshot or self.collect_posture_snapshot()
        totals: Dict[str, float] = defaultdict(float)
        for resource in snapshot.resources:
            totals[resource.provider] += resource.cost_per_month()
        totals["total"] = sum(totals.values())
        return {provider: round(cost, 2) for provider, cost in totals.items()}


__all__ = ["CloudOpsPlatform", "PostureSnapshot"]

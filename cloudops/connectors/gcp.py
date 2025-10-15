"""Static GCP connector used for the CloudOps demo."""

from __future__ import annotations

from typing import Dict, Iterable, List

from .base import CloudConnector, CloudResource


class GCPConnector:
    provider = "gcp"

    def __init__(self) -> None:
        self._resources = [
            CloudResource(
                provider=self.provider,
                name="ml-platform",
                resource_type="gke_cluster",
                cost_per_hour=2.9,
                utilization=0.58,
                tags={"env": "prod", "tier": "data"},
            ),
            CloudResource(
                provider=self.provider,
                name="event-stream",
                resource_type="pubsub_topic",
                cost_per_hour=0.45,
                utilization=0.21,
                tags={"env": "dev", "tier": "integration"},
            ),
        ]

    def discover_resources(self) -> Iterable[CloudResource]:
        return tuple(self._resources)

    def collect_operational_metrics(self) -> Dict[str, float]:
        return {
            "avg_cpu_utilization": 0.39,
            "error_rate": 0.001,
            "spend_month_to_date": sum(r.cost_per_month() for r in self._resources),
        }

    def describe_security_findings(self) -> List[str]:
        return [
            "Security Command Center: Public bucket detected in analytics-project",
        ]


__all__ = ["GCPConnector"]

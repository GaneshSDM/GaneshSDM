"""Static Azure connector used for the CloudOps demo."""

from __future__ import annotations

from typing import Dict, Iterable, List

from .base import CloudConnector, CloudResource


class AzureConnector:
    provider = "azure"

    def __init__(self) -> None:
        self._resources = [
            CloudResource(
                provider=self.provider,
                name="customer-insights",
                resource_type="synapse_workspace",
                cost_per_hour=3.25,
                utilization=0.63,
                tags={"env": "prod", "tier": "analytics"},
            ),
            CloudResource(
                provider=self.provider,
                name="support-functions",
                resource_type="app_service_plan",
                cost_per_hour=1.05,
                utilization=0.28,
                tags={"env": "staging", "tier": "web"},
            ),
        ]

    def discover_resources(self) -> Iterable[CloudResource]:
        return tuple(self._resources)

    def collect_operational_metrics(self) -> Dict[str, float]:
        return {
            "avg_cpu_utilization": 0.46,
            "error_rate": 0.002,
            "spend_month_to_date": sum(r.cost_per_month() for r in self._resources),
        }

    def describe_security_findings(self) -> List[str]:
        return [
            "Defender for Cloud: Storage account missing immutability policy",
        ]


__all__ = ["AzureConnector"]

"""Static AWS connector used for the CloudOps demo."""

from __future__ import annotations

from typing import Dict, Iterable, List

from .base import CloudConnector, CloudResource


class AWSConnector:
    provider = "aws"

    def __init__(self) -> None:
        self._resources = [
            CloudResource(
                provider=self.provider,
                name="orders-api",
                resource_type="ecs_service",
                cost_per_hour=1.75,
                utilization=0.42,
                tags={"env": "prod", "tier": "web"},
            ),
            CloudResource(
                provider=self.provider,
                name="finance-warehouse",
                resource_type="redshift_cluster",
                cost_per_hour=4.10,
                utilization=0.71,
                tags={"env": "prod", "owner": "finops"},
            ),
        ]

    def discover_resources(self) -> Iterable[CloudResource]:
        return tuple(self._resources)

    def collect_operational_metrics(self) -> Dict[str, float]:
        return {
            "avg_cpu_utilization": 0.54,
            "error_rate": 0.004,
            "spend_month_to_date": sum(r.cost_per_month() for r in self._resources),
        }

    def describe_security_findings(self) -> List[str]:
        return [
            "SecurityHub: IAM access key older than 90 days for analytics-bot",
            "GuardDuty: Reconnaissance activity blocked in ap-southeast-1",
        ]


__all__ = ["AWSConnector"]

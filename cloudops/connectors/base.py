"""Interfaces and dataclasses shared by all cloud connectors."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Protocol


@dataclass(frozen=True)
class CloudResource:
    """Metadata describing a managed cloud resource."""

    provider: str
    name: str
    resource_type: str
    cost_per_hour: float
    utilization: float
    tags: Dict[str, str]

    def cost_per_month(self, hours: int = 730) -> float:
        """Estimate the monthly cost using an hours multiplier."""

        return round(self.cost_per_hour * hours, 2)


class CloudConnector(Protocol):
    """All connectors implement a uniform discovery and metrics interface."""

    provider: str

    def discover_resources(self) -> Iterable[CloudResource]:
        """Return the resources that are currently under management."""

    def collect_operational_metrics(self) -> Dict[str, float]:
        """Return lightweight operational signals used for heuristics."""

    def describe_security_findings(self) -> List[str]:
        """Surface notable security or compliance issues."""


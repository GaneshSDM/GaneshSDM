"""Simple statistical checks that can be used during demos."""

from __future__ import annotations

import csv
from pathlib import Path
from statistics import mean, pstdev


Record = dict[str, object]


def _parse_float(value: str | None) -> float:
    if value in (None, "", "None"):
        return 0.0
    return float(value)


def detect_anomalies(csv_path: str | Path, value_column: str) -> list[Record]:
    """Return suspicious rows detected via a basic z-score."""

    path = Path(csv_path)
    with path.open() as handle:
        reader = csv.DictReader(handle)
        rows = [dict(row) for row in reader]

    if not rows or value_column not in rows[0]:
        raise ValueError(f"Column '{value_column}' not found in {csv_path}.")

    values = [_parse_float(row[value_column]) for row in rows]
    avg = mean(values)
    std = pstdev(values)

    if std == 0:
        return []

    anomalies: list[Record] = []
    for row, value in zip(rows, values):
        z_score = (value - avg) / std
        if abs(z_score) > 3:
            anomalies.append(row)

    return anomalies


__all__ = ["detect_anomalies"]

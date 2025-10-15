"""A light-weight imitation of ``snowflake.connector`` for demo purposes."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, List, Tuple
import csv


@dataclass
class FakeCursor:
    """Minimal cursor that records commands and persists rows to disk."""

    executed_commands: list[str] = field(default_factory=list)
    output_path: Path = Path("demo_snowflake_output.csv")

    def execute(self, command: str) -> None:
        self.executed_commands.append(command)

    def write_records(self, rows: Iterable[dict[str, object]], table_name: str) -> Tuple[bool, int, int, None]:
        row_list: List[dict[str, object]] = list(rows)
        if not row_list:
            return True, 0, 0, None

        fieldnames = list(row_list[0].keys())
        with self.output_path.open("w", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(row_list)

        return True, 1, len(row_list), None


@dataclass
class FakeConnection:
    cursor_instance: FakeCursor = field(default_factory=FakeCursor)

    def cursor(self) -> FakeCursor:
        return self.cursor_instance

    def close(self) -> None:
        pass


def connect(**_: object) -> FakeConnection:  # pragma: no cover - behaviour is trivial
    return FakeConnection()


__all__ = ["FakeCursor", "FakeConnection", "connect"]

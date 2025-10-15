"""Utility helpers used across the demo for retry semantics."""

from __future__ import annotations

import time
from typing import Callable, TypeVar

T = TypeVar("T")


def run_with_retries(fn: Callable[[], T], retries: int = 3, delay: int = 30) -> T:
    """Execute ``fn`` with retries, logging output to the console."""

    last_error: Exception | None = None

    for attempt in range(1, retries + 1):
        try:
            result = fn()
            print(f"✅ ETL succeeded, rows={result}")
            return result
        except Exception as exc:  # pragma: no cover - used for interactive demos
            last_error = exc
            print(f"⚠️ Attempt {attempt}/{retries} failed: {exc}")
            time.sleep(delay)

    raise RuntimeError("❌ ETL failed permanently") from last_error


__all__ = ["run_with_retries"]

"""Expose metrics from the demo ETL pipeline."""

from __future__ import annotations

import subprocess
import time

from prometheus_client import Gauge, start_http_server

ETL_SUCCESS = Gauge("etl_pipeline_success", "1=success,0=failure")
ETL_DURATION = Gauge("etl_pipeline_duration_seconds", "ETL runtime in seconds")
ETL_ROWS = Gauge("etl_pipeline_rows", "Rows processed")


def run_and_collect() -> None:
    """Execute the ETL pipeline on an interval and export metrics."""

    while True:
        start = time.time()
        try:
            output = subprocess.check_output(["python", "etl/etl_job.py"], text=True)
            ETL_SUCCESS.set(1)
            for token in output.split():
                if token.isdigit():
                    ETL_ROWS.set(int(token))
            print(output)
        except Exception as exc:  # pragma: no cover - interactive loop
            print(f"Failed to execute ETL pipeline: {exc}")
            ETL_SUCCESS.set(0)
        ETL_DURATION.set(time.time() - start)
        time.sleep(300)


if __name__ == "__main__":
    start_http_server(8000)
    run_and_collect()

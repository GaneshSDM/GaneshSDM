"""Demo ETL pipeline that showcases the accelerator's Python layer."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable

from remediation.retry_handler import run_with_retries
from snowflake.connector import FakeCursor, connect

DATA_PATH = Path(__file__).resolve().parent / "sample_sales.csv"


Record = dict[str, object]


def extract() -> list[Record]:
    """Load the raw CSV dataset used for the demo."""

    with DATA_PATH.open() as handle:
        reader = csv.DictReader(handle)
        return [dict(row) for row in reader]


def transform(rows: Iterable[Record]) -> list[Record]:
    """Clean the dataset by dropping duplicates and filling missing values."""

    cleaned: list[Record] = []
    seen = set()
    for row in rows:
        key = tuple(sorted(row.items()))
        if key in seen:
            continue
        seen.add(key)
        amount = row.get("amount")
        row["amount"] = float(amount) if amount not in (None, "", "None") else 0.0
        cleaned.append(row)
    return cleaned


def load(rows: Iterable[Record]) -> int:
    """Write the records to a Snowflake-like destination."""

    conn = connect()
    cs: FakeCursor = conn.cursor()
    cs.execute("CREATE OR REPLACE TABLE SALES (id int, product string, amount float)")
    success, nchunks, nrows, _ = cs.write_records(rows, "SALES")
    conn.close()

    if not success:
        raise RuntimeError("Loading data into Snowflake demo table failed")

    return nrows


def etl_pipeline() -> int:
    records = extract()
    transformed = transform(records)
    return load(transformed)


if __name__ == "__main__":
    run_with_retries(etl_pipeline, retries=3, delay=1)

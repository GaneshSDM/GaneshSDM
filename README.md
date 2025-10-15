# ETL Accelerator Demo

This repository packages a lightweight but end-to-end demonstration of an ETL
accelerator that can be walked through with business stakeholders.  The demo is
split into distinct layers so that each capability can be showcased in
isolation:

| Layer | Location | Highlights |
| --- | --- | --- |
| Orchestration | `dags/etl_accelerator.py` | Airflow DAG that chains ingestion, Databricks, and validation tasks |
| Data Engineering | `etl/etl_job.py` | Extract-transform-load workflow running on a sample sales dataset |
| Remediation | `remediation/retry_handler.py` | Shared retry helper used across the stack |
| Monitoring | `monitoring/` | Prometheus exporter and anomaly detection logic |
| Infrastructure as Code | `infrastructure/main.tf` | Terraform blueprint for Snowflake and Databricks resources |
| Strategy & Vision | `docs/ai_cloudops_platform.md` | AI CloudOps platform blueprint for enterprise multi-cloud operations |
| Working Prototype | `cloudops/run_demo.py` | Executable simulation of the CloudOps control plane with multi-cloud connectors |
| CloudOps Walkthrough | `docs/cloudops_getting_started.md` | Step-by-step instructions for running and extending the prototype |

## Getting started

1. **Run the ETL pipeline locally**
   ```bash
   python -m etl.etl_job
   ```
   The run uses the built-in Snowflake stub, writes a CSV to
   `demo_snowflake_output.csv`, and logs the number of rows processed.

2. **Preview anomaly detection**
   ```bash
   python - <<'PY'
   from monitoring.anomaly_detector import detect_anomalies
   print(detect_anomalies("etl/sample_sales.csv", "amount"))
   PY
   ```

3. **Review the orchestration and infrastructure blueprints**
   * `dags/etl_accelerator.py` shows how Airflow wires the components together.
   * `infrastructure/main.tf` illustrates how Snowflake and Databricks jobs
     would be provisioned.
   * `cloudops/run_demo.py` demonstrates the CloudOps control plane concepts in
     code with sample connectors and recommendations. See
     `docs/cloudops_getting_started.md` for a full walkthrough of how to run the
     simulation and validate it with automated tests.

## Monitoring demo

Run the Prometheus exporter to collect metrics every five minutes:

```bash
python monitoring/exporter.py
```

Prometheus can scrape the metrics using `monitoring/prometheus.yml`.

---

This project is intentionally self-contained so it can be demoed on a laptop
without cloud connectivity while still representing a realistic architecture.

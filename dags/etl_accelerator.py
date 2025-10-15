"""Demo Airflow DAG wiring the accelerator components together.

This DAG is intentionally lightweight so it can be dropped into a demo
environment without any additional configuration.  The operators simply point
at the functions that live inside this repository which keeps all of the demo
logic in one place.
"""

from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.databricks.operators.databricks import DatabricksRunNowOperator

from etl.etl_job import etl_pipeline
from monitoring.anomaly_detector import detect_anomalies


DEFAULT_ARGS = {"owner": "dataops", "retries": 1}


with DAG(
    dag_id="etl_accelerator_demo",
    default_args=DEFAULT_ARGS,
    schedule_interval="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    doc_md="""
    ### Demo ETL Accelerator

    1. Bulk ingest a CSV file stored alongside the repository.
    2. Kick-off a Databricks job that represents the heavy-lifting transform layer.
    3. Validate the transformed dataset by running a simple anomaly detector.
    """,
) as dag:
    ingest_csv = PythonOperator(
        task_id="bulk_ingest",
        python_callable=etl_pipeline,
    )

    run_databricks = DatabricksRunNowOperator(
        task_id="databricks_transform",
        job_id=1234,  # Placeholder: replace with Terraform output in real deployments.
    )

    validate = PythonOperator(
        task_id="validate_data",
        python_callable=lambda: detect_anomalies("etl/sample_sales.csv", "amount"),
    )

    ingest_csv >> run_databricks >> validate

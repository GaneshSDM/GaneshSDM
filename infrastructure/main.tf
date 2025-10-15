provider "snowflake" {
  account  = var.snowflake_account
  username = var.snowflake_user
  password = var.snowflake_pass
  role     = "SYSADMIN"
}

resource "snowflake_database" "etl_db" {
  name = "ETL_DB"
}

resource "databricks_job" "etl_job" {
  name = "databricks_etl_job"
  new_cluster {
    spark_version = "12.2.x-scala2.12"
    node_type_id  = "Standard_DS3_v2"
    num_workers   = 2
  }
  notebook_task {
    notebook_path = "/Shared/transform_sales"
  }
}

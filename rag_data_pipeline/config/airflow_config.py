"""
Airflow DAG config
"""

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from rag_pipeline import run_pipeline

with DAG("rag_pipeline_dag", start_date=datetime(2023, 1, 1), schedule_interval="@daily", catchup=False) as dag:
    run_rag_task = PythonOperator(
        task_id="run_rag_pipeline",
        python_callable=run_pipeline,
        op_kwargs={"source": "daily_source", "db_config": {"db": "vector_db"}},
    )

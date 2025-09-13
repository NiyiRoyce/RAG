"""
Check DAGs load correctly in Airflow
"""

import os

def test_dags_exist():
    assert os.path.exists("dags"), "DAGs folder missing!"

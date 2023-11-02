from datetime import datetime, timedelta
from airflow.models import DAG
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
from airflow.operators.bash_operator import BashOperator
import logging

# def print_sla_miss(**kwargs):
#     logging.info("SLA missed")


#ingest_url="/ingestToDruid?fileName=session_ingest.json"

with DAG(
     dag_id='api_hit_test',
     schedule_interval='@hourly',
     start_date=datetime(2023, 11, 2),
     catchup=False,
     #sla=timedelta(hours=2),
     #sla_miss_callback=print_sla_miss,
     #default_args=default_args
 ) as dag:
    
     api_hit_test= SimpleHttpOperator(
         task_id='api_hit_test',
         http_conn_id='api_ingest',
         endpoint='searchRumEvents/',
         method='POST',
        # response_filter=lambda response:json.loads(response.text),
         log_response=True
     )

    

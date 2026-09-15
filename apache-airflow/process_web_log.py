# Step 1: Importing Modules
# To initiate the DAG Object
from airflow import DAG

# Importing datetime and timedelta modules for scheduling the DAGs
from datetime import timedelta, datetime

# Import the BashOperator
from airflow.operators.bash import BashOperator

# Step 2: Initiating the default_args
default_args = {
        'owner' : 'dummy_user',
        'start_date' : datetime(2026, 1, 1),        # Standard practice is to set a past date (or datetime.today())
        'email' : ['dummy_user@example.com'],
        #'email_on_failure': True,                  # Optional suitable additional argument
        #'email_on_retry': True,                    # Optional suitable additional argument
        'retries': 1,                              # Number of retries if a task fails
        'retry_delay': timedelta(minutes=5),       # Delay between retries
}

# Step 3: Define the DAG using the default arguments (Creating DAG Object)
# This task should extract the ipaddress field from the web server log file
dag = DAG(
        dag_id='DAG-1',
        default_args=default_args,
        schedule=timedelta(days=1),       # Daily schedule OR // schedule="@daily"
        catchup=False
    )

# Task 3 - Create a task to extract data
extract_data = BashOperator(
    task_id='extract_data',
    bash_command='cut -d" " -f1 /home/project/airflow/dags/capstone/accesslog.txt > /home/project/airflow/dags/capstone/extracted_data.txt',
    dag=dag,
)

# Task 4 - Create a task to transform the data in the txt file
# This task should filter out all the occurrences of ipaddress “198.46.149.143”
transform_data = BashOperator(
    task_id='transform_data',
    bash_command='grep -v "198.46.149.143" /home/project/airflow/dags/capstone/extracted_data.txt > /home/project/airflow/dags/capstone/transformed_data.txt',
    dag=dag,
)

# Task 5 - Create a task to load the data
# This task should archive the file transformed_data.txt into a tar file named weblog.tar
load_data = BashOperator(
    task_id='load_data',
    bash_command='tar -cf /home/project/airflow/dags/capstone/weblog.tar -C /home/project/airflow/dags/capstone transformed_data.txt',
    dag=dag,
)

# Task 6 - Define the task pipeline
extract_data >> transform_data >> load_data

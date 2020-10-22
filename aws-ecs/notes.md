# Elastic Container Service
Cluster
- Multiple EC2 instances which will house the docker containers

Task Definition
- A JSON file that defines the configuration of (upto 10) containers that you want to run

Task
- Launches containers define in task Definition
- Tasks do not remain running once workload is complete

Service 
- Ensures tasks remaining running eg. web-app

Container Agent
- Binary on each EC2 instance which monitors, starts and stops tasks.

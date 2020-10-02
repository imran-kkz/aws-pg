# AWS Developer Certification Studying

Notes before we begin:
- read the whitepapers
	- Architecting for Cloud: AWS Best Practices
	- Practicing CI and CD on AWS

# Elastic Beanstalk

## What is a PAAS
- a platform allowing customers to develop, run, and manage applications without the complexity of building and maintaining the infrastructure typically associated with developing and launching an app
- think of it as the heroku of AWS
- Elastic Beanstalk = EB

- not recommended for "Production applications"
  - aws is talking about enterprise, large companies

- EB is powered by CloudFormation Templates
  - Spins up:
    - ELB
    - Autoscaling groups
    - RDS Database
    - EC2 Instance will come preconfigured
    - Monitoring (CloudWatch, SNS)
    - In-Place and Blue-Green Deployment Methodologies
    - Security (rotates passwords)
    - can run Dockerize Environments

## Web vs Worker env

| Web Environment | Worker Environement |
| front end | background jobs |

### Web Env Types

- Load Balanced Env
  - EC2 instances are set to scale
  - uses ELB
  - Essentially it is designed to scale

- Single-instance Environment (cost effective)
  - Still uses ASG but your desired capacity set to 1 to ensure server is always running
  - no ELB
  - Public IP has to be used to route traffic to server

## Deployment Policies 

### All at once
- Deploy the new app version to all instance at the same time
- takes all instances out of service while the deployment processes
- servers become available again
- This is the fastest but most dangerous Deployment Method
- if there is a major failure here
  - will have to roll back
  - will have downtime

### Rolling
- Deploy the new app version to a batch of instances at a time
- takes batches of instances out of service while the deployment processes
- reattaches updated instances
- gooes onto next batch, taking them out of service
- reattaches those instances (rinse and repeat)
- incase of failure
  - need to perform an additional rolling update in order to roll back the changes

### Rolling w/ additional batch
- launch new instance that iwll be used to replace a batch
- deploy app version to new batch
- attach the new batch and terminate the existing batch
- this way we never reduce our capacity
  - important for applications where a reduction in capacity could cause availability issues for users
  - incase of failures - you nneed to perform rolling updates

### Immutable
- Create a new ASG group with EC2 instances
- Deploy the updated version of the app on the new EC2 instances
- Point the ELB to the new ASG and delete the old ASG which will terminate the old EC2 Instances
- this is the safest way to deploy for critical applications
- In case of failure:
  - you just terminate the new instances since the existing instances still remain

## EB Deployment Methodologies

- 


## In-Place vs Blue/Green Deployment

- not definitive in definition and the context can change the scope of what they mean
- In-Place can mean within the scope of the Elastic Beanstalk Env
  - All deployment policies provided by EB could be considered In-Place since they are within the scope of a single EB Environment
    - All at once
    - Rolling 
    - Rolling w/ additional batch
    - Immutable
- In-Place could mean the scope of the same server (not replacing the server
  - Deployment policies which do not involve the server being replaced
    - All at once
    - Rolling
- In-Place could mean the scope of an uninterrupted server
  - Traffic is never routed away from hte server (taken-out-of-service)
  - Implements Zero-Downtime Deploys where Blue/Greens occurs on the server

### Blue/Green in the context of Elastic Beanstalk
- Immutable (In-Place)
  - When everything is happening inside the environment of EB, your entire environment will have to terminate
  - if you have any databases running in EB - they will also be terminated
- If you run a blue/green deploy, it will mainly be when you have a database outside of your specific EB environment, and want to keep your data
  
### EB Config Files
- EB environments can be customized
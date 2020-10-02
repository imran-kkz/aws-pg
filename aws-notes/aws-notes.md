# AWS Developer Certification Studying

Notes before we begin:
- read the whitepapers
	- Architecting for Cloud: AWS Best Practices
	- Practicing CI and CD on AWS

***
# Cheat Sheet
- Elastic Beanstalk handles the deployment, from capacity provisioning, load balancing, auto-scaling, to application health monitoring
- When you want to run a web-application but you dont want to have to think aobut the underlying infrastructure
- It costss nothing to use Elastic Beanstalk (only the resources it provisions eg. RDS, ELB, EC2)
- Recommended for test or dev apps. Not recommended for prod use
- You can choose from the following preconfigured platforms
  - Java, .NET, PHP, Mode.js, Python, Ruby, Go, Docker
- You can run containers on EB either in Single-Container or Multi-Container, these containers are running on ECS instead of EC2
- You can launch a web environment or worker environment
  - web envs come in 2 types: single instance or load balanced
    - single env launches a single EC2 instance, EIP is assigned to the EC2
    - load balanced env launchs EC2s behind an ELB managed by an ASG
  - Worker env creates an SQS queue, install the SQS daemon on the EC2 instances, and has ASG scaling policy which will add or remove instances based on queue size
- EB has the following deployment policies:
  - All at once takes all servers OOS, applies the changes, and then restarts those servers
    - this is fast but it has downtime
  - Rolling
	- updates servers in batches which reduces capacity of the whole env
  - Batch Rolling
    - update servers with an extra batch which will replace the old servers
      - this doesnt reduce capacity
  - Immutable
    - creates the same amt of servers and replaces all the code to new servers, terminates old ones
- Rolling deployment policies requires an ELB and so cannot be used with single-instance web environments
- In-Place deployment is when deployment occurs within the environment, all deployment policies are In-Place
- Blue/Green
  - When deployment swaps environments (outside an environment), when oyu have external resources rush as RDS which cannot be destroyed - this is suited to Blue/Green
- .ebextensions is a folder which contains all configuration files
- with EB you can provide a custom image which can improve provisioning times
- if you let EB create the RDS instance, that means when you delete your env, it will delete the database. this setup is intended for dev and test envs
- Dockerrun.aws.json is similar to a ECS task definition file and defines multi container configuration

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
- EB environments can be customized using configuration files
- .ebextensions is a hidden folder called at the root of your project which contactions the config files
- .config is the extension for the config files which need to be stored in .ebextensions

- Configurations files can config:
  - option settings
  - linux/windows server configuration
  - custom resources

### Env Manifest
- the environment manifest is a file called env.yml which is stored at the root of your project
- when creating new elastic beanstalk environments this file allows you to configure the defaaults such as:
  - the name of the environment
  - choosing the stack solution
  - associating the environment links
  - default config of servers
  - etc.
    - you can use the + symbol to add on to your env names for unique variables

### Server Configuration
- Need to configure downloading packages
  - generally will be yum
- Groups 
  - assign group ids (ex. Docker)
- Users
- Files
  - providing something like a yml file
- commands 
  - these are commands that you want to run before your code is in the environment
- services
  - define which services should be started or stopped when the instance is launched
- container commands 
  - execute commands that affect your application source code

## EB CLI
- the CLI is hosted on GitHub 
  - simple as cloning the repo
- Some simple commands:
  - eb init
    - configure your project directory and the EB CLI
  - eb status
    - see the current status of your env
  - eb health
    - view health info about the instances and the state of your overall env (use --refresh to update every 10s)
  - eb events
    - see a list of events output by EB
  - eb logs 
    - pull logs from an instance in your env
  - eb open
    - open your env's website in a browser
  - eb deploy
    - once the env is running, deploy an update
  - eb config
    - take a look at the configuration options abailable for your running env
  - eb terminate 
    - delete the environment

## EB Custom Image
- you can specify your own AMI 
  - this is useful if you have a lot of packages that you need to install and so this way you can just bake it into an AMI

Steps:
1. AWS Docs 
   1. get the platform info to use the cli to understand `describe-platform-version`
2. go to the EC2 marketplace and launch the server
3. login using ssl or sessions manager
4. configure however you want
5. bake the AMI
6. set the AMI and set the new environments

## Configure RDS database
- the database can be added inside or outside your EB environment

Inside EB Env
- intended generally for dev envs
- you create the database within EB
- when the EB env is terminated, the database will also be terminated

Outside EB Env
- intended for production envs
- you know you're doing this when you are creating your database first in RDS and then you configure it with your EC2 instances inside EB env
- when the EB env is terminated the database will remain

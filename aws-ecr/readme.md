# AWS ECR 

This is a containerized flask app that can run in AWS ECR
- this is just mainly for learning purposes and studying for AWS cert
- code pulled from https://github.com/linuxacademy/cda-2018-flask-app


# How to containerize and run in AWS ECR

1. login to aws ec2 instance
2. install docker on the machine
   1. add $USER to docker group for running cmds w/o sudo
3. clone into this repo
   1. Commands to enter are as follows:
      1. `cd awspg`
      2. `cd aws-ecr`
      3. `docker build -t penguin-app-linuxacademy .`
      4. `docker image ls` to see the new image that you have created
      5. you can also run the following command for testing: `docker run -p 80:80 penguin-app-linuxacademy`  
4. While staying inside the repository, run the following:
   1. `aws ecr create-repository --repository-name {enter name you wish}`
   2. Copy down the repositoryUri link for quick reference
   3. use the aws cli to login to ecr docker registry and upload the image you have just created using the following command: `aws ecr get-login --region {your region} --no-include-email`
      1. this will print out a docker login cmd that you copy and paste into your terminal
   4. Once you are succefully logged in lets follow along to upload the image to the repo
      1. `docker tag penguin-app-linuxacademy:latest {enter your repositoryUri link here!!}`
      2. `docker push {newly tagged image}`
5. Congrats, you've just pushed an image to aws-ecr!
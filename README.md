End to End Machine Learning Project - CI/CD"# mlproject" 

-- Create project structure.
-- Then setup.py to create pacakage
-- Create Exception and Logger python file 
-- I run notebook just to do EDA .
-- I write data_ingestion script and than data_transformation. Pipelines define for transformation
-- I write helper function in utils.py 
-- Create Api 


## AWS CI-CD Deployment ##

Step 1:-Create Docker File and write below code

FROM python:3.8-slim-buster
WORKDIR /app
COPY . /app
RUN apt update -y && apt install awscli -y
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 unzip -y && pip install -r requirements.txt
CMD ["python3", "app.py"]


Step 2:- Create Docker Image --Docker hub where all docker images can be there and can access by public

open terminal and type    docker build -t studentperformance-app .
docker images
docker run -d -p 8080:8080 studentperformance-app

#############################################################################
Step3:-Now create .github-->workflows folder and create main.yaml file. 

This file will run whenever push on any main branch and ignore readme file . JOb will divided into 3 part .
A) Continous integration
B)Build and Push ECR image
C) Continous Deployment 

This file we can get from github -->Action-->workflow

###############################################################

Step4:- IAM Setting in AWS

1) Add user and give access of "AmazonEC2ContainerRegistryFullAccess" and "AmazonEC2ContainerRegistry"
 
2) click to user--> username-->security_credential--> Click to access key(below you will see)-->CLI--> Next--> create access key--> Download .csvfile(having info of secret key) --> Done

########################################################################

Step5:- Setup ECR (Amazon Elastic Container Registry (Amazon ECR) is an AWS managed container image registry service that is secure, scalable, and reliable.So we will use ECR to copy our Docker image)

Search ECR--> Get Started-->create repo-->Private-->Give repo name -->create repo--> copy url 

This url we will use for ECR_login , note somewhere .

########################################################################################

Step6:- EC2 Setup

Search EC2--> Launch instance--> Give Web Server name --> select ubuntu--> t2.medium --> key pair name (we can create new one)---
---> check on "Allow HTTPS traffic from internet" and "Allow HTTP traffic from internet" --> Launch instance--> check instance --
--->click instance id --> connect(cmd will open)

Now machine created and need docket setup in it by running few commands

sudo apt-get update -y
sudo apt-get upgrade
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
 Now can check docker is configured or not by type "docker"

Setup Github runner
Github Setting---> Actions--> Runners-->Click at New self-hosted runner--> select Linux--> Now you will see command which need to run on EC2 as shown below

mkdir actions-runner && cd actions-runner
curl -o actions-runner-linux-x64-2.303.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.303.0/actions-runner-linux-x64-2.303.0.tar.gz
echo "e4a9fb7269c1a156eb5d5369232d0cd62e06bec2fd2b321600e85ac914a9cc73  actions-runner-linux-x64-2.303.0.tar.gz" | shasum -a 256 -c
tar xzf ./actions-runner-linux-x64-2.303.0.tar.gz
./config.sh --url https://github.com/gaurav4726/mlproject --token AJQ5XJ74ZFGQ5O4XBCJDUPLEHJAE6

Press Enter
Enter the name of runner : self-hosted 
Press Enter
Press Enter

runs-on: self-hosted

Now check Github Setting---> Actions--> Runners-->Click at New self-hosted runner--> self-hosted will created and marked as green 


Launch EC2 instance--> security-->edit inbound rule--> Set custom tcp , port 8080, source custom 0.0.0.0/0
Note: port in app.py set 8080 also

Now you will launch instance you will see ip which is app ip of cloud --Ex:8.28.123.80:8080

########################################################################

Step7:- Add Keys :-

Goto Github setting --> secret&variables--> Actions --> Add 5 keys by clicking New repository secret

AWS_ACCESS_KEY_ID= Take from csv which we download during step 4

AWS_SECRET_ACCESS_KEY=Take from csv which we download during step 4

AWS_REGION = Ex:-us-east-1 ( Need to check in AWS)

AWS_ECR_LOGIN_URI = Ex:- 696637341622.dkr.ecr.ap-south-1.amazonaws.com(Url of ECR in step5 , take before /)

ECR_REPOSITORY_NAME = Ex:-simple-app(Url of ECR in step5 , take after /)

## This is full setup for deployment if want to close than close EC2 and ECR both ## 













































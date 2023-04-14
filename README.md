End to End Machine Learning Project - CI/CD"# mlproject" 

Create project structure.
Then setup.py to create pacakage
Create Exception and Logger python file 
I run notebook just to do EDA .
I write data_ingestion script and than data_transformation. Pipelines define for transformation
I write helper function in utils.py 


AWS CI-CD Deployment 

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


Step3:-Now create .github-->workflows folder and create main.yaml file. 

This file will run whenever push on any main branch and ignore readme file . JOb will divided into 3 part .
A) Continous integration
B)Build and Push ECR image
C) Continous Deployment 


This file we can get from github -->Action-->workflow

Step4:- IAM Setting in AWS
























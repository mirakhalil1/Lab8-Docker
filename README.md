# Lab 8 - Docker and Containers

## Activity 1
Docker container commands:
- docker ps -a
- docker logs lab8_hello
- docker stop lab8_hello

## Activity 2
Two Flask API Docker images:

### Image 1
Tag: 0.0.1-RELEASE
Port: 5000
Endpoint: /api/users

### Image 2
Tag: 0.0.2-RELEASE
Port: 3000
Endpoint: /get_users

## Docker Build Commands

docker build -f Dockerfile.lab5 -t mirakhalil1/lab8-mira_khalil:0.0.1-RELEASE .

docker build -f Dockerfile.users -t mirakhalil1/lab8-mira_khalil:0.0.2-RELEASE .

## Docker Run Commands

docker run --name lab8_api_5000 -p 5000:5000 -d mirakhalil1/lab8-mira_khalil:0.0.1-RELEASE

docker run --name lab8_api_3000 -p 3000:3000 -d mirakhalil1/lab8-mira_khalil:0.0.2-RELEASE

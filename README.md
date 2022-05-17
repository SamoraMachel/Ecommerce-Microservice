# Microservices with Flask
A simple flask application for practising microservices with kafka and coackroach db

## Software dependacies
In order to run the project, the application relies on..
 - docker
 - python 3

## Configuration 
First you'll have to create a network for the database to function properly
```bash 
docker network create -d bridge network_cockroachdb
```
EQObject service
=============

This is a basic test service. It serves as a template for others easy-queue modules.

# Develop in local
To create a python environment for development:
> conda env create -f environment.yml \
conda activate easy-queue

# Deploy with Docker

To build image (from Dockerfile folder):
> docker build --tag eqobject-service .

To run image:
> docker run -p 15000:15000 --name eqobjectservice eqobject-service

To start/stop image
> docker start eqobjectservice

> docker stop eqobjectservice

API Rest will be available on [EQObject Swagger](http://localhost:15000/eqobject/api/#/)
# bandw

This repository contains oversimplified version of wandb service: bandw - beights and wiases.

Bandw gives ability to log something locally and then to access plots of logs in browser.

## Usage

Using this repository requires docker and docker-compose installed

### Setup server

To setup local server following commands have to be run:
```
cd app
docker network create redis-net
docker-compose up
```
These commands create network for access to redis database and start the server.

### Loging

Folder `examples` contains a simple example which logs random values.

To run example run following commands from the root of the repository:

```
docker build -f examples/Dockerfile -t bandw_example .
docker run --net redis-net bandw_example
```

To use bandw one has to put the command below into Dockerfile because bandw is not a pip package:

```
COPY bandw bandw
```

### Web page

The plots of logs can be accesed at `0.0.0.0:8080`

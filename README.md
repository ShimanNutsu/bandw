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

To run examples run following commands from the root of the repository:

For random logger:
```
docker build -f examples/random_logger/Dockerfile -t random_example .
docker run --net redis-net random_example python main.py
```

For simple conv net trainig with logging:
```
docker build -f examples/simple_cnn/Dockerfile -t simple_cnn .
docker run --net redis-net simple_cnn python main.py
```
(Code for this example was stolen from github.com/pytorch/examples/tree/main/mnist)

To use bandw one has to put the command below into Dockerfile because bandw is not a pip package:

```
COPY bandw bandw
```

### Web page

The plots of logs can be accessed at `0.0.0.0:8080`

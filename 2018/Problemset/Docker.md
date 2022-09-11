# Docker

## Problem Statement

This problem deals with playing around docker (<https://www.docker.com/>), which is a containerization technology. Your task is simple.

Upload an ubuntu docker image to [docker store](https://store.docker.com/) or [docker hub](https://hub.docker.com/) with your username. This image should contain a file in the `/home` directory with the name `testfile.sh` and the following contents:

```txt
#!/bin/sh
echo "My name is Sahil Arora, and my container works!"
```

Replace my name with yours here. When I run your image using `docker run IMAGE_NAME`, this is what I should see on my machine's terminal(not the docker container's terminal):

```txt
My name is Sahil Arora, and my container works!
```

Anybody around the world if has to do this, he must be able to type a simple command `docker run IMAGE_NAME` and should see this output on his terminal. Here `IMAGE_NAME` is the name of the image which you set.


## Weightage

135 points

## Deliverables

In your git repository whose link you will be submitting, make 2 files:

1. `Docker.md`: Here you need to write the report as to how you did this, what all resources you took help from, and what you learnt. You also need to give a link to your image on `docker store`/`docker hub`.
2. `Dockerimage`: This file should have the name of the image which you set, i.e. `IMAGE_NAME`. For instance, if the name of your image is `sahilarora535/testimage`, this should be the only content in this file.

Remember, do not worry if you are unable to complete it, just document whatever you were able to do. :) 

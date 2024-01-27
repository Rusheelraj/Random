## Docker-installation:

``` $ sudo apt install docker-compose docker ```

Check and test a sample docker image:

``` $ sudo docker run hello-world ```

How to create a docker image:
```
$ mkdir new_docker
$ sudo nano Dockerfile (write all the required dependencies and OS for your docker image) 
```

Save the dockerfile 

Build an image from a Dockerfile:
``` sudo docker build -t <image_name> ```

Build an Image from a Dockerfile without the cache:

``` sudo docker build -t <image_name> . –no-cache```

List local images:

``` sudo docker images ```

Delete an Image:
``` sudo docker rmi <image_name> ```

Remove all unused images:
``` sudo docker image prune ```

## Docker-Hub:

Login into Docker:
```sudo docker login -u <username>```

Publish an image to Docker Hub:
``` sudo docker push <username>/<image_name> ```

Search Hub for an image:
``` sudo docker search <image_name> ```

Pull an image from a Docker Hub:
``` sudo docker pull <image_name>``` 

## General Commands

Get help with Docker:
``` sudo docker --help ```

Display system-wide information:
``` sudo docker info```

## Containers

Create and run a container from an image, with a custom name:
``` sudo docker run --name <container_name> <image_name> ```


Run a container in the background:
``` sudo docker run -d <image_name>``` 

Start or stop an existing container:
``` sudo docker start|stop <container_name> (or <container-id>) ```

Remove a stopped container:
``` sudo docker rm <container_name>```

Open a shell inside a running container:
``` sudo docker exec -it <container_name> sh```

Explanation: This command is used to open a new shell session inside an already running Docker container. Replace <container_name> with the name or ID of your running Docker container.

``` sudo docker run -it --rm <image_name> sh or (bash) //depending on the type of the OS```

Explanation: This command is used to start a new Docker container from an image, and it immediately opens a shell session inside the new container. The --rm flag means that the container will be automatically removed after you exit the shell. 

``` To list currently running containers:```
sudo docker ps

``` List all docker containers (running and stopped):```
sudo docker ps --all

## Code your own Dockerfile:

FROM {docker-image} or FROM {docker-image}:{latest}

Example: FROM ubuntu:latest

MAINTAINER {name}

Example: MAINTAINER Rusheel Raj Panakadan

RUN {command}

Example: RUN apt-get update && apt-get install -y nginx // Execute commands during image build process.

CMD {command}

Example: CMD ["nginx", "-g", "daemon off;"] or CMD ["/bin/sh"] 

Note: Can be executed only once in a Dockerfile. Takes the last CMD as final. Set the default command to be executed when the container is run.

LABEL maintainer = "Rusheel Raj" 

Example: LABEL version = "2.0" or LABEL description = "Kali linux docker"

EXPOSE {port/protocol}

EXPOSE 80/udp // Default TCP port is exposed. 

docker run -p 8080:80 {image}

ENV {key} = {value} 

Example: ENV SHELL /bin/bash or ENV DEBIAN_FRONTEND = noninteractive

ADD {src} {dst} 

Example: ADD file.txt /app/ or ADD mydir/ /app/ or ADD <link> /app/ or ADD file.txt /app/newfile.txt

COPY {src} {dst} 

Note: Same as ADD, but no advanced features like ADD (uncompression, URL fetch)

ENTRYPOINT ["echo", "Hello,", "World"] // when docker is run, it directly prints out "Hello World"

// RUN useradd -ms /bin/bash rusheel

USER rusheel // Switches to user rusheel 

WORKDIR {path}

Example:

WORKDIR /home/kali/important

ARG {name} = {default_value}

Example:

```
ARG version=latest // by default
FROM ubuntu:$version
RUN echo "The version is $version"
```

Execute: docker build --build-arg version=20.04 -t <image> . //Dynamic allocation


ONBUILD {Dockerfile-instruction}

Example:

```
FROM alpine
RUN apt-get update && apt-get install -y apache2
ONBUILD COPY . /var/www/html
ONBUILD EXPOSE 80
```

It allows you to define certain actions or instructions that should be performed automatically when another image is built on top of the current one.

STOPSIGNAL {signal} // Either it can be an integer value or signal name ( 9 or SIGKILL)

Example:

```
FROM ubuntu:latest
STOPSIGNAL SIGTERM // When you run docker stop, this is the system call signal sent to the container's main process.
CMD ["sleep", "infinity"]
```

Other functions: SIGKILL - 9 (immediate termination - forceful), SIGINT - 2 (Similar to SIGTERM, Interrupt signal - Ctrl + C), SIGQUIT - 3 (Similar to SIGINT, but also generates a core dump of the process).

HEALTHCHECK {options} CMD {command} 

{options} : --interval = duration, --timeout = duration, --retries = duration

Command exit status: 0:success/healthy, 1:unhealthy, 2:reserved (do not use this exit code)

Example: 
```
FROM ubuntu:latest
HEALTHCHECK --interval=30s --timeout=10s --retries=3 CMD ["ping", "-c", "1", "google.com"]
```

$ docker inspect --format='{{.State.Health.Status}}' <container_id>

Output can be 3 values: Starting, Healthy, Unhealthy

SHELL ["{executable}", "{param1}", "{param2}"]

Example:

```
FROM microsoft/windowsservercore
RUN echo rusheel // Prints rusheel; using cmd terminal
RUN powershell -command Write-Host rusheel // Prints rusheel; using powershell terminal (temporary changed)
SHELL ["powershell", "-command"]
RUN Write-Host rusheel // prints rusheel; using powershell terminal (permanently changed)
SHELL ["cmd", "/S", "/C"]
RUN echo rusheel // prints rusheel; using cmd terminal (permanently changed again!) 
SHELL ["/bin/bash", "-c"]
RUN echo "rusheel"; prints rusheel; using /bin/bash terminal (permanently changed again !!)
```

## Sample Dockerfile using the above stated commands

```
FROM ubuntu:latest
MAINTAINER Rusheel Raj Panakadan
RUN apt-get update && apt-get install -y nginx
ENV SHELL /bin/bash
ENV DEBIAN_FRONTEND noninteractive
LABEL version="1.0" description="Simple Nginx container with Ubuntu base"
EXPOSE 80/tcp
WORKDIR /app
COPY index.html /app/
CMD ["nginx", "-g", "daemon off;"]
```

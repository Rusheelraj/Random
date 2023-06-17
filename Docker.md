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

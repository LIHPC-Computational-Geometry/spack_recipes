# Using containers
## Podman

We decide to use [Podman](https://podman.io/) instead of docker as it does not require to be root. Podman and docker commands are identical. To use Podman, we start by removing all docker applications from our laptop (if docker is installed).

### Uninstall docker

To completely uninstall Docker:

*Step 1* 

    dpkg -l | grep -i docker

To identify what installed package you have:

*Step 2*

    sudo apt-get purge -y docker-engine docker docker.io docker-ce docker-ce-cli docker-compose-plugin
    sudo apt-get autoremove -y --purge docker-engine docker docker.io docker-ce docker-compose-plugin

The above commands will not remove images, containers, volumes, or user created configuration files on your host. If you wish to delete all images, containers, and volumes run the following commands:

    sudo rm -rf /var/lib/docker /etc/docker
    sudo rm /etc/apparmor.d/docker
    sudo groupdel docker
    sudo rm -rf /var/run/docker.sock

### Install Podman

To install Podman:

    sudo apt-get -y install podman


## X11 and Open GL applications in a container

### Build the image

You will build an image on your computer. Download the [`images/Dockerfile.x11ogl`](https://raw.githubusercontent.com/LIHPC-Computational-Geometry/lihpccg-ci/main/images/Dockerfile.x11ogl) file and enter the following command:

    podman build -t lihpccg/x11ogl . -f Dockerfile_x11ogl --format docker

**Note:** Podman and docker commands are identical. To build an image with Podman and a Docker file do not forget the `--format docker` option for the build command (see below).

### Run the container

    podman run -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY --device /dev/dri --rm -it lihpccg/x11ogl bash

- `--rm` By default a container’s file system persists even after the container exits. This option automatically cleans up the container; helpful for running short-term processes.

- `-it` By default, the container runs and terminates. This option and `bash` at the end of the command opens a bash terminal inside the container.

- `-v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY --device /dev/dri` Options needed to open the display when running X11 applications.

Then, you are in a terminal inside the container. Just test the execution of `xeyes` and `glxgears` and check that a window is displayed and that the application is active (eyes are moving and gears are turning).

Enter CTRL-D to quit the container.

## Using the container in VSCode

In the following use cases, we have a `lihpccg` directory on our computer, containing a git clone of all (or a subset) of the [lihpccg GitHub](https://github.com/LIHPC-Computational-Geometry) projects. We consider that the `lihpccg` directory will be our VSCode root folder.
### Build and open a container from an image

To execute our x11ogl container in VSCode: 
- Create a `lihpccg/.devcontainer` directory and copy the [`devcontainer.json`](https://raw.githubusercontent.com/LIHPC-Computational-Geometry/lihpccg-ci/main/devcontainer.json) in it.
- Launch VSCode and click on `File>Open Folder` menu and select `lihpccg` directory.
- VSCode should automatically ask you if you want to install the `Dev Container` extension. In this case, just accept it otherwise install the extension (clik on the Extensions icon in the Activity Bar on the left and search extension in marketplace in the top left search bar).
- Launch the container with CTRL-P and select `Dev Containers: Rebuild and Reopen in Container`. Wait for the container to start and open a terminal (Terminal menu in top menu bar). The terminal is open in the container.
- Test the execution of `xeyes` and `glxgears` and check that a window is displayed and that the application is active (eyes are moving and gears are turning).

If you want to work with the container used in lihpccg GitHub CI, change the container on the line 2-3 of the `devcontainer.json` file and rebuild and restart the container.

**Note:** VSCode will install a server into the remote container into the `/vscode-server` directory. It will also save the user preferences (extensions...) into the `${HOME}/.vscode-server` directory. Do not set the home folder to `/dev` directory in your Dockerfile (`ENV HOME /dev`). It is a shared memory folder with (in general) not enough space to store user preferences.

### Attach to a running container

We have a running container on our machine and we want to open our `lihpccg` workspace in it.

Attach the container with CTRL-P and select `Dev Containers: Attach to Running Container...`. VSCode will propose you a list of existing containers. Just select the desired container to be connected to it.
## Podman memo

### Useful commands

- `podman images` to list available images.
- `podman rmi <image id>` to remove an image.
- `podman ps -a` to see all containers.
- `podman rm <container id>` to remove a container.
- `podman run --rm -it <image id> bash` to run an image and open a terminal in it. The `--rm` option is used to remove the container when closing it.
- `podman exec -it <container id> bash` to open a bash terminal in a container.
- `podman build --no-cache -f <dockerfile name> -t <image name> --format docker` to build an image from a docker file. **Do not forget the `--no-cache` option** specially if your dockerfile contains `git clone` commands. Without it, if you have several images with the same repository cloned, your workspace can be outdated.

### Using dockerhub to store images

- `podman login docker.io` to log to your dockerhub account.
- `podman push <image name>` to push your local image to dockerhub.
- `podman pull <image name>` to pull a dockerhub image to your local registry.

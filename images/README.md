# Directory content

- `Dockerfile`: file to build the docker image used in lihpc products CI on github.
  Building the image is quite a long process depending on your computer.
  The image is available on [Dockerhub](https://hub.docker.com/repository/docker/lihpccg/mgx-ubuntu.20.04-spack.0.19.0/general) and it can be pulled (see below for details).

- `Dockerfile_x11ogl`: file to build a container including `xeyes` and `glxgears`.
  Do not hesitate to build the image to test if X11 and Open GL applications run in your environment (see below).

- `devcontainer.json`: example file to use a container in VSCode (see below).

- `registries.conf`: file to copy to ̀`/etc/containers` to use dockerhub.

# Podman

We decide to use [Podman](https://podman.io/) instead of docker as it does not require to be root. Podman and docker coimmands are identical. To use Podman, we start by removing all docker applications from our laptop (if docker is installed).

## Uninstall docker

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

## Install Podman

To install Podman:

    sudo apt-get -y install podman


# X11 and Open GL applications in a container

## Build the image

You will build an image on your computer. Use the  `Dockerfile_x11ogl` provided here:

    podman build -t lihpccg/x11ogl . -f Dockerfile_x11ogl --format docker

**Note:** Podman and docker commands are identical. To build an image with Podman and a Docker file do not forget the `--format docker` option for the build command (see below).

## Run the container

    podman run -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY --rm -it lihpccg/x11ogl bash

- `--rm` By default a container’s file system persists even after the container exits. This option automatically cleans up the container; helpful for running short-term processes.

- `it` By default, the container runs and terminates. This option and `bash` at the end of the command opens a bash terminal inside the container.

- `-v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY` Options needed to open the display when running X11 applications.

Then, you are in a terminal inside the container. Just test the execution of `xeyes` and `glxgears` and check that a window is displayed and that the application is active (eyes are moving and gears are turning).

Enter CTRL-D to quit the container.

# Using the container in VSCode

## Use case

We have a `lihpccg` directory on our computer, containing a git clone of all (or a subset) of the [lihpccg GitHub](https://github.com/LIHPC-Computational-Geometry) projects. We consider that the `lihpccg` directory will be our VSCode root folder.

## Commands

To execute our x11ogl container in VSCode: 
- Create a `.devcontainer` directory in  `lihpccg` directory and copy the `devcontainer.json` file provided (see above).
- Launch VSCode and click on `File>Open Folder` menu and select `lihpccg` directory.
- VSCode should automatically ask you if you want to install the `Dev Container` extension. In this case, just accept it otherwise install the extension (clik on the Extensions icon in the Activity Bar on the left and search extension in marketplace in the top left search bar).
- Launch the container with CTRL-P and select `Dev Containers: Rebuild and Reopen in Container`. Wait for the container to start and open a terminal (Terminal menu in top menu bar). The terminal is open in the container.
- Test the execution of `xeyes` and `glxgears` and check that a window is displayed and that the application is active (eyes are moving and gears are turning).

If you want to work with the container used in lihpccg GitHub CI, change the container on the line 2-3 of the `devcontainer.json` file and rebuild and restart the container.

**Note:** VSCode will install a server into the remote container into the `/vscode-server` directory. It will also save the user preferences (extensions...) into the `${HOME}/.vscode-server` directory. Do not set the home folder to `/dev` directory in your Dockerfile (`ENV HOME /dev`). It is a shared memory folder with (in general) not enough disk space to store user preferences.


# TODO

- Modify GitHub CI with the new image.
- Try to instantiate a Qt class in the CI to execute preferences project test.

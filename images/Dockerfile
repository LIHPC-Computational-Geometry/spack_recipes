#============== OS LAYER ==================
# In ubuntu:20.4 the Open GL version is too old to execute in container
# Ubuntu 22.04 allows to execute glxgears in a docker container
FROM ubuntu:22.04
#==========================================
# METADATA OF THE IMAGE
LABEL description "Build env" version="1.0" maintainer="Meshing team <lihpccg@gmail.com>"
#==========================================
ARG SPACK_VERSION=0.19.0
# Do not use /dev as the HOME if you use containers in vscode
# /dev is too small to store .vscode-server directory containing user preferences
# ENV HOME /dev
#==========================================
SHELL ["/bin/bash", "-c"]
#==========================================
ENV TZ=Europe/Paris
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
#==========================================
# libxt-dev has been added in 01/23 to compile VTK.
# Error msg without libxt-dev: "X11_Xt_LIB could not be found. Required for VTK X lib."
RUN apt update &&\
    apt install -y build-essential cmake python3 python3-distutils python3-venv unzip zip curl git libxt-dev libgl-dev gfortran &&\
    apt clean &&\
    rm -rf /var/lib/apt/lists/*
#==========================================
RUN git clone --depth=1 -b v${SPACK_VERSION} https://github.com/spack/spack.git &&\
    git clone --depth=1 https://github.com/LIHPC-Computational-Geometry/spack_recipes_meshing.git &&\
    cp spack_recipes_meshing/config/packages.yaml /spack/etc/spack/ &&\
    cp spack_recipes_meshing/supersede_repo/packages/petsc/*.* /spack/var/spack/repos/builtin/packages/petsc &&\
    cp spack_recipes_meshing/supersede_repo/packages/opencascade/*.* /spack/var/spack/repos/builtin/packages/opencascade &&\
    cp -r spack_recipes_meshing/supersede_repo/packages/vtk-maillage /spack/var/spack/repos/builtin/packages

RUN source /spack/share/spack/setup-env.sh && \
    spack config --scope site add 'packages:all:target:[x86_64]' && \
    spack compiler find && \
    spack external find cmake

RUN sed -i 's#"${ARCHITECTURE}/${COMPILERNAME}-${COMPILERVER}/${PACKAGE}-${VERSION}-${HASH}"#"${PACKAGE}-${VERSION}"#g' spack/etc/spack/defaults/config.yaml
#==========================================
RUN source /spack/share/spack/setup-env.sh && \
    spack env create meshing-env &&\
    spack env activate meshing-env &&\
    spack add python@3 &&\
    spack add qt@5.14.2 &&\
    spack add hdf5+cxx~mpi &&\
    spack add opencascade &&\
    spack add vtk-maillage~mpi &&\
    spack add cgns~mpi &&\
    spack add swig &&\
    spack concretize &&\
    spack install &&\
    rm -rf /spack/var/spack/cache/*
#==========================================

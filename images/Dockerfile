#============== OS LAYER ==================
FROM ubuntu:20.04
#==========================================
# METADATA OF THE IMAGE
LABEL description "Build env" version="1.0" maintainer="Meshing teamp <lihpccg@gmail.com>"
#==========================================
ARG SPACK_VERSION=0.19.0
#==========================================
SHELL ["/bin/bash", "-c"]
#==========================================
ENV TZ=Europe/Paris
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
#==========================================
RUN apt update &&\
    apt install -y build-essential cmake python3 python3-distutils python3-venv unzip zip curl git libgl-dev gfortran-9 &&\
    apt clean &&\
    rm -rf /var/lib/apt/lists/*
#==========================================
RUN git clone --depth=1 -b v${SPACK_VERSION} https://github.com/spack/spack.git &&\
    git clone --depth=1 https://github.com/LIHPC-Computational-Geometry/spack_recipes_meshing.git &&\
    cp spack_recipes_meshing/config/packages.yaml /spack/etc/spack/ &&\
    cp spack_recipes_meshing/supersede_repo/packages/petsc/package.py spack/var/spack/repos/builtin/packages/petsc/package.py

RUN source /spack/share/spack/setup-env.sh && \
    spack config --scope site add 'packages:all:target:[x86_64]' && \
    spack compiler find
RUN sed -i 's#"${ARCHITECTURE}/${COMPILERNAME}-${COMPILERVER}/${PACKAGE}-${VERSION}-${HASH}"#"${PACKAGE}-${VERSION}"#g' spack/etc/spack/defaults/config.yaml
#==========================================
RUN source /spack/share/spack/setup-env.sh && \
    spack env create meshing-env &&\
    spack env activate meshing-env &&\
    spack add python@3 &&\
    spack add qt@5.14.2 &&\
    spack add hdf5+cxx~mpi &&\
    spack add opencascade@7.4.0 &&\
    spack add vtk~mpi &&\
    spack add cgns~mpi &&\
    spack add swig &&\
    spack concretize &&\
    spack install &&\
    rm -rf /spack/var/spack/cache/*
#==========================================

#==========================================
# First get a spack release
git clone --depth=1 -b v0.20.1  https://github.com/spack/spack.git
#==========================================
# can be mandatory if you have already used spack on your computer
# delete the .spack directory in the home of the user 
#==========================================
# our recipes
git clone https://github.com/LIHPC-Computational-Geometry/spack_recipes.git
#==========================================
# hard-coded modifications to spack configuration

# this is used to declare opengl as non buildable and use the system library 
cp ./spack_recipes/config/packages.yaml ./spack/etc/spack/

# to register our recipes; it assumes that spack_recipes and spack are located at
# the same level. You can use the "spack repo add" commands instead of copying the repos.yaml file
#spack repo add ./spack_recipes/meshing
#spack repo add ./spack_recipes/meshing_supersede
cp spack_recipes/config/repos.yaml spack/etc/spack/defaults/repos.yaml

#==========================================
# configure spack; it modifies the .spack directory in the user home
source ./spack/share/spack/setup-env.sh
spack clean -a
spack external find cmake

spack compiler find
# spack uses the highest version of the compiler found by default; if it is incomplete,
# for example the C compiler is installed but not the CXX one the installations will fail.
# Compilers found can be investigated by (see `spack help compiler` commands)
#spack compiler list
#spack compiler info gcc
# An undesirable version can be removed by editing ~/.spack/linux/compilers.yaml or using
#spack compiler remove gcc@12

#==========================================

# +mpi should actually be ok, but currently the default openmpi install fails
spack spec magix3d ^vtk-maillage~opengl2+qt~mpi ^hdf5~mpi ^cgns~mpi ^mesquite~mpi
#spack install magix3d ^vtk-maillage~opengl2+qt~mpi ^hdf5~mpi ^cgns~mpi ^mesquite~mpi

# to work on the main branch
git clone git@github.com:LIHPC-Computational-Geometry/magix3d.git
spack dev-build -d ./magix3d magix3d@2.2.7 ^vtk-maillage~opengl2+qt~mpi ^hdf5~mpi ^cgns~mpi ^mesquite~mpi

# to configure an IDE
# get the CMAKE_PREFIX_PATH with ';' as separators
#spack load --only dependencies --sh magix3d | grep CMAKE_PREFIX_PATH | awk -F "=" {'print $2'} | sed 's/:/;/g'

#==========================================
# testing the install
#export PYTHONPATH=spack/opt/spack/gmds/lib:$PYTHONPATH
#spack load py-pytest
#pytest gmds/pygmds/tst gmds/test_samples
#==========================================

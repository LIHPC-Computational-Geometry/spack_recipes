#==========================================
# First get a spack release
git clone --depth=1 -b v0.20.1  https://github.com/spack/spack.git
#==========================================
# can be mandatory if you have already used spack on your computer
# delete the .spack directory in the home of the user 
#==========================================
git clone https://github.com/LIHPC-Computational-Geometry/spack_recipes.git

# this is used to declare opengl as non buildable and use the system library 
cp ./spack_recipes/config/packages.yaml ./spack/etc/spack/

source ./spack/share/spack/setup-env.sh
spack repo add ./spack_recipes/meshing
spack repo add ./spack_recipes/meshing_supersede
spack compiler find
spack external find cmake
#==========================================

# +mpi should actually be ok, but currently the default openmpi install fails
spack spec magix3d ^vtk-maillage~opengl2+qt~mpi ^hdf5~mpi ^cgns~mpi ^mesquite~mpi
#spack install magix3d ^vtk-maillage~opengl2+qt~mpi ^hdf5~mpi ^cgns~mpi ^mesquite~mpi

# to work on the main branch
git clone git@github.com:LIHPC-Computational-Geometry/magix3d.git
spack dev-build -d ./magix3d magix3d@2.2.7 ^vtk-maillage~opengl2+qt~mpi ^hdf5~mpi ^cgns~mpi ^mesquite~mpi

#==========================================
# testing the install
#export PYTHONPATH=spack/opt/spack/gmds/lib:$PYTHONPATH
#spack load py-pytest
#pytest gmds/pygmds/tst gmds/test_samples
#==========================================

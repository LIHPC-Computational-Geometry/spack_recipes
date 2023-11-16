#==========================================
# First get a spack release
git clone --depth=1 -b v0.20.1  https://github.com/spack/spack.git
#==========================================
# can be mandatory if you have already used back on your computer
# delete the .spack n the home of the user 
#==========================================
git clone https://github.com/LIHPC-Computational-Geometry/spack_recipes.git
cp ./spack_recipes/config/packages.yaml ./spack/etc/spack/
. ./spack/share/spack/setup-env.sh
spack repo add ./spack_recipes/meshing
spack repo add ./spack_recipes/meshing_supersede
spack compiler find
spack external find cmake
#==========================================
git clone git@github.com:LIHPC-Computational-Geometry/magix3d.git
#==========================================
spack spec magix3d ^vtk-maillage~opengl2+qt~mpi ^hdf5~mpi ^cgns~mpi ^mesquite~mpi
spack dev-build -d ./magix3d magix3d@2.2.7 ^vtk-maillage~opengl2+qt~mpi ^hdf5~mpi ^cgns~mpi ^mesquite~mpi
#==========================================
# testing the install
#export PYTHONPATH=spack/opt/spack/gmds/lib:$PYTHONPATH
#spack load py-pytest
#pytest gmds/pygmds/tst gmds/test_samples
#==========================================

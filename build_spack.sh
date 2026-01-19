#==========================================
# First get a spack release
git clone --depth=1 -b v0.23.1  https://github.com/spack/spack.git
#==========================================
# can be mandatory if you have already used spack on your computer
# delete the .spack directory in the home of the user 
#==========================================
# get our recipes
git clone https://github.com/LIHPC-Computational-Geometry/spack_recipes.git
#==========================================
# modifying spack configuration
#==========================================
# hard-coded modifications to spack configuration

# Optionnal: modifying the install_tree variable to make it shorter and more human readable;
# the HASH part in install directory names is removed which can lead to collisions.
# The spack/etc/spack/defaults/config.yaml file can be modified by hand
# - in spack version 0.20.1
#sed -i 's#"{architecture}/{compiler.name}-{compiler.version}/{name}-{version}-{hash}"#"{name}"#g' spack/etc/spack/defaults/config.yaml

# this is used to declare opengl as non buildable and use the system library 
cp ./spack_recipes/config/packages.yaml ./spack/etc/spack/

# to register our recipes; it assumes that spack_recipes and spack are located at
# the same level. You can use the "spack repo add" commands instead of copying the repos.yaml file
#spack repo add ./spack_recipes/meshing
#spack repo add ./spack_recipes/meshing_supersede
cp spack_recipes/config/repos.yaml spack/etc/spack/defaults/repos.yaml

# Optionnal: the default tmpdir used to build is defined in spack/etc/spack/defaults/config.yaml
# under the entry build_stage: $tempdir/$user/spack-stage
# Should one prefer to use a tmpfs or has limited disk space in the temporary dir (Qt's build directory can require up to 6Go on my setup)
# this entry can be modified

#==========================================
# configure spack using spack commands; it modifies the .spack directory in the user home
source spack/share/spack/setup-env.sh
spack clean -a

# registering cmake
spack external find cmake

# registering compilers
spack compiler find
# spack uses the highest version of the compiler found by default; if it is incomplete,
# for example the C compiler is installed but not the CXX one the installations will fail.
# Compilers found can be investigated by (see `spack help compiler` commands)
#spack compiler list
#spack compiler info gcc
# An undesirable version can be removed by editing ~/.spack/linux/compilers.yaml or using
#spack compiler remove gcc@12

#==========================================
# for regular install

# +mpi should actually be ok, but currently the default openmpi install fails
#spack spec magix3d+smooth3d+triton2+doc ^vtk-maillage~opengl2+qt~mpi ^hdf5~mpi ^cgns~mpi ^mesquite~mpi
#spack install magix3d+smooth3d+triton2+doc ^vtk-maillage~opengl2+qt~mpi ^hdf5~mpi ^cgns~mpi ^mesquite~mpi

# install for dev purposes
git clone git@github.com:LIHPC-Computational-Geometry/magix3d.git
# you will probably want build_type=Debug or RelWithDebInfo.
# Choose the variants you need, you can check them using `spack info gmds`.
# The dev_path option does not seem to handle relative paths.
spack install magix3d+smooth3d+triton2+doc dev_path=$PWD/magix3d build_type=Debug ^vtk-maillage~opengl2+qt~mpi ^hdf5~mpi ^cgns~mpi ^mesquite~mpi

# to configure an IDE
# spack created files and directories named gmds/spack-* in the gmds source tree, where the necessary
# options are set up
# get the CMAKE_PREFIX_PATH with ';' as separators
# NOTE: in spack version >= 0.22 the spack-build-env.txt is located in magix3d/build-systemname-hash/spack-build-env.txt
cat magix3d/build-*/spack-build-env.txt  | grep CMAKE_PREFIX_PATH | awk -F "=" {'print $2'} | awk -F ";" {'print $1'} | sed 's/:/;/g'
#spack load --only dependencies --sh magix3d | grep CMAKE_PREFIX_PATH | awk -F "=" {'print $2'} | sed 's/:/;/g'

# Note: I have issues building the doc this way, I guess other variables from spack-build-env.txt
# are required. In this case -DWITH_DOC:BOOL=OFF can be specified
cat magix3d/build-*/spack-configure-args.txt

#==========================================
# testing the install

# fetch the test data 
git clone --recurse-submodules https://github.com/LIHPC-Computational-Geometry/magix3d_test_data_dir.git
export MAGIX3D_TEST_DATA_DIR=$PWD/magix3d_test_data_dir

spack load python
spack load py-pytest
# when developing be careful to take the correct pyMagix3d library
# use the one in the build directory if needed
export PYTHONPATH=`spack find -p magix3d | awk 'NR==2 {print $2}'`/lib:$PYTHONPATH
# pytest should be executed from the magix3d/test_link directory as there are relative paths in some tests
cd pytest -v -s magix3d/test_link
pytest -v -s .
#==========================================

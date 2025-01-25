#==========================================
# First get a spack release
# On macos v0.22.3 or v0.23 should be chosen (because of the system's python-3.12 version ?)
git clone --depth=1 -b v0.22.2  https://github.com/spack/spack.git
# git clone --depth=1 -b v0.23.0  https://github.com/spack/spack.git
#==========================================
# can be mandatory if you have already used spack on your computer
# delete the .spack directory in the home of the user  in order to 
# have a fresh start 
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
# - in spack version 0.20.3
#sed -i 's#"{architecture}/{compiler.name}-{compiler.version}/{name}-{version}-{hash}"#"{name}"#g' spack/etc/spack/defaults/config.yaml

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
# It is activated by default in the hdf5 and cgns recipes, so choose not to use it if necessary
#spack install gmds+python+blocking+cgns ^cgns~mpi ^hdf5~mpi

# install for dev purposes
git clone git@github.com:LIHPC-Computational-Geometry/gmds.git
# you will probably want build_type=Debug or RelWithDebInfo.
# Choose the variants you need, you can check them using `spack info gmds`.
# The dev_path option does not seem to handle relative paths.
spack install gmds+python+blocking+cgns dev_path=$PWD/gmds build_type=Debug ^cgns~mpi ^hdf5~mpi ^cgal@5.6

# On macos for the MCTS component :
# 1. In the blocking component used for the MCTS the latest cgal-6.0.1 does not work, 
# cgal-5.6 should be installed instead
# 2. the glib .pc interface file contains an incorrect rpath option; in the file 
# spack/opt/spack/linux-ubuntu22.04-icelake/gcc-11.4.0/glib-2.78.3-3vfyja7wiuk536ni2jpm6b2e2lv34s45//lib/pkgconfig/glib-2.0.pc
# appears an option 
# -rpath=/home/legoffn/travail/gmds/build_20240904/spack/opt/spack/linux-ubuntu22.04-icelake/gcc-11.4.0/gettext-0.22.5-z3gxvfsrgp25buly2kju6ktqv73qk7aj/lib
# where the '=' character is not recognized by the apple-clang linker; the comma ',' character should be used instead. 
# The compilation of gmds will fail; so replace the '=' character and launch 'spack install' again


# to configure an IDE
# spack created files and directories named gmds/spack-* in the gmds source tree, where the necessary
# options are set up
# get the CMAKE_PREFIX_PATH with ';' as separators
# NOTE: in spack version >= 0.22 the spack-build-env.txt is located in gmds/build-systemname-hash/spack-build-env.txt
cat gmds/spack-build-env.txt  | grep CMAKE_PREFIX_PATH | awk -F "=" {'print $2'} | awk -F ";" {'print $1'} | sed 's/:/;/g'

# get the cmake options that were explicitly set by spack; add -DWITH_TEST:BOOL=ON
# to activate the tests
cat gmds/spack-configure-args.txt

#==========================================
# testing the install
#export PYTHONPATH=spack/opt/spack/gmds/lib:$PYTHONPATH
#spack load py-pytest
#pytest gmds/pygmds/tst gmds/test_samples
#==========================================

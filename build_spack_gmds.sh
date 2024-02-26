#==========================================
# First get a spack release
git clone --depth=1 -b v0.20.1  https://github.com/spack/spack.git
#==========================================
# can be mandatory if you have already used spack on your computer
# delete the .spack directory in the home of the user 
#==========================================
# get our recipes
git clone --branch gmds_temp --depth=1 https://github.com/LIHPC-Computational-Geometry/spack_recipes.git
#==========================================
# modifying spack configuration
#==========================================
# hard-coded modifications to spack configuration

# Optionnal: modifying the install_tree variable to make it shorter and more human readable;
# the HASH part in install directory names is removed which can lead to collisions.
# The spack/etc/spack/defaults/config.yaml file can be modified by hand
# - in spack version 0.19.2
#sed -i 's#"${ARCHITECTURE}/${COMPILERNAME}-${COMPILERVER}/${PACKAGE}-${VERSION}-${HASH}"#"${PACKAGE}"#g' spack/etc/spack/defaults/config.yaml
# - in spack version 0.20.1
#sed -i 's#"{architecture}/{compiler.name}-{compiler.version}/{name}-{version}-{hash}"#"{name}"#g' spack/etc/spack/defaults/config.yaml

# to register our recipes; it assumes that spack_recipes and spack are located at
# the same level. You can use the "spack repo add" commands instead of copying the repos.yaml file
#spack repo add ./spack_recipes/meshing_repo
#spack repo add ./spack_recipes/supersede_repo
cp spack_recipes/config/repos.yaml spack/etc/spack/defaults/repos.yaml

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
#spack install gmds+python+blocking+cgns

# install for dev purposes
git clone git@github.com:LIHPC-Computational-Geometry/gmds.git
# you will probably want build_type=Debug or RelWithDebInfo.
# Choose the variants you need, you can check them using `spack info gmds`.
# The dev_path option does not seem to handle relative paths.
spack install gmds+python+blocking+cgns dev_path=$PWD/gmds build_type=Debug

# if there are issues with mpi (activated by default in the hdf5 and cgns recipes) do not install it
#spack install gmds+python+blocking+cgns dev_path=$PWD/gmds build_type=Debug ^hdf5~mpi ^cgns~mpi

# the dev-build command seems to take a "real" version number
#spack dev-build -d ./gmds gmds@999 +python+blocking+cgns build_type=Debug

# to configure an IDE
# spack created files and directories named gmds/spack-* in the gmds source tree, where the necessary
# options are set up
# get the CMAKE_PREFIX_PATH with ';' as separators
cat gmds/spack-build-env.txt  | grep CMAKE_PREFIX_PATH | awk -F "=" {'print $2'} | awk -F ";" {'print $1'} | sed 's/:/;/g'
# get the cmake options, it is good to activate the tests -DWITH_TEST=ON
cat gmds/spack-configure-args.txt
#==========================================
# testing the install
#export PYTHONPATH=spack/opt/spack/gmds/lib:$PYTHONPATH
#spack load py-pytest
#pytest gmds/pygmds/tst gmds/test_samples
#==========================================

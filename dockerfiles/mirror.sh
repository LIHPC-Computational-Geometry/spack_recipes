#!/bin/bash

# INSTALL_DIR must be defined except for the mirror
# INSTALL_DIR is defined in the containers using this script

GH_BASE=https://github.com/LIHPC-Computational-Geometry
PRJS=(guitoolkitsvariables tkutil qtutil lima pythonutil preferences qualif qwtcharts gmds072 gmdscea qtpython triton2 vtkcontrib qtvtk qqualif mgx)

print_usage() {
	echo "Usage:"
	echo "  Download released versions and clone projects:  mirror.sh mirror-releases SPACK_RECIPES_RELEASE_NUMBER"
	echo "  Download and build released versions:           mirror.sh build-releases  SPACK_RECIPES_RELEASE_NUMBER"
	exit 1
}

build() {
	srcdir=$1
	builddir=$2
	installdir=$3
	echo -e "\e[1;32mCompiling $srcdir in $builddir\e[0m"
	cmake -S $srcdir -B $builddir --preset=ci --install-prefix=$installdir \
	&& cmake --build $builddir --target install --parallel 4 \
	|| exit 1
}

download_release_and_untar() {
	prj=$1
	version=$2
	outputdir=$3

	url=$GH_BASE/$prj/archive/refs/tags/$version.tar.gz
	echo -e "\e[1;32mDownloading $url and untar in $outputdir directory\e[0m"
	curl -L $url | tar xz --directory $outputdir || exit 1
}

download_release() {
	prj=$1
	version=$2
	if [ $# -eq 3 ]; then
		url=$3
	else
		url=$GH_BASE/$prj/archive/refs/tags/$version.tar.gz
	fi

	echo -e "\e[1;32mDownloading $url in meshing_mirrors\e[0m"

	# TO REMOVE WHEN GMDS072 IS REPLACED BY GMDS
	if [[ $prj == gmds072 ]]; then prj=gmds; fi

	mkdir -p meshing_mirror/$prj
	curl -L $url > meshing_mirror/$prj/$prj-$version.tar.gz || exit 1
}

clone() {
	prj=$1
	outputdir=$2

	url=$GH_BASE/$prj.git
	echo -e "\e[1;32mCloning in $outputdir\e[0m"
	git clone --bare $url $outputdir || exit 1
}

download_recipes_sh() {
	recipes_release=$1

	url=$GH_BASE/spack_recipes_meshing/releases/download/$recipes_release/recipes.sh
	echo -e "\e[1;32mDownloading $url in /tmp to get versions of products\e[0m"
	curl -L $url > /tmp/recipes.sh || exit 1
}


if [[ $1 = "mirror-releases" ]] && [ $# -eq 2 ]; then

	MIRROR_DIR=github-mirror-$2
	mkdir $MIRROR_DIR && cd $MIRROR_DIR
	download_recipes_sh $2
	source /tmp/recipes.sh || exit 1

	for prj in ${PRJS[@]}
	do
		echo -e "\n\e[1;33m=== Project $prj\e[0m"
		clone $prj LIHPC-Computational-Geometry/$prj
		# TO REMOVE WHEN GMDS072 IS REPLACED BY GMDS
		if [[ $prj == gmds072 ]]; then prj_version=${products[gmds]}; else prj_version=${products[$prj]}; fi
		download_release $prj $prj_version
	done

	#### Special cooking to prepare bundle
	# Spack needs vtk-maillage tarball == VTK 7.1.1 tarball
	# Spack recipe applies patches on VTK tarball
	echo -e "\n\e[1;33m=== Project vtk-maillage\e[0m"
	download_release vtk-maillage '7.1.1' https://vtk.org/files/release/7.1/VTK-7.1.1.tar.gz

	# Mirroring spack_recipes_meshing from mirrors
	echo -e "\n\e[1;33m=== Spack recipes\e[0m"
	prj=spack_recipes_meshing
	download_release_and_untar $prj $2 .
	mv $prj-$2 meshing_recipes
	tar cvfz meshing_recipes.tar.gz meshing_recipes
	rm -rf meshing_recipes

	# Tar all mirrors
	tar cvfz meshing_mirror.tar.gz meshing_mirror && rm -rf meshing_mirror
	#### End of Special cooking

	echo -e "\n\e[1;33mMirror available in: $MIRROR_DIR\e[0m"
	cd ..

elif [[ $1 = "build-releases" ]] && [ $# -eq 2 ]; then

	mkdir -p src build
	download_recipes_sh $2
	source /tmp/recipes.sh || exit 1

	for prj in ${PRJS[@]}
	do
		echo -e "\n\e[1;33m=== Project $prj\e[0m"
		# TO REMOVE WHEN GMDS072 IS REPLACED BY GMDS
		if [[ $prj == gmds072 ]]; then prj_version=${products[gmds]}; else prj_version=${products[$prj]}; fi
		download_release_and_untar $prj $prj_version src
		build src/$prj-$prj_version build/$prj $INSTALL_DIR/$prj
	done

else
	print_usage
fi

echo -e "\n\e[1;33m=== DONE \e[0m"
exit 0


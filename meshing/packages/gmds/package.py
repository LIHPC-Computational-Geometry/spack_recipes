# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install gmds
#
# You can edit this file again by typing:
#
#     spack edit gmds
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Gmds(CMakePackage):
    """GMDS: Generic Mesh Data and Services."""

    homepage = "https://github.com/LIHPC-Computational-Geometry/gmds"
    url = "https://github.com/LIHPC-Computational-Geometry/gmds/archive/refs/tags/0.0.0.tar.gz"
    git = "https://github.com/LIHPC-Computational-Geometry/gmds.git"

    version('main', branch='main')
    version('1.4.3', sha256='0eca3433084b784024502b5bfbc047184b7ed91716b5a2896279ab3b8ca3fb26')
    version('1.4.2', sha256='ed2a0aa682728b6b2f2e595d2e1388f98f85595d2772ac00761f8fddb127da19')
    version('1.4.1', sha256='fda3eed76c05d3893ce2f5a6080315e3ed62daa43c0aac8b9c7d8e1338a5237f')
    version('1.4.0', sha256='bf1b11ee4e50f199babb83ddcaa41ab6b21d5db1bbac2d1f892791f303578fa7')
    version('1.3.9', sha256='b3aff5062559beb52d885bcec3bfe1f473c99963751d2545dbf55232cfa589e1')
    version('1.3.8', sha256='4856ea2dac23f19e7b5cbe16c64cbc8083e3a2da14bcb12644f33bef28faa76a')
    version('1.3.7', sha256='102a1370257a22c7a864629507113fecb91c68f63eafb12f95dd7fd44a2f992a')
    version('1.3.6', sha256='135282c214c9a4f2c7fd1281001b026b7a35e260acb58093df1cc2907e159304')
    version('1.3.5', sha256='9391e4f6858080fe38538fa7ad3650a1237a1db5fd4c165de6b1f62c1e0a1a74')
    version('1.3.4', sha256='1d8c28e948eb26d20cac63e1884d4bac032ee74f1a5dfa70b532e847f48b9bb0')
    version('1.3.3', sha256='a8387dfb4e023877a271dd862aa2a6ec301623daccc4aef1455861368e90daea')
    version('1.3.2', sha256='cd6efea3815f0bf62951caa065e568405d938370547152a892ef28c921a99cc9')
    version('1.3.1', sha256='59e5f993b8a650d67c3d317c27151cb784084f841606934ebc235cb4c886b215')
    version('1.3.0', sha256='a21ae0d8941e91c37d7a255cb3b639823d33a0111f1a0a321adec58a027d7723')

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    variant('kmds', default=False, description='Build with Kokkos')
    variant('elg3d', default=False, description='Build Elg3D')
    variant('blocking', default=False, description='Build the blocking component')
    variant('lima', default=False, description='Provide Lima IO')
    variant('python', default=False, description='Provide GMDS Python API')
    variant('cgns', default=False, description='Provide CGNS blocking export')

    depends_on('glpk')
    # necessary to build the internal glpk
    depends_on('libtool', type='build')
    depends_on('eigen')

    depends_on('kokkos', when='+kmds')

    # necessary to find gts
    depends_on('pkgconfig', type=('build'))
    depends_on('pcre2')
    depends_on('glib')
    depends_on('gts')

    depends_on('exodusii', when='+elg3d')

    depends_on('cgns', when='+cgns')

    conflicts('+elg3d', when='~kmds', msg='elg3d cannot be built without kmds.')

    depends_on('cgal', when='+blocking')
    depends_on('py-pybind11', when='+python')
    depends_on('lima+mli2', when='+lima')

    # testing dependencies
    depends_on('lcov')
    depends_on('googletest')
    depends_on('py-pytest', when='+python')

    depends_on('nlohmann-json')

    def cmake_args(self):
        args = []
        args.append(self.define_from_variant('ENABLE_KMDS', 'kmds'))
        args.append(self.define_from_variant('ENABLE_ELG3D', 'elg3d'))
        args.append(self.define_from_variant('ENABLE_BLOCKING', 'blocking'))
        args.append(self.define_from_variant('WITH_PYTHON_API', 'python'))
        args.append(self.define_from_variant('WITH_LIMA', 'lima'))
        args.append(self.define_from_variant('WITH_CGNS', 'cgns'))
        return args

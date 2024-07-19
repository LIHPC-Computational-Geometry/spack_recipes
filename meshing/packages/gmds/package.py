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
    version('1.3.4', sha256='1d8c28e948eb26d20cac63e1884d4bac032ee74f1a5dfa70b532e847f48b9bb0')
    version('1.3.3', sha256='a8387dfb4e023877a271dd862aa2a6ec301623daccc4aef1455861368e90daea')
    version('1.3.2', sha256='cd6efea3815f0bf62951caa065e568405d938370547152a892ef28c921a99cc9')
    version('1.3.1', sha256='59e5f993b8a650d67c3d317c27151cb784084f841606934ebc235cb4c886b215')
    version('1.3.0', sha256='a21ae0d8941e91c37d7a255cb3b639823d33a0111f1a0a321adec58a027d7723')
    version('1.2.1')
    version('1.1.0')
    version('1.0.0')

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
    depends_on('gts', when='+elg3d')
    # necessary to find gts
    depends_on('pkg-config', type='build', when='+elg3d')
    depends_on('exodusii', when='+elg3d')

    depends_on('cgns', when='+cgns')

    conflicts('+elg3d', when='~kmds', msg='elg3d cannot be built without kmds.')

    depends_on('cgal', when='+blocking')
    depends_on('py-pybind11', when='+python')
    depends_on('lima', when='+lima')

    # testing dependencies
    depends_on('lcov')
    depends_on('googletest')
    depends_on('py-pytest', when='+python')

    def cmake_args(self):
        args = []
        args.append(self.define_from_variant('ENABLE_KMDS', 'kmds'))
        args.append(self.define_from_variant('ENABLE_ELG3D', 'elg3d'))
        args.append(self.define_from_variant('ENABLE_BLOCKING', 'blocking'))
        args.append(self.define_from_variant('WITH_PYTHON_API', 'python'))
        args.append(self.define_from_variant('WITH_LIMA', 'lima'))
        args.append(self.define_from_variant('WITH_CGNS', 'cgns'))
        return args

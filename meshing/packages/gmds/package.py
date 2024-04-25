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
    url      = "https://github.com/LIHPC-Computational-Geometry/gmds/archive/refs/tags/v1.2.1.tar.gz"
    git = "https://github.com/LIHPC-Computational-Geometry/gmds.git"

    version('main', branch='main')
    version('1.2.1')
    version('1.1.0')
    version('1.0.0')

    variant('kmds', default=False, description='Build with Kokkos')
    variant('elg3d', default=False, description='Build Elg3D')
    variant('blocking', default=False, description='Build the blocking component')
    variant('lima',default=False, description='Provide Lima IO')
    variant('python',default=False, description='Provide GMDS Python API')
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

    conflicts('+elg3d', when='~kmds',
             msg='elg3d cannot be built without kmds.')

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

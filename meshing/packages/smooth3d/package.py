# -*- coding: utf-8 -*-

##############################################################################
# Project Smooth3d
#
# Smooth3D is a mesh smoothing library
#
##############################################################################

from spack import *


class Smooth3d(CMakePackage):

    """Smooth3D is a mesh smoothing library"""

    homepage = 'https://github.com/LIHPC-Computational-Geometry/smooth3d'
    url = 'https://github.com/LIHPC-Computational-Geometry/smooth3d/archive/refs/tags/0.0.0.tar.gz'
    git = 'https://github.com/LIHPC-Computational-Geometry/smooth3d.git'
    maintainers = ['meshing_team']

    version('3.3.2', sha256='15dd83958c6e1febf8e6f68a92721adc01415637990b4823af24ce7001096548')
    version('3.3.1', sha256='914e844330b88f2efb9fd26f37c8df76d4a4ab7136de34d0999ba77d2c5adae1')
    version('3.3.0', sha256='2b392a2a4ed7b58ea503b423335369edf727e7c8e8054b2a321d4a2160b95a64')
    version('3.2.1', sha256='e26fde58bebdf64134ae52fb6d1d1e95490c725a479370038c3093a46de4c837')
    version('3.2.0', sha256='5e0132a5a6c75d18247db1fccfd7d64cdca7d9a8bb44c246616527a92fe809ea')

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    variant('shared', default=True, description='Build as a shared library.')

    depends_on('gmds')
    depends_on('mesquite')
    depends_on('lima')
    depends_on('machine-types')

    def cmake_args(self):
        args = []
        args.append(self.define_from_variant('BUILD_SHARED_LIBS', 'shared'))

        return args

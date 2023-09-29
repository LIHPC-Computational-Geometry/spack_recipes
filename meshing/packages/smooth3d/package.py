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
    url = 'https://github.com/LIHPC-Computational-Geometry/smooth3d/archive/refs/tags/v3.0.2.tar.gz'
    git = 'https://github.com/LIHPC-Computational-Geometry/smooth3d.git'
    maintainers = ['meshing_team']
    
    version('3.2.0', sha256='1d50222b7204e14d813ab73f569eb78faf7a353fcd62a19ca6845a8098e59044')
    version('3.0.2')#, sha256='0be62f149fa154621dbdeefdf00d026bb2bd26ff7bd88c8560bce652ff209038')
    version('3.0.1', sha256='534f067951629e5697a04d7965487193659877b0ec8dbdd1ed0200a01d60907d')
    version('3.0.0', sha256='9ef4b2e380c507cc14883a6233c1df933bf3fc49549fd7e3f87630ae2abb6c82')

    variant('shared', default=True, description='Build as a shared library.')
    variant('machinetypes', default=False, description='Links with an external machinetypes.')

    depends_on('gmds')
    depends_on('mesquite')
    depends_on('lima')
    #depends_on('machine-types', when='+machinetypes')

    def cmake_args(self):
        args = []
        args.append(self.define_from_variant('BUILD_SHARED_LIBS', 'shared'))
        args.append(self.define_from_variant('WITH_EXTERNAL_MACHINETYPES', 'machinetypes'))

        return args

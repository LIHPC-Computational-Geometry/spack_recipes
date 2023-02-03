# -*- coding: iso-8859-15 -*-

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
    
    version('3.0.2')#, sha256='0be62f149fa154621dbdeefdf00d026bb2bd26ff7bd88c8560bce652ff209038')
    version('3.0.1', sha256='534f067951629e5697a04d7965487193659877b0ec8dbdd1ed0200a01d60907d')
    version('3.0.0', sha256='9ef4b2e380c507cc14883a6233c1df933bf3fc49549fd7e3f87630ae2abb6c82')

    variant('shared', default=True, description='Build as a shared library.')

    depends_on('gmds')
    depends_on('mesquite')
    depends_on('lima')
    #removed for outside
    #depends_on('machine-types')

    def cmake_args(self):
        args = [self.define_from_variant('BUILD_SHARED_LIBS', 'shared')]

        return args

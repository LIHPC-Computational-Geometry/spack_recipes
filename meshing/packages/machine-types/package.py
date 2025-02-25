# -*- coding: utf-8 -*-
##############################################################################
# Project machine-types
#
##############################################################################

from spack import *


class MachineTypes(CMakePackage):
    """Simple C numeric types definitions"""

    homepage = 'https://github.com/LIHPC-Computational-Geometry/machine-types'
    url = 'https://github.com/LIHPC-Computational-Geometry/machine-types/archive/refs/tags/0.0.0.tar.gz'
    git = 'https://github.com/LIHPC-Computational-Geometry/machine-types.git'

    version('2.0.1', sha256='c961e25f883cf1f48f3cbace1d4263292014f5fe863854f7094f745792e94a9c')
    version('2.0.0', sha256='fb7d0095b2b4028e1cead97363c3e6c0bdaaa582ae6e90cd7f70cb8e344a730e')

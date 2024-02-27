# -*- coding: utf-8 -*-
##############################################################################
# Project machine_types
#
##############################################################################

from spack import *


class MachineTypes(CMakePackage):
    """Simple C numeric types definitions"""

    homepage = 'https://github.com/LIHPC-Computational-Geometry/machine_types'
    url = 'https://github.com/LIHPC-Computational-Geometry/machine_types/archive/refs/tags/0.0.0.tar.gz'
    git = 'https://github.com/LIHPC-Computational-Geometry/machine_types.git'

    version('2.0.0', sha256='fb7d0095b2b4028e1cead97363c3e6c0bdaaa582ae6e90cd7f70cb8e344a730e')

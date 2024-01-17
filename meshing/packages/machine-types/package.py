# -*- coding: utf-8 -*-
##############################################################################
# Project machine-types
#
##############################################################################

from spack import *


class MachineTypes(CMakePackage):
    """Simple C numeric types definitions"""

    homepage = 'https://github.com/LIHPC-Computational-Geometry/machine_types'
    url = 'https://github.com/LIHPC-Computational-Geometry/machine_types/archive/refs/tags/0.0.0.tar.gz'
    git = 'https://github.com/LIHPC-Computational-Geometry/machine_types.git'

    version('2.0.0')


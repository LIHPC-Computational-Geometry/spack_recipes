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

    version('2.0.0', sha256="15f2c41531d8ee70c45ca98a9ab1e1d1845403d75be4e2a7aa2b3335ade2d922")

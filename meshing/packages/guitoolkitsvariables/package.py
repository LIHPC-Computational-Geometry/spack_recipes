# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Guitoolkitsvariables(CMakePackage):

    homepage = 'https://github.com/LIHPC-Computational-Geometry/guitoolkitsvariables'
    url = 'https://github.com/LIHPC-Computational-Geometry/guitoolkitsvariables/archive/refs/tags/0.0.0.tar.gz'
    git = 'https://github.com/LIHPC-Computational-Geometry/guitoolkitsvariables.git'
    maintainers = ['meshing_team']

    version('develop', branch='main')
    version('1.5.0', sha256='7bbd606571634d971e645ab76613bf1bcde7d1193ab6ab10b7e3f8540640723e')
    version('1.4.3', sha256='d3455e90300eea95522d30a14a24f8f0053663e8761606ea4c91b7aa934f86e4')
    version('1.4.2', sha256='564d3d55a274faedf9d8c3b1f351f7268d2e40e58dc6a92745c53c67c45a764e')
    version('1.4.1', sha256='9670a0f383aa70b3005c85bf2e48b1b843084be172d150efc5268ab5c8dfdf1d')
    version('1.3.3', sha256='8b0cfa94d892af453bb2f6672a2f4ffcc8129ec20ae045a8f6f4e13c2b4a96de')
    version('1.3.2', sha256='3e8621469763e3216c4cea9197eba3361fb1cd4e060f0295a65e99e9262250f4')
    version('1.3.0', sha256='bc8844a6b13b35eea8cb99676e23824d6e437f7cfe3bc7aedea62a7b3e93bb64')

    def cmake_args(self):
        args = []
        return args

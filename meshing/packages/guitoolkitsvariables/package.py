# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Guitoolkitsvariables(CMakePackage):

    homepage = 'https://github.com/LIHPC-Computational-Geometry/guitoolkitsvariables'
    url = 'https://github.com/LIHPC-Computational-Geometry/guitoolkitsvariables/archive/refs/tags/1.3.0.tar.gz'
    git = 'https://github.com/LIHPC-Computational-Geometry/guitoolkitsvariables.git' 
    maintainers = ['meshing_team']

    version('develop', branch='main')
    version('1.3.2', sha256='3e8621469763e3216c4cea9197eba3361fb1cd4e060f0295a65e99e9262250f4')
    version('1.3.0', sha256='bc8844a6b13b35eea8cb99676e23824d6e437f7cfe3bc7aedea62a7b3e93bb64')

    def cmake_args(self):
        args = []
        return args

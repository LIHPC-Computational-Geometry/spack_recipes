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

    version('main', branch='main')
    version('1.3.0', sha256='bc8844a6b13b35eea8cb99676e23824d6e437f7cfe3bc7aedea62a7b3e93bb64')

    def cmake_args(self):
        args = []
        args.append(self.define_from_variant('BUILD_SHARED_LIBS', 'shared'))

        return args

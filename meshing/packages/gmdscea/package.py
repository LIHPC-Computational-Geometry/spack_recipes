# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Gmdscea(CMakePackage):

    homepage = 'https://github.com/LIHPC-Computational-Geometry/gmdscea'
    url = 'https://github.com/LIHPC-Computational-Geometry/gmdscea/archive/refs/tags/0.0.0.tar.gz'
    git = 'https://github.com/LIHPC-Computational-Geometry/gmdscea.git' 
    maintainers = ['meshing_team']

    version('main', branch='main')
    version('2.0.1', sha256='c4848f095480c6a1b1b21a8f145f4151f194a3342ac8e78bf54ad33def573e84')

    variant('shared', default=True, description='Build as a shared library.')

    depends_on('gmds')
    depends_on('lima')

    def cmake_args(self):
        args = []
        args.append(self.define_from_variant('BUILD_SHARED_LIBS', 'shared'))

        return args

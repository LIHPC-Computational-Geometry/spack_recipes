# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Gmdscea(CMakePackage):

    homepage = 'https://github.com/LIHPC-Computational-Geometry/gmdscea'
    url = 'https://github.com/LIHPC-Computational-Geometry/gmdscea/archive/refs/tags/2.0.0.tar.gz'
    git = 'https://github.com/LIHPC-Computational-Geometry/gmdscea.git' 
    maintainers = ['meshing_team']

    version('main', branch='main')
    version('2.0.0', sha256='81846ce42c2f8dea041a02823fc28cf1f435b793ec2e788097851787abfdcb4b')

    variant('shared', default=True, description='Build as a shared library.')

    depends_on('gmds')
    depends_on('lima')

    def cmake_args(self):
        args = []
        args.append(self.define_from_variant('BUILD_SHARED_LIBS', 'shared'))

        return args
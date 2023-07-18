# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install gmds
#
# You can edit this file again by typing:
#
#     spack edit gmds
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Triton2(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    homepage = 'https://github.com/LIHPC-Computational-Geometry/triton2'
    url = 'https://github.com/LIHPC-Computational-Geometry/triton2/archive/refs/tags/1.0.0.tar.gz'
    git = 'https://github.com/LIHPC-Computational-Geometry/triton2.git' 
    maintainers = ['meshing_team']

    version('main', branch='main')
    version('1.0.0', sha256='40e17e5611bee25774507fe0f074a99d03b1755eeb22fa7fa59408d1701582ff')

    variant('shared', default=True, description='Build as a shared library.')

    # FIXME: Add dependencies if required.
    depends_on('gmds')
    depends_on('gmdscea')

    def cmake_args(self):
        args = []
        args.append(self.define_from_variant('BUILD_SHARED_LIBS', 'shared'))

        return args

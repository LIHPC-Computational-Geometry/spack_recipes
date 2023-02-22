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


class Gmds(CMakePackage):

    homepage = 'https://gitlab.com/meshing'
    url = 'https://github.com/LIHPC-Computational-Geometry/gmds072/archive/refs/tags/v0.7.2.tar.gz'
    git = 'https://github.com/LIHPC-Computational-Geometry/gmds072'

    maintainers = ['meshing_team']

    #version('0.7.2'),# sha256='ab3bc88f832b12f937308c90aa0dc6b12b9ec7cff9929477beee1f3dcdbf8963')
    version('0.7.2')#, sha256='83cdc17a94ac0efb871d312e2534f3d6e0567747e339b42909d6d0c8dc1fb6e8')

    # depends_on('foo')

    def cmake_args(self):
        args = []
        return args

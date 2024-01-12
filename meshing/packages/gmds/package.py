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
    url = 'https://github.com/LIHPC-Computational-Geometry/gmds072/archive/refs/tags/0.0.0.tar.gz'
    git = 'https://github.com/LIHPC-Computational-Geometry/gmds072'

    maintainers = ['meshing_team']

    version('0.7.2', sha256='acba4344cb4f892275c9cb6580b1e6b99056346ecca02604350a5b5e84f73687')

    # depends_on('foo')

    def cmake_args(self):
        args = []
        return args

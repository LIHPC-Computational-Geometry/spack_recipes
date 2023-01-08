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


class MgxGmds(CMakePackage):

    homepage = 'https://gitlab.com/meshing'
    url = 'https://gitlab.com/meshing/gmds/-/archive/0.7.2/gmds-0.7.2.tgz'
    git = 'https://gitlab.com/meshing/gmds.git'

    homepage = 'https://github.com/LIHPC-Computational-Geometry/MGX_GMDS'
    url = 'https://github.com/LIHPC-Computational-Geometry/MGX_GMDS/archive/refs/tags/v0.7.2.tar.gz'
    git = 'https://github.com/LIHPC-Computational-Geometry/MGX_GMDS.git' 
    maintainers = ['meshing_team']
    
    version('main', branch='main')
    version('0.7.2')#, sha256='ab3bc88f832b12f937308c90aa0dc6b12b9ec7cff9929477beee1f3dcdbf8963')

    def cmake_args(self):
        args = []
        return args

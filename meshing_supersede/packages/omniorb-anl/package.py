##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install omniorb
#
# You can edit this file again by typing:
#
#     spack edit omniorb
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *

#
# omniORB 4.1.7 de ATT tres legerement retouche pour qu'il puisse s'installe dans
# un environnement spack (de base il y a un probleme de shebang ...)
#


class OmniorbAnl(AutotoolsPackage):
    """ORB de ATT"""

    homepage = ""
    url = "omniorb-anl-4.1.7.tar.gz"
    maintainers = ['meshing_team']
    version('4.1.7', sha256='3f42d97cb0344afb25c3b203ec874ad3d2ea944ea75a16bcb5e084c66273691d')
    version('4.3.0.1', sha256="9a33c5ba83f3c8a0fc5e7f30ad10acea9923b1787c50feb6c0b20cbee64f8e85")

    # On a besoin de 2.7 <= python < 3.0.0 :
    depends_on('python', type=('build', 'link', 'run'))

    def configure_args(self):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        py = self.spec['python']
        args.append(f'PYTHON={py.command.path}')
        if self.spec.satisfies('@4.2.99:'):
            args.append('CXXFLAGS=-std=c++11')

        return args

# Positionnement de l'environnement PYTHON nécéssaire sous RedHat 7/Spack Organizer master 200923
    def setup_build_environment(self, env):
        py = self.spec['python']
        env.set('PYTHON', py.command.path)

    def setup_run_environment(self, env):
        py = self.spec['python']
        env.set('PYTHON', py.command.path)

# -*- coding: utf-8 -*-
##############################################################################
# Project Preferences
#
# CEA/DAM/DSSI, 2020
##############################################################################

from spack import *


class Preferences(CMakePackage):
    """Bibliotheque d'utilitaires de gestion de preferences utilisateur reposant sur XercesC et Qt"""

    homepage = 'https://github.com/LIHPC-Computational-Geometry/preferences'
    url = 'https://github.com/LIHPC-Computational-Geometry/preferences/archive/refs/tags/6.2.2.tar.gz'
    git = 'https://github.com/LIHPC-Computational-Geometry/preferences.git'

    maintainers = ['meshing_team']

    depends_on('guitoolkitsvariables', type=('build'))
    depends_on('qtutil@5: +shared', type=('build', 'link'), when='+shared')
    depends_on('qtutil@5: ~shared', type=('build', 'link'), when='~shared')
    depends_on('tkutil')
    depends_on('xerces-c', type=('build', 'link'))
    depends_on('qt')
    depends_on('pkgconfig', type=('build'))

    version('6.3.0', sha256='300742a5dce7055f340b461d6740e89599b5c64e74bc37aa2f8953cc28ea7f90')
    version('6.2.2', sha256='5797fee3678c4b6d340a0cc4dd49fd2f050ed4574b9bba178d5c23aecadccc32')
    version('6.2.1', sha256='b39a6db6cb01fb264ce206c4ad2dbc49b6e2b9ce56ecc23c27b562937f70edb6')
    version('6.2.0', sha256='f7e7fe9ad7f7c5578e1bfbfd3318a04e15e6891459559f8d8971279701b0d458')
    version('5.6.2', sha256='f734cc05483303b5e5168da55537e212037108360c0981ae3816d034ac3214fc')
    version('5.5.7', sha256='09600a039e8458993eecaa8d7a6a8396f910caeddb3aecb4a7873d1cbaea31ae')
    version('5.5.3', sha256='9077607e1ed81d83ea675112f1be6e6d82b314a7756eef67da85cee9dad7642f')
    version('5.5.2', sha256='7f5544912c4b1044e398b5dc06ad21b5c918b461166ddc407e07396befb34137')
    version('5.1.0', sha256='8add5bcdd2ff0e70cfca49f00c4b848e771da4295143638e4978d0563050c0ed')
    version('5.0.2', sha256='2baa60b1d249c0af491a883f3fe4acd1d98a778136fef7713bbf69d83dc5c982')
    version('5.0.0', sha256='15a19af6009da3e9365684007cab7fa138d6040b01e365b0d2a8b2a0064d08e3')

    variant('shared', default=True, description='Creation de bibliotheques dynamiques (defaut:shared, annuler le defaut par ~shared)')

    def cmake_args(self):
        args = []
        args.append(self.define_from_variant('BUILD_SHARED_LIBS', 'shared'))
        if self.spec.satisfies('%intel'):
            args.append('-DCMAKE_CXX_FLAGS="-std=c++11"')

        return args

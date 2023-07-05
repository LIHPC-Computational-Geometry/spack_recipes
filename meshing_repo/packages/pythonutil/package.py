# -*- coding: utf-8 -*-
##############################################################################

from spack import *


class Pythonutil(CMakePackage):
    """Utilitaires python-cpp."""

    homepage = 'https://github.com/LIHPC-Computational-Geometry/pythonutil'
    url = 'https://github.com/LIHPC-Computational-Geometry/pythonutil/archive/refs/tags/5.6.6.tar.gz'
    git = 'https://github.com/LIHPC-Computational-Geometry/pythonutil.git' 
    maintainers = ['meshing_team']

    depends_on('tkutil')
    depends_on('python', type=('build', 'link'))
# On a besoin de swig >= 3.0.0 :
    depends_on('swig@3:', type='build')

    variant('shared', default=True, description='Creation de bibliotheques dynamiques (defaut:shared, annuler le defaut par ~shared)')

    version('5.6.6', sha256='6edd64ff6ac22ea3483a551c49e490f77071aebe50d5586ece6f8ff929d6e84f')
    version('5.0.2')

    def cmake_args(self):
        args = []
        args.append(self.define_from_variant('BUILD_SHARED_LIBS', 'shared'))

        if self.spec['python'].version < Version('3'):
            args.append('-DUSE_PYTHON_3:BOOL=OFF')
        else:
            args.append('-DUSE_PYTHON_3:BOOL=ON')

        return args

# -*- coding: utf-8 -*-
##############################################################################

from spack import *


class Pythonutil(CMakePackage):
    """Utilitaires python-cpp."""

    homepage = 'https://github.com/LIHPC-Computational-Geometry/pythonutil'
    url = 'https://github.com/LIHPC-Computational-Geometry/pythonutil/archive/refs/tags/6.2.1.tar.gz'
    git = 'https://github.com/LIHPC-Computational-Geometry/pythonutil.git' 
    maintainers = ['meshing_team']

    depends_on('tkutil')
    depends_on('python', type=('build', 'link'))
# On a besoin de swig >= 3.0.0 :
    depends_on('swig@3:', type='build')

    variant('shared', default=True, description='Creation de bibliotheques dynamiques (defaut:shared, annuler le defaut par ~shared)')

    version('6.2.1', sha256='14425325f2627bb410d9effb022aa0d1f7d7ee490766093668e3552630809acb')
    version('6.2.0', sha256='6c513802336821be8895bc7f46bc580d80a564e2d7ec6c4ee2b1c7d6383a383f')
    version('5.6.6', sha256='6edd64ff6ac22ea3483a551c49e490f77071aebe50d5586ece6f8ff929d6e84f')
    version('5.0.2')

    def cmake_args(self):
        args = []
        args.append(self.define_from_variant('BUILD_SHARED_LIBS', 'shared'))
        args.append(self.define('USE_PYTHON_3', int(self.spec['python'].version[0]) >= 3))
        args.append(self.define('USE_PYTHON_2', int(self.spec['python'].version[0]) < 3))

        return args
